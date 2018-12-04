#!/usr/bin/python3

from pyquery import PyQuery
import readline
import requests
from urllib.parse import urlparse
from urllib.parse import parse_qs
from os.path import join as pjoin

def main():
    export_path = '/mnt/nfsserver/internal/kodi-data/yt-music-videos/'
    while True:
        url = rlinput("url: ")
        parsed = urlparse(url)
        video_id = parse_qs(parsed.query)['v'][0]
        r = requests.get(url)
        pq = PyQuery(r.text)
        title = pq('title').text()
        if title.endswith(' - YouTube'):
            title = title[:-10]
        title = rlinput("title: ", title)
        path = "%s%s.strm" % (export_path, title)
        with open(path, "w") as f:
            content = 'plugin://plugin.video.youtube/play/?video_id=%s' % video_id
            f.write(content)

def rlinput(prompt, prefill=''):
   readline.set_startup_hook(lambda: readline.insert_text(prefill))
   try:
      return input(prompt)
   finally:
      readline.set_startup_hook()

if __name__ == "__main__":
    main()
