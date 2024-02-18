from pytube import YouTube
from src.progress import on_progress, on_complete

def download_yt(url, output_dir) -> str:
    yt = YouTube(
        url,
        on_progress_callback=on_progress
    )

    video = yt.streams.filter(progressive=False, type='video').order_by('resolution').desc().first()
    audio = yt.streams.filter(type='audio').order_by('abr').desc().first()

    video.download(output_path=output_dir, filename='video.webm',skip_existing=False,timeout=5,max_retries=3)
    audio.download(output_path=output_dir, filename='audio.webm',skip_existing=False,timeout=5,max_retries=3)

    on_complete()

    return str(video.title)