# image_sequence_streamer.py
""" Loads an Image sequence and returns each frame sequentially when called. Provides options for looping the stream or
repeating the last frame"""
import cv2
import os
import numpy as np

__version__ = '0.3'
__author__ = 'Rob Dupre (KU)'


class ImageSequenceStreamer:
    def __init__(self, seq_path, start_frame=0, identifier=0, frame_size=(None, None), loop_last=True, repeat=False):
        """Loads an Image sequence and returns each frame sequentially when called. Provides options for looping the
        stream or repeating the last frame
        :param seq_path: String identifying the folder location of the images.
        :param start_frame: [OPTIONAL] Allows for the image sequence to start at a specific point
        :param frame_size: [OPTIONAL] Allows for loaded frames to be resized
        :param loop_last: [OPTIONAL] if True last frame is repeated until stop is called
        :param repeat: [OPTIONAL] if True repeats all frames until stop is called
        """
        self.id = identifier
        self.start_frame = start_frame
        self.counter = self.start_frame - 1

        self.folder_location = seq_path
        self.file_list = []
        # GET LIST OF IMAGES AT FILE LOCATION
        valid_images = ('.jpg', '.png', '.tga', '.tif', '.jpeg')
        try:
            for f in sorted(os.listdir(self.folder_location)):
                ext = os.path.splitext(f)[1]
                if ext.lower().endswith(valid_images):
                    self.file_list.append(os.path.join(self.folder_location, f))
            self.num_frames = len(self.file_list)
        except Exception as e:
            print(e)
            self.isOpened = False
        else:
            # GET THE FRAME SIZE FROM THE FIRST IMAGE IF NOT SPECIFIED
            try:
                temp_image = cv2.imread(self.file_list[0])
            except Exception as e:
                print(e)
                print('FAILED TO LOAD MEDIA ' + str(self.id) + '.')
                self.isOpened = False
            else:
                self.isOpened = True

            self.stopped = False
            if frame_size[0] is None:
                if temp_image.shape[0] > temp_image.shape[1]:
                    self.size = (temp_image.shape[0], temp_image.shape[1])
                else:
                    self.size = (temp_image.shape[1], temp_image.shape[0])
            else:
                self.size = (frame_size[0], frame_size[1])
            self.width = self.size[0]
            self.height = self.size[1]

            self.current_frame = np.zeros([200, 200, 3])
            self.grabbed = False
            self.loop_last = loop_last
            self.repeat = repeat
            if self.loop_last and self.repeat:
                print('Cannot loop the last frame and repeat, repeating will take precedence')

    def open(self):
        """Returns if the Image Sequence stream is open
        :return: bool success or fail
        """
        return self.isOpened

    def read(self):
        """Updates the current_image"""

        if not self.stopped:

            # SET COUNTER FOR NEXT FRAME
            if self.counter < self.num_frames:
                self.counter = self.counter + 1

            # THIS IS NOW THE LAST IMAGE IN THE LIST
            if self.counter == self.num_frames:
                # BREAK OUT THE METHOD AS CURRENT IMAGE IS STILL LOADED FROM BEFORE AND NO UPDATE IS REQUIRED
                if not self.loop_last and not self.repeat:
                    self.counter = self.num_frames - 1
                    self.stopped = True
                    self.grabbed = False
                    return
                # RESTART THE COUNTER
                if self.repeat:
                    self.counter = self.start_frame
                # LOOPING THE LAST FRAME
                else:
                    self.counter = self.num_frames - 1
                    return
            # LOAD THE NEXT IMAGE AS LONG AS THERE ARE STILL ENTRIES IN THE file_list,
            try:
                self.current_frame = cv2.resize(cv2.imread(self.file_list[self.counter]), self.size)
            except Exception as e:
                print(e)
                self.grabbed = False
            else:
                self.grabbed = True

        # NOW STOPPING THE IMAGE LOADING
        else:
            self.grabbed = False

    def start(self):
        """Sets the self.working bool to True starting the cycle of frames
        """
        self.stopped = False

    def stop(self):
        """Sets the self.working bool to False stopping the cycle of frames
        """
        self.stopped = True


if __name__ == '__main__':
    import time
    cap = ImageSequenceStreamer(os.path.abspath('test_data/'), start_frame=3, loop_last=False, repeat=False)
    # cap = ImageSequenceStreamer(os.path.abspath('test_data/'), frame_size=(352, 240), loop_last=True, repeat=False)
    # cap = ImageSequenceStreamer(os.path.abspath('test_data/'), frame_size=(352, 240), loop_last=True, repeat=True)
    # cap = ImageSequenceStreamer(os.path.abspath('test_data/'), frame_size=(352, 240), loop_last=False, repeat=True)
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

