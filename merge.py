from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
from rich import print
import os

# Get the path to the temporary directory

def merge(video,audio,output_path,title):
    
    # title = os.path.splitext(video)[0]

    video_clip = VideoFileClip(video).without_audio()
    audio_clip = AudioFileClip(audio)


    final_clip = video_clip.set_audio(audio_clip)

    final_clip.write_videofile(os.path.join(output_path, title + ".mp4"))

    print("[green]Video Is Ready:thumbs_up:[/green]")