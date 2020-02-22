from pytube import YouTube


def get_tube(url):
    tube = YouTube(url)
    return tube

def get_streams(tube, **kwargs):
    streams = tube.streams.filter(**kwargs)
    return streams
