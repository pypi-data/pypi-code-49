from ctypes import *
import numpy as np
import os
from find_centers import find_center


class PylonCamera:
    def __init__(self, settings_path=None):
        self.is_init = False
        dir = os.path.dirname(__file__)
        dll_path = dir + r'/x64/Release/PylonCameraDll.dll'
        self.camdll = cdll.LoadLibrary(dll_path)

        # Terminate
        # Create Video
        self.camdll.CreateVideo.restype = c_int
        self.camdll.CreateVideo.argtypes = [c_char_p, c_int, c_int, POINTER(c_int)]

        # Grab image
        self.camdll.GetImage.restype = c_int
        self.camdll.GetImage.argtypes = [POINTER(c_ubyte), c_int, c_int]

        # Gram images sequence
        self.camdll.GrabImagesSequence.restype = c_int
        self.camdll.GrabImagesSequence.args = [c_int, POINTER(POINTER(c_ubyte))]

        # Get Camera Info
        self.camdll.GetCameraInfo.restype = c_int
        self.camdll.GetCameraInfo.argtypes = [POINTER(c_int), POINTER(c_int), POINTER(c_float), POINTER(c_float)]

        # Save camera settings
        self.camdll.SaveCameraSettings.restype = c_int
        self.camdll.SaveCameraSettings.argtypes = [c_char_p]

        # # Change parameters
        self.camdll.set_parameter.restype = c_int
        self.camdll.set_parameter.argtypes = [c_char_p, c_float]

        # Load camera settings
        self.camdll.LoadCameraSettings.restype = c_int
        self.camdll.LoadCameraSettings.argtypes = [c_char_p]

        # Initialize and set dll ref
        self.camdll.Initialize()
        self.is_init = True

        # Load camera settings if path is specified
        if settings_path:
            self.camdll.LoadCameraSettings(settings_path.encode())

        # get camera info
        width = c_int(0)
        height = c_int(0)
        fps = c_float(0.)
        readout_time = c_float(0.)
        ecode = self.camdll.GetCameraInfo(byref(width), byref(height), byref(fps), byref(readout_time))
        self.check_for_error(ecode, '__init__')

        # init members
        self.width = width.value
        self.height = height.value
        self.fps = fps.value
        self.readout_time = readout_time.value * 1E-6

    def __del__(self):
        # Terminate
        if self.is_init:
            self.camdll.Terminate()

    def check_for_error(self, ecode, method):
        if ecode is not 0:
            raise Exception(f"PylonCamera: {method} failed, ecode: {ecode}")

    def set_cam_parameter(self, name, val):
        ecode = self.camdll.set_parameter(c_char_p(name.encode()), val)
        self.check_for_error(ecode, "Setting exposure time")

    def grab_image(self):
        buffer = (c_ubyte * (self.width * self.height))()
        ecode = self.camdll.GetImage(buffer, self.width, self.height)
        self.check_for_error(ecode, 'grab_image')

        img = np.reshape(buffer, (self.height, self.width))

        return img

    def grab_images_sequence(self, num_of_images):
        # create some arrays
        buffers = [np.zeros(self.width * self.height, dtype="ubyte") for ii in range(num_of_images)]

        # get ctypes handles
        ctypes_arrays = [np.ctypeslib.as_ctypes(array) for array in buffers]

        # Pack into pointer array
        pointer_ar = (POINTER(c_ubyte) * num_of_images)(*ctypes_arrays)

        ecode = self.camdll.GrabImagesSequence(num_of_images, pointer_ar)
        self.check_for_error(ecode, 'grab_images_sequence')

        for ii in range(num_of_images):
            buffers[ii] = np.reshape(buffers[ii], (self.height, self.width))

        return buffers

    def create_video(self, video_path, duration, fps):
        img_skipped = c_int(-1)
        ecode = self.camdll.CreateVideo(c_char_p(video_path.encode()), duration, fps, byref(img_skipped))
        self.check_for_error(ecode, 'create_video')

        print("%s create, %d img skipped" % (video_path, img_skipped.value))

    def save_camera_settings(self, filepath):
        ecode = self.camdll.SaveCameraSettings(filepath.encode())
        self.check_for_error(ecode, 'save_camera_settings')

    def load_camera_settings(self, filepath):
        ecode = self.camdll.LoadCameraSettings(filepath.encode())
        self.check_for_error(ecode, 'load_camera_settings')

    @CFUNCTYPE(None, c_int)
    def foo(self, arg):
        '''

        :return:
        '''
        print('foo Called with', arg)

    def find_centers_in_images_sequence(self, num_of_images):
        # create some arrays
        x = np.zeros(num_of_images, dtype="double")
        y = np.zeros(num_of_images, dtype="double")
        timestamp = np.zeros(num_of_images, dtype="long")

        # get ctypes handles
        x_ctypes = np.ctypeslib.as_ctypes(x)
        y_ctypes = np.ctypeslib.as_ctypes(y)
        timestamp_ctypes = np.ctypeslib.as_ctypes(timestamp)

        ecode = self.camdll.find_centers_in_images_sequence(int(self.width), int(self.height),
                                                            byref(timestamp_ctypes), byref(x_ctypes), byref(y_ctypes),
                                                            num_of_images, find_center)
        self.check_for_error(ecode, 'FindCentersInImagesSequence')

        return x, y, timestamp

    def grab_images_using_thread(self, num_of_images):
        # create some arrays
        x = np.zeros(num_of_images, dtype="double")
        y = np.zeros(num_of_images, dtype="double")
        timestamp = np.zeros(num_of_images, dtype="uint64")

        # get ctypes handles
        x_ctypes = np.ctypeslib.as_ctypes(x)
        y_ctypes = np.ctypeslib.as_ctypes(y)
        timestamp_ctypes = np.ctypeslib.as_ctypes(timestamp)

        # Blocking function to grab all centers
        ecode = self.camdll.grab_images_using_thread(int(self.width), int(self.height),
                                                        byref(timestamp_ctypes), byref(x_ctypes), byref(y_ctypes),
                                                     num_of_images, find_center)
        self.check_for_error(ecode, 'grab_images_using_thread')

        return x, y, timestamp
