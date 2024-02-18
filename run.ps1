# Install dependencies (output redirected to null)
python -m pip install discord asyncio requests git+https://github.com/pytube/pytube > $null 2>&1

# Run program with the provided link
python main.py
