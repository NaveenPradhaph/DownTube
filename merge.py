from moviepy.editor import VideoFileClip, AudioFileClip
from rich import print
import os
from moviepy.video.io.ffmpeg_reader import ffmpeg_parse_infos

def merge(video, audio, output_path):
    title = os.path.splitext(video)[0]

    # Get video information using ffmpeg_parse_infos
    video_infos = ffmpeg_parse_infos(video)
    
    # Print the 'infos' dictionary for debugging
    print("Video Infos:", video_infos)

    # Check if 'video_fps' is in the video_infos dictionary
    if 'video_fps' in video_infos:
        fps = video_infos['video_fps']
    else:
        # Set a default value if 'video_fps' is not present
        fps = 30  # You can adjust this value as needed

    video_clip = VideoFileClip(video)
    video_clip = video_clip.set_fps(fps)
    audio_clip = AudioFileClip(audio)

    final_clip = video_clip.set_audio(audio_clip)

    final_clip.write_videofile(os.path.join(output_path, title + ".mp4"))
    print("[green]Video Is Ready:thumbs_up:[/green]")
