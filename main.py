import sys
import random
from src.download import download

if __name__ == '__main__':
    if len(sys.argv) < 1:
        print('\033[91m' + "More arguments required (python main.py link)" + '\033[0m')

    url = sys.argv[1]
    output_dir = './output'
    filebin = 'vu7lrn7ceafc' + str(random.randint(1000,9999))

    download(url, output_dir, filebin)
