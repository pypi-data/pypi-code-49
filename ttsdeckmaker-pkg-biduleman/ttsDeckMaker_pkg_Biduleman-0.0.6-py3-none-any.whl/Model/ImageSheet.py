from io import BytesIO

import requests
from PIL import Image
from ttsdm_pkg.Utils.Imgur import upload_image


class ImageUrlRequired(Exception):
    """imageUrl needed to add image to imageSheet"""
    pass


class ImageSheet:
    imageSheetCount = 0

    def __init__(self, width=2440, height=3400, image_per_row=5, image_per_column=5):
        self.IMAGES_PER_SHEET = image_per_row * image_per_column
        self.IMAGES_PER_ROW = image_per_row
        self.IMAGE_PER_COLUMN = image_per_column
        self.width = width
        self.height = height
        self.image = Image.new('RGB', (self.width, self.height), color='black')
        self.url = ""
        self.cardImageCount = 0
        ImageSheet.imageSheetCount += 1
        self.id = self.imageSheetCount

    def add_image(self, url):
        if self.cardImageCount is 24:
            self.url = self.get_url()
            return False
        else:
            image = Image.open(BytesIO(requests.get(url).content))
            pos_x = self.cardImageCount % self.IMAGES_PER_ROW
            pos_y = int(self.cardImageCount / self.IMAGE_PER_COLUMN)
            box_position = self.get_box_position(pos_x, pos_y)
            self.image.paste(image, box_position)
            self.cardImageCount += 1
            return self.id * 100 + (self.cardImageCount - 1)

    def add_hidden_face_image(self, url):
        if url:
            image = Image.open(BytesIO(requests.get(url).content))
            box_position = self.get_box_position(self.IMAGES_PER_ROW, self.IMAGE_PER_COLUMN)
            self.image.paste(image, box_position)
        else:
            return

    def get_box_position(self, pos_x, pos_y):
        return (int(self.width / self.IMAGES_PER_ROW * pos_x),
                int(self.height / self.IMAGE_PER_COLUMN * pos_y),
                int(self.width / self.IMAGES_PER_ROW * (pos_x + 1)),
                int(self.height / self.IMAGE_PER_COLUMN * (pos_y + 1)))

    def get_url(self):
        if self.url:
            return self.url
        else:
            self.url = upload_image(self.image)
            return self.url

    def get_json_dict(self):
        return {
            str(self.id): {
                "NumWidth": self.IMAGES_PER_ROW,
                "NumHeight": self.IMAGE_PER_COLUMN,
                "FaceURL": self.get_url(),
                "BackURL": ""
            }
        }
