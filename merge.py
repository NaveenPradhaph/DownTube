from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
from rich import print
import os

def merge(video,audio):
    
    title = os.path.splitext(video)[0]

    video_clip = VideoFileClip(f"D:\TryOn\Videos\{video}")
    audio_clip = AudioFileClip(f"D:\TryOn\Audios\{audio}")

    final_clip = video_clip.set_audio(audio_clip)

    final_clip.write_videofile(os.path.join("D:\TryOn\Vid", title + ".mp4"))

    print("[green]Video Is Ready:thumbs_up:[/green]")