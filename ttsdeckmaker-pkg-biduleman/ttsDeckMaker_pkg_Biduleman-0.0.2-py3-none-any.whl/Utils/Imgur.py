import io
import requests

CLIENT_ID = 'Client-ID cee7939ef1e4700'
HEADERS = {"Authorization": CLIENT_ID}
IMGUR_URL = "https://api.imgur.com/3/upload"


def upload_image(image):
    temp = io.BytesIO()
    image.save(temp, format="JPEG")
    return requests.post(
        IMGUR_URL,
        headers=HEADERS,
        data={
            'image': temp.getvalue(),
            'type': 'file',
            'name': 'cards.jpg',
            'title': 'deck'
        }
    ).json()["data"]["link"]
