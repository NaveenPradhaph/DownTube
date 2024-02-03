import inquirer
from pytube import YouTube
from download_video import download_v
from download_audio import download_a
from pyfiglet import Figlet
from merge import merge
from pytube.__main__ import YouTube
from makefolder import make_downtube
from rich import print
figlet = Figlet(font='big')
def main():
    print(f"[red]{figlet.renderText('Downtube')}[/red]")
    url = input("Enter the link : ")
    yt = YouTube(url=url)

    video = yt.streams.filter(only_video=True)

    resolution = dict()

    for x in video:
        resolution[x.itag] = [x.resolution,x.fps,x.filesize_mb]

    choices = [
        (
            f"{resolution.get(x)[0]} --- {resolution.get(x)[1]}fps --- {resolution.get(x)[2]}mb",
            x
        )
        for x in resolution
    ]

    questions = [
        inquirer.List('choice',
                      message="Select an option:",
                      choices=choices,
        ),
    ]

    answers = inquirer.prompt(questions)
    
    selected_option = list(answers.values())

    video_path = download_v(url, selected_option[0])
    audio_path = download_a(url)
    output_path = make_downtube()
    print(output_path)
    print(video_path)
    print(audio_path)
    merge(video_path,audio_path,output_path)



if __name__ == "__main__":
    main()