import os
from src.create_folder import create_folder
from src.downloader import download_yt
from src.merge import merge
from src.remove_spaces import remove_spaces
from src.upload import upload
from src.cleanup import cleanup

async def download(url, output_dir, filebin, audio_only, edit_message, response_obj, message_obj) -> str:
    video_file = 'video.webm'
    audio_file = 'audio.webm'

    try:
        # create folder
        print(f"Creating '{output_dir}'")
        await edit_message(response_obj, message_obj, f"5%")
        create_folder(output_dir)

        # download video & audio
        print(f"Downloading '{url}'")
        await edit_message(response_obj, message_obj, f"10%")
        title = download_yt(url, output_dir)
        title += '.mp4'

        # remove spaces from title
        print(f"Renaming '{title}'")
        await edit_message(response_obj, message_obj, f"40%")
        title = remove_spaces(title)

        # merge video & audio if necessary
        if audio_only:
            os.rename(f"{output_dir}/{audio_file}", f"{output_dir}/{title}")
        else:
            print(f"Merging '{output_dir}/{video_file}' and '{output_dir}/{audio_file}' into '{output_dir}/{title}'")
            await edit_message(response_obj, message_obj, f"50%")
            merge(f"{output_dir}/{video_file}", f"{output_dir}/{audio_file}", f"{output_dir}/{title}")

        # upload to filebin
        print(f"Uploading '{title}'")
        await edit_message(response_obj, message_obj, f"60%")
        upload(filebin, title, f"{output_dir}/{title}")

        # cleanup artifacts
        print("Cleaning up artifacts")
        await edit_message(response_obj, message_obj, f"90%")
        # cleanup(output_dir)

        print(f"\033[92m Download file at: \033[95m https://filebin.net/{filebin}/{title} \033[0m")
        return f"https://filebin.net/{filebin}/{title}"
    except Exception as ex:
        print(f"\033[91m Failed: {str(ex)} \033[0m")
