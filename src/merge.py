import subprocess

def merge(audio_file, video_file, output_file):
    try:
        cmd = ['ffmpeg', '-i', audio_file, '-i', video_file, '-c', 'copy', output_file]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception as ex:
        raise Exception('Merge failed') from ex
