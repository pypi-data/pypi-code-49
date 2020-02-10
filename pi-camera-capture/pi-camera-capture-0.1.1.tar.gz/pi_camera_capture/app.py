import socket
from time import time
import requests
from pi_camera_capture.cam import capture


HOSTNAME = socket.gethostname()


def query_distance(url):
    return requests.get(url).json().get("distance", None)


def upload_image(url, image):
    return requests.post(url, files={"file": image})


def upload_image_if_distance_exist(distance_server_url, upload_server_url):
    now = int(time() * 10 ** 9)
    image = capture()
    distance = query_distance("{}/?time={}".format(distance_server_url, now))
    if distance:
        image.name = "{}_{}.jpg".format(HOSTNAME, distance)
        upload_image(upload_server_url, image)


def main(distance_server_url, upload_server_url):
    while True:
        try:
            upload_image_if_distance_exist(
                distance_server_url, upload_server_url
            )
        except Exception as ex:  # pylint: disable=broad-except
            print(ex)
