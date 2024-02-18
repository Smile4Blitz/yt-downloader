import requests

def upload(bin_name, filename, file_path):
    url = f'https://filebin.net/{bin_name}/{filename}'
    headers = {'Content-Type': 'application/octet-stream'}
    with open(file_path, 'rb') as file:
        requests.post(url, headers=headers, data=file)
