import youtube_dl
import eyed3

from pathlib import Path
from functools import partial
from tubex.utils import ClosableQueue, start_threads, stop_threads


def downloader(opts, *args):
    url, pathname = args[0]
    filename = Path(pathname.name).stem
    mp3_pathname = f"{pathname.parent / filename}.mp3"
    if Path(mp3_pathname).exists():
        print(f"Already exist: {pathname!s}")
        return mp3_pathname
    print(f"Downloading {filename}...")
    with youtube_dl.YoutubeDL(opts) as ydl:
        ydl.download([url])
        return mp3_pathname


def taggger(album, artist, mp3_pathname):
    print(f"Tagging mp3 {mp3_pathname}")
    song = eyed3.load(mp3_pathname).tag
    song.album = album
    song.artist = artist
    song.save()
    return mp3_pathname


def download(opts, album, artist, tube_url):
    download_queue = ClosableQueue()
    tag_queue = ClosableQueue()
    done_queue = ClosableQueue()

    with youtube_dl.YoutubeDL(opts) as ydl:
        download_info = ydl.extract_info(tube_url, download=False)
        if "entries" in download_info:
            download_infos = download_info["entries"]
        else:
            download_infos = [download_info]

        download_urls = [
            (d["webpage_url"], Path(ydl.prepare_filename(d))) for d in download_infos
        ]

    for url, pathname in download_urls:
        download_queue.put((url, pathname))

    mp3_download = partial(downloader, opts)
    mp3_tag = partial(taggger, album, artist)
    download_threads = start_threads(4, mp3_download, download_queue, tag_queue)
    tag_threads = start_threads(4, mp3_tag, tag_queue, done_queue)

    stop_threads(download_queue, download_threads)
    stop_threads(tag_queue, tag_threads)
    print(f"{done_queue.qsize()} items downloaded")
