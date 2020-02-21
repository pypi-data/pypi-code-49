import threading

def start_thread(func):
    def wrapped(*args, **kwargs):
        thread = threading.Thread(target=func, args=args, kwargs=kwargs, daemon=True)
        thread.start()
        return thread
    return wrapped

def standart_position_output(func):
    """
    :param target_position: 1x6 list
    """
    def wrapped(self):
        point = {}
        rotation = {}
        points_list = [round(item, 5) for item in func(self)]

        for axis, value in zip(['x', 'y', 'z'], points_list[0:3]):
            point.update({axis: value})
        for rot, value in zip(['roll', 'pitch', 'yaw'], points_list[3:6]):
            rotation.update({rot: value})

        ref_frame = {'point': point, 'rotation': rotation}
        return ref_frame
    return wrapped