from pytube import YouTube,Stream
from rich import  print
import shutil
import time
import sys
import io

# Get the path to the temporary directory

def on_progress(
    stream: Stream, chunk: bytes, bytes_remaining: int
) -> None:  # pylint: disable=W0613
    filesize = stream.filesize
    bytes_received = filesize - bytes_remaining
    display_progress_bar(bytes_received, filesize)

start_time = time.time()



def display_progress_bar(
    bytes_received: int, filesize: int, ch: str = "▬", scale: float = 0.55
) -> None:
    """Display a simple, pretty progress bar.

    Example:
    ~~~~~~~~
    PSY - GANGNAM STYLE(강남스타일) MV.mp4
    ↳ |▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬| 100.0%

    :param int bytes_received:
        The delta between the total file size (bytes) and bytes already
        written to disk.
    :param int filesize:
        File size of the media stream in bytes.
    :param str ch:
        Character to use for presenting progress segment.
    :param float scale:
        Scale multiplier to reduce progress bar size.

    """
    columns = shutil.get_terminal_size().columns
    max_width = int(columns * scale)

    filled = int(round(max_width * bytes_received / float(filesize)))
    remaining = max_width - filled
    progress_bar = ch * filled + " " * remaining
    # 
    downloaded_size = f"{bytes_received / (1024 * 1024):.2f}MB"
    total_size = f"{filesize / (1024 * 1024):.2f}MB"
    elapsed_time = time.time() - start_time
    download_speed = bytes_received / elapsed_time  # Bytes per second
    time_left = (filesize - bytes_received) / download_speed
    time_left_str = time.strftime("%H:%M:%S", time.gmtime(time_left))
    # 
    percent = round(100.0 * bytes_received / float(filesize), 1)
    text = f"↳|{progress_bar}| {percent}% - {downloaded_size}/{total_size} - {time_left_str} left\r"
    sys.stdout.write(text)
    sys.stdout.flush()





def download_a(url):
    yt = YouTube(url=url,on_progress_callback=on_progress)
    audio = yt.streams.filter(only_audio=True)
    print("[magenta]AudioHarvest...[/magenta]")
    highest_quality_stream = None
    highest_bitrate = 0

    # print(audio)

    # # Iterate through the streams to find the highest quality audio
    for stream in audio:
        if stream.type == "audio":
            bitrate = int(stream.abr.replace("kbps", ""))
            if bitrate > highest_bitrate:
                highest_bitrate = bitrate
                highest_quality_stream = stream

    stream = yt.streams.get_by_itag(highest_quality_stream.itag)
    # audio_buffer = io.BytesIO(stream.stream_to_buffer().read())
    audio_buffer = io.BytesIO()

    # Download the video content directly into the buffer
    stream.stream_to_buffer(audio_buffer)
    return audio_buffer

    # return stream.download(output_path=temp_dir,filename=stream.default_filename)