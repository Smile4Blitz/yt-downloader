import os

def cleanup(folder):
    try:
        # Remove all files in the folder
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
        
        # Remove the empty directory
        os.rmdir(folder)
    except Exception as ex:
        raise Exception(f"Failed to cleanup {folder}") from ex
