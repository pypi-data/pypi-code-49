from typing import Dict

import youtube_dl
from youtube_dl.utils import DownloadError

# from werkzeug.exceptions import BadRequest


def get_content_metadata(url: str) -> Dict[str, str]:
    """
    Return the metada associated to an URL.

    Return format is a dict:
    ```
    {
        "artist": <string>,
        "duration": <int>,
        "title": <string>,
        "url": <string>
    }
    ```
    """
    with youtube_dl.YoutubeDL({}) as ydl:
        try:
            metadata = ydl.extract_info(url, download=False)
        except DownloadError:
            raise BadRequest("Unrecognized URL")
        return {
            "artist": metadata["uploader"],
            "duration": metadata["duration"],
            "title": metadata["title"],
            "url": metadata["webpage_url"],
        }
