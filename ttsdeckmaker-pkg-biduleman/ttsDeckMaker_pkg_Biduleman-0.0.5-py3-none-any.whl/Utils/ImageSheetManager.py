from ttsdm_pkg.Model.ImageSheet import ImageSheet


class ImageSheetManager:
    imageSheets = [ImageSheet()]
    url_id_dict = {}

    def add_image(self, url):
        if url in self.url_id_dict:
            tts_id = self.url_id_dict.get(url)
            return tts_id, ImageSheetManager.imageSheets[int(str(tts_id)[0]) - 1]
        else:
            tts_id = ImageSheetManager.imageSheets[-1].add_image(url)
            if tts_id:
                self.url_id_dict[url] = tts_id
                return tts_id, ImageSheetManager.imageSheets[-1]
            else:
                self.imageSheets.append(ImageSheet())
                return self.add_image(url)
