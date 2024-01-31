# from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
# from rich import print
# import os
# import io

# # Get the path to the temporary directory

# def merge(video,audio,output_path,title):
    
#     # title = os.path.splitext(video)[0]
#     video.seek(0)
#     audio.seek(0)
#     video_clip = VideoFileClip(io.BytesIO(video))
#     audio_clip = AudioFileClip(io.BytesIO(audio))


#     final_clip = video_clip.set_audio(audio_clip)

#     final_clip.write_videofile(os.path.join(output_path, title + ".mp4"))

#     print("[green]Video Is Ready:thumbs_up:[/green]")


from moviepy.editor import VideoFileClip, AudioFileClip
from rich import print
import os
import io
import tempfile

def merge(video, audio, output_path, title):
    with tempfile.NamedTemporaryFile(suffix=".mp4", delete=False) as video_temp:
        video_temp.write(video.getvalue())
        video_temp.seek(0)

        # Create VideoFileClip from temporary file path
        video_clip = VideoFileClip(video_temp.name).without_audio()

    audio_temp = AudioFileClip(io.BytesIO(audio.getvalue()))
    audio_temp.seek(0)
    audio_clip = AudioFileClip(audio_temp)

    final_clip = video_clip.set_audio(audio_clip)

    final_clip.write_videofile(os.path.join(output_path, title + ".mp4"))

    print("[green]Video Is Ready:thumbs_up:[/green]")
