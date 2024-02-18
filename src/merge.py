import subprocess

def merge(audio_file, video_file, output_file):
    try:
        cmd = ['ffmpeg', '-i', video_file, '-i', audio_file, '-c', 'copy', '-y', output_file]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception as ex:
        raise Exception('Merge failed') from ex
