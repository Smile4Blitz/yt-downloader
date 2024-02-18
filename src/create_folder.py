import os  
from src.cleanup import cleanup

def create_folder(output_dir) -> bool:
    try:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        else:
            cleanup(output_dir)
        return True
    except Exception as ex:
        raise Exception('Folder creation failed.') from ex