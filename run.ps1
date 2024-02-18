# Install dependencies (output redirected to null)
python -m pip install requests git+https://github.com/pytube/pytube > $null 2>&1

# Ask for link
$link = Read-Host "Enter YouTube link"

# Run program with the provided link
python main.py $link