def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    perc_completed = bytes_downloaded / total_size * 100
    if perc_completed < 100:
        print(f"Progress: {perc_completed}")
    return

def on_complete():
    print('\033[92m' + "Progress: 100%" + '\033[0m')
    return
