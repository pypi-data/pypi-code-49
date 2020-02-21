"""
Name : VideoCodec.py
Author  : Cash
Contact : tkggpdc2007@163.com
Time    : 2020-01-08 10:52
Desc:
"""

import os


def convert_mp42png(video_path, output_dir):
    """
    视频生成图片序列
    :param video_path:
    :param output_dir:
    :return:
    """
    _command = "ffmpeg -i {} -f image2 {}/%05d.png -y"
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    _command = _command.format(video_path, output_dir)
    res = os.system(_command)
    if res == 0:
        file_names = os.listdir(output_dir)
        file_names = sorted(file_names)
        return [os.sep.join((output_dir, x)) for x in file_names]
    else:
        os.remove(output_dir)
        return None


def convert_png2mp4(image_dir, output_path, fps=25.0):
    """
    图片生成视频
    :param image_dir:
    :param output_path:
    :param fps: 帧率
    :return:
    """
    _command = "ffmpeg -f image2 -i {}/%05d.png -r {} {} -y"
    if not os.path.exists(image_dir):
        return False
    _command = _command.format(image_dir, fps, output_path)
    res = os.system(_command)
    return True if res == 0 else False


def convert_mp42ts(video_path, output_path):
    """
    格式转换: mp4转ts
    :param video_path:
    :param output_path:
    :return:
    """
    _command = "ffmpeg -y -i {} -vcodec copy -acodec copy -vbsf h264_mp4toannexb {}"
    _command = _command.format(video_path, output_path)
    res = os.system(_command)
    return True if res == 0 else False


def compress_mp4(video_path, output_path):
    """
    视频压缩
    :param video_path:
    :param output_path:
    :return:
    """
    _command = "ffmpeg -threads 2 -re -i {} -b:v 1000k -b:a 32k {}"
    _command = _command.format(video_path, output_path)
    res = os.system(_command)
    return True if res == 0 else False


def video_info(video_path):
    """
    获取视频参数
    :param video_path:
    :return:
    """
    _command = "ffmpeg -i {}"
    _command = _command.format(video_path)
    res = os.system(_command)
    return True if res == 0 else False


def convert_mp42gif(video_path, output_path, num_frames=30):
    """
    视频转gif
    :param video_path:
    :param output_path:
    :param num_frames:
    :return:
    """
    _command = "ffmpeg -i {} -vframes {} -f gif {} -y"
    _command = _command.format(video_path, num_frames, output_path)
    res = os.system(_command)
    return True if res == 0 else False
