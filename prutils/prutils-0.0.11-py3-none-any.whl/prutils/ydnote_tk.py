import requests

from prutils.string import get_re_last
from prutils.url import get_url_param_dict


class YDTK:
    def __init__(self, shared_url):
        self.shared_url = shared_url
        self.pre_init()

    def pre_init(self):
        pass

    def get_shared_id(self):
        return get_url_param_dict(self.shared_url)["id"]

    def get_last_img_url(self):
        url = "https://note.youdao.com/yws/public/note/" + self.get_shared_id()
        r = requests.get(url)
        j = r.json()
        return get_re_last('<img data-media-type="image" src="(.*?)".*?>', j["content"])


