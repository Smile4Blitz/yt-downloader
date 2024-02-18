# YouTube Video Downloader

This program is written in [Python](https://www.python.org/) and is designed to download & merge the highest quality available video and audio streams from [YouTube](https://www.youtube.com/), upload the resulting video file to [FileBin](https://filebin.net/), and return a download link.

I also intend on implementing this into a Discord bot.

## Usage

To use this program, follow these steps:

1. Ensure you have Python installed on your system.
2. Clone the repository 

   ```powershell
   git clone https://github.com/Smile4Blitz/yt-downloader
   ```
3. Run the Powershell script "run.ps1" in the following way:

   ```powershell
   python run.py <YouTube_URL>
   ```
   Replace `<YouTube_URL>` with the URL of the YouTube video you want to download.
4. Run the Powershell script with the command:

   ```powershell
   ./run.ps1 <YouTube_URL>
   ```
   Replace `<YouTube_URL>` with the URL of the YouTube video you want to download.

## Functionality

- Downloads & merges the highest quality available video and audio streams from Youtube
- Uploads the resulting video file to [FileBin](https://filebin.net/).
- Returns a download link for the uploaded video file.

## Dependencies

- Requires Python3: https://www.python.org/downloads/
- Requires ffmpeg: https://ffmpeg.org/download.html#build-windows

## Disclaimer

This program is provided as-is without any warranties. Use it responsibly and adhere to YouTube's terms of service regarding video downloads.

## Contributors

- Smile4Blitz - Initial implementation
