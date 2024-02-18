from src.create_folder import create_folder
from src.downloader import download_yt
from src.merge import merge
from src.remove_spaces import remove_spaces
from src.upload import upload
from src.cleanup import cleanup

def download(url, output_dir, filebin):
    video = output_dir + '/video.webm'
    audio = output_dir + '/audio.webm'

    try:
        # create folder
        print(f"Creating '{output_dir}'")
        create_folder(output_dir)

        # download video & audio
        print(f"Downloading '{url}'")
        title = download_yt(url, output_dir)

        # remove spaces from title
        print(f"Renaming '{title}'")
        title = remove_spaces(title)

        # merge video & audio
        print(f"Merging into '{title}'")
        pwd = output_dir + '/' + title
        merge(video, audio, pwd)

        # upload to filebin
        print(f"Uploading '{title}'")
        upload(filebin, title, output_dir + '/' + title)

        # cleanup artifacts
        print("Cleaning up artifacts")
        cleanup(output_dir)

        print('\033[92m' + f"Download file at: " + '\033[95m' + f"https://filebin.net/{filebin}/{title}" + '\033[0m')
    except Exception as ex:
        print('\033[91m' + f'Failed: {str(ex)}' + '\033[0m')
