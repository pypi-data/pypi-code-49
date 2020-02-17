import cv2
import os

from innolab_utils.pylon_camera_dll.PylonCamera import PylonCamera


def grab_image(pcam):
    img = pcam.grab_image()

    cv2.namedWindow('img', cv2.WINDOW_GUI_EXPANDED | cv2.WINDOW_FREERATIO)
    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def create_video(pcam):
    video_path = "dump/test_video.avi"
    pcam.create_video(video_path, 3, 25)

    vidcap = cv2.VideoCapture(video_path)
    framerate = vidcap.get(5)
    framecount = vidcap.get(7)

    print("framerate: %d, framecount: %d" % (framerate, framecount))


def grab_images_sequence(pcam):
    images = pcam.grab_images_sequence(130)

    cv2.namedWindow('img', cv2.WINDOW_GUI_EXPANDED | cv2.WINDOW_FREERATIO)

    for img in images:
        cv2.imshow('img', img)
        cv2.waitKey(3)

    cv2.destroyAllWindows()

    # dump images to video
    img = images[0]
    width = img.shape[1]
    height = img.shape[0]
    writer = cv2.VideoWriter("dump/grab_images_sequence.avi", cv2.VideoWriter_fourcc(*"XVID"), int(pcam.fps), (width, height), False)
    for img in images:
        writer.write(img)
    writer.release()


def save_and_load_camera_settings(pcam):
    filepath = './dump/save_and_load_camera_settings.pfs'
    if os.path.exists(filepath):
        os.remove(filepath)

    pcam.save_camera_settings(filepath)
    if not os.path.exists(filepath):
        raise("failed saving settings to %s" % filepath)

    pcam.load_camera_settings(filepath)


if __name__ == "__main__":
    path = r"C:\Development\feedback_calibration\src\bgVGA.pfs"
    pcam = PylonCamera(path)

    grab_image(pcam)

    # create_video(pcam)
    # grab_images_sequence(pcam)
    # save_and_load_camera_settings(pcam)
