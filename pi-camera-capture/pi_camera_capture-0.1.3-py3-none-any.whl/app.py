import socket
import time
import requests
from pi_camera_capture.cam import capture


HOSTNAME = socket.gethostname()


def query_distance(url):
    return requests.get(url).json()


def upload_image(url, image):
    return requests.post(url, files={"file": image})


def upload_image_if_distance_exist(
    distance_server_url, upload_server_url, sleep_time=0.01
):
    now = int(time.time() * 10 ** 9)
    image = capture()
    time.sleep(sleep_time)
    result = query_distance("{}/?time={}".format(distance_server_url, now))
    if result:
        image.name = "{}_{}_{}_{}.jpg".format(
            result["time"], now, HOSTNAME, result["distance"]
        )
        upload_image(upload_server_url, image)


def main(distance_server_url, upload_server_url, sleep_time=0.01):
    while True:
        try:
            upload_image_if_distance_exist(
                distance_server_url, upload_server_url, sleep_time
            )
        except Exception as ex:  # pylint: disable=broad-except
            print(ex)
