# video_streamer.py
"""Implementation of an RTSP or Video stream reader utilising OpenCV"""
import cv2
import time
import numpy as np
from threading import Thread
from rdutils.get_incrementer import get_incrementer

__version__ = '0.5'
__author__ = 'Rob Dupre (KU)'


class VideoStreamer:
    def __init__(self, cam_file_path, frame_size=(None, None), identifier=1, threaded=True):
        """Opens a video file
        :param cam_file_path: string of the video file location or RTSP Stream address (with authentication)
        :param frame_size: (OPTIONAL) When present will resize to the frame_size the loaded frames
        :param identifier: (OPTIONAL) id for this stream
        :param threaded: (OPTIONAL) bool determining if the video should stream in a sperate thread
        """
        self.stream = cv2.VideoCapture(cam_file_path)
        self.id = identifier
        self.threaded = threaded
        self.counter = 0
        if self.open():
            self.fps = self.stream.get(cv2.CAP_PROP_FPS)
            try:
                self.num_frames = int(self.stream.get(cv2.CAP_PROP_FRAME_COUNT))
            except Exception as e:
                print(e)
                self.num_frames = -1
        else:
            print('FAILED TO LOAD MEDIA ' + str(self.id) + '.')

        self.stopped = False
        self.size = frame_size
        if self.size[0] is None:
            self.width = self.stream.get(cv2.CAP_PROP_FRAME_WIDTH)
            self.height = self.stream.get(cv2.CAP_PROP_FRAME_HEIGHT)
        else:
            self.width = self.size[0]
            self.height = self.size[1]
        self.current_frame = np.zeros([200, 200, 3])
        self.grabbed = False

    def open(self):
        """Returns if the Video stream is open, (mirrors cv2.VideoCapture.isOpened())
        :return: bool success or fail
        """
        return self.stream.isOpened()

    def _read_frame(self):
        """Gets the next frame and if a specific size has been specified will resize the frame accordingly
        """
        self.grabbed, image = self.stream.read()
        # CHECK IF THE IMAGE WAS GRABBED
        if self.grabbed:
            self.counter += 1
            if self.size[0] is None:
                self.current_frame = image
            else:
                self.current_frame = cv2.resize(image, self.size)

    def read(self):
        """Reads the next frame into self.current_frame, for use when not threaded
        """
        if not self.threaded:
            self._read_frame()

    def start(self):
        """Sets self.stopped to False and if threaded creates thread to handle the update() function
        :return: self
        """
        if self.threaded:
            t = Thread(target=self._update, args=())
            t.daemon = True
            t.start()
            # ADD DELAY TO ALLOW STREAMER TO BUFFER SOME INITIAL FRAMES
            time.sleep(0.5)
        self.stopped = False
        return self

    def _update(self):
        """Updates the self.current_frame with the latest frame from the streamer object and the self.grabbed bool
        will close the thread if the stream fails.
        """
        while True:
            if self.stopped:
                return
            self._read_frame()

    def stop(self):
        """Sets the self.stopped bool to True but doesn't close the thread, stopping the reading of frames
        """
        self.stopped = True

    def save(self, filename):
        """Saves the current frame to a png file
        :param filename: string filename to save the image
        """
        print('Screenshot Saved')
        cv2.imwrite(get_incrementer(self.counter, 6) + '.png', self.current_frame)


if __name__ == '__main__':
    cap = VideoStreamer('rtsp://admin:admin@192.168.0.35:8554/channels/1', threaded=False)
    # cap = VideoStreamer('test_data/carpark_timelapse.mp4', threaded=True)
    # cap = VideoStreamer('rtsp://admin:admin@192.168.0.35:8554/channels/1', threaded=True)
    cap.start()
    while cap.open():
        # WILL DO NOTHING IF THREADED
        cap.read()
        cv2.imshow('Video', cap.current_frame)
        print(cap.counter)
        if cv2.waitKey(1) == ord('c') or not cap.grabbed:
            exit(0)
        # SLEEP TO ENSURE THREADING IS WORKING CORRECTLY (COUNTER SHOULD GO UP OUTSIDE OF READ CALLS)
        time.sleep(1)
