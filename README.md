# RarBG-Search
This script allows a user to search through the old rarbg archive for magnet links from before
website went down

## Requirements
```
python >= 3.10.x
python-venv
```

## Preparing the environment
```bash
python3 -m venv .venv
source ./.venv/bin/activate
pip3 install -r requirements.txt
```

## Usage
```bash
user@localhost$ ./search.py
 [i] Connecting to database...
 [i] Loading torrents from database...
Search?> Interstellar
 [i] Matching torrents:
 [+]    Interstellar.2014.1080p.xxxxx.xxxxxxxx.xxxx.xxxxxx(Size: 0 GB)
            magnet:?xt=urn:btih:98ASDF88ASDFLA9081234098143AER98123FFF90
 [i] Torrents Found: 39
Search ?> 
```