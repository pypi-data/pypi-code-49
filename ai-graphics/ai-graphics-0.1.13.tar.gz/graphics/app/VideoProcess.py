"""
Name : VideoProcess.py
Author  : Cash
Contact : tkggpdc2007@163.com
Time    : 2020-01-08 10:52
Desc:
"""

import os
import cv2
import numpy as np
from scenedetect.video_manager import VideoManager
from scenedetect.scene_manager import SceneManager
from scenedetect.stats_manager import StatsManager
from scenedetect.detectors import ContentDetector
from moviepy.editor import VideoFileClip, ImageSequenceClip, concatenate_videoclips
from .FontWriter import write_text
from .Graphics import alpha_compose, add_border, erase_border

__all__ = ['extract_frames',
           'batch_resize',
           'video_compose',
           'scene_frames',
           'video_clip',
           'video_caption',
           'video_border',
           'video_logo',
           'video_image',
           'video_erase',
           'video_speed',
           'video_cut']


def extract_frames(path, threshold=30.0, batch_size=32):
    """
    提取视频关键帧
    :param path: the video path
    :param threshold: the threshold of two frames`s pixel diff
    :param batch_size: batch size
    :return: a list of [images]
    """
    key_frames = []
    try:
        video_capture = cv2.VideoCapture(path)
        success, frame = video_capture.read()
        height, width = frame.shape[:2]
        key_frames.append([frame[:, :, ::-1]])

        frame_diffs, prev_frame, idx = [], None, 0
        while success:
            curr_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2LUV)
            if curr_frame is not None and prev_frame is not None:
                diff = cv2.absdiff(curr_frame, prev_frame)
                diff_sum_mean = np.sum(diff) / (width * height)
                frame_diffs.append(diff_sum_mean)
                if diff_sum_mean > threshold:
                    if len(key_frames[-1]) < batch_size:
                        key_frames[-1].append(frame[:, :, ::-1])
                    else:
                        if len(key_frames) * batch_size > 128:
                            break
                        key_frames.append([frame[:, :, ::-1]])
            idx += 1
            prev_frame = curr_frame
            success, frame = video_capture.read()
        video_capture.release()
    except ValueError:
        pass

    return key_frames


def batch_resize(images, max_size=640):
    """
    批量缩放图像
    :param images: a list of numpy data
    :param max_size: max size of width, height
    :return: a list of numpy data
    """
    try:
        if len(images) > 0 and max(images[0].shape) > max_size:
            h, w, _ = images[0].shape
            r = max_size / max(w, h)
            images = [cv2.resize(image, (int(w * r), int(h * r))) for image in images]

    except ValueError:
        pass

    return images


def video_compose(paths, output_path):
    """
    视频合成
    :param paths: the list of video path
    :param output_path: the output video path
    :return:
    """
    try:
        clips = [VideoFileClip(path) for path in paths if os.path.exists(path)]
        if len(clips) == 0:
            return

        video = concatenate_videoclips(clips)
        video.write_videofile(output_path, fps=clips[0].fps, audio_codec="aac", threads=5)

    except ValueError:
        pass

    return


def scene_frames(path):
    """
    获取视频每个镜头所在的帧数
    :param path: the video path
    :return:
    """
    video_manager = VideoManager([path])
    scene_manager = SceneManager(StatsManager())
    scene_manager.add_detector(ContentDetector())
    start_time = video_manager.get_base_timecode()

    try:
        frame_nums = video_manager._frame_length
        video_manager.set_duration(start_time=start_time, end_time=start_time + frame_nums)
        video_manager.set_downscale_factor()
        video_manager.start()

        scene_manager.detect_scenes(frame_source=video_manager)
        scene_list = scene_manager.get_scene_list(start_time)
        video_manager.release()

        return [scene[1].get_frames() - scene[0].get_frames() for scene in scene_list], frame_nums

    except ValueError:
        return []


def video_clip(path, output_dir=""):
    """
    视频镜头分割
    :param path: the video path
    :param output_dir: output fold dir
    :return:
    """
    try:
        if not os.path.exists(path):
            return
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        clip = VideoFileClip(path)
        frame_list, _ = scene_frames(path)
        frames = [frame for frame in clip.iter_frames()]

        count, fps = 0, clip.fps
        for i, frame_num in enumerate(frame_list):
            file_name = (output_dir + "/%s_%s_%s.mp4") % (i + 1, count, count + frame_num)
            audio = clip.audio.subclip(count / fps, (count + frame_num) / fps)
            video = ImageSequenceClip(frames[count:count + frame_num], fps=fps).set_audio(audio)
            video.write_videofile(file_name, fps=fps, audio_codec="aac", threads=5)
            count = count + frame_num

        audio.close()
        video.close()
        clip.close()
    except ValueError:
        pass


def video_caption(path, text, position, font_size, font_color, font_path, fps=None):
    """
    视频添加字幕
    :param path: the video path
    :param text: caption text
    :param position:
    :param font_size:
    :param font_color:
    :param font_path:
    :param fps:
    :return:
    """
    try:
        clip = VideoFileClip(path)
        frames = [write_text(frame, text, position, font_size, font_color, font_path) for frame in
                  clip.iter_frames()]
        num_frames = min(clip.reader.nframes, len(frames))
        fps = clip.fps if fps is None else fps
        audio = clip.audio.subclip(0 / fps, num_frames / fps)
        clip = ImageSequenceClip(frames, fps=fps).set_audio(audio)
        clip.write_videofile(os.path.splitext(path)[0] + '.mp4', fps=fps, audio_codec="aac", threads=5)
        audio.close()
        clip.close()
    except ValueError:
        pass


def video_border(path, border=[0, 0, 0, 0], color=(0, 0, 0)):
    """
    视频添加黑边
    :param path: the video path
    :param border: border list -> [up, down, left, right]
    :param color: color tuple -> (r, g, b)
    :return:
    """
    try:
        clip = VideoFileClip(path)
        frames = [add_border(frame, border, color) for frame in clip.iter_frames()]
        fps, num_frames = clip.fps, min(clip.reader.nframes, len(frames))
        audio = clip.audio.subclip(0 / fps, num_frames / fps)
        clip = ImageSequenceClip(frames, fps=fps).set_audio(audio)
        clip.write_videofile(os.path.splitext(path)[0] + '.mp4', fps=fps, audio_codec="aac", threads=5)
        audio.close()
        clip.close()
    except ValueError:
        pass


def video_logo(path, src, x, y):
    """
    视频添加LOGO
    :param path: the video path
    :param src: the logo image
    :param x: col
    :param y: row
    :return:
    """
    try:
        clip = VideoFileClip(path)
        frames = [alpha_compose(frame, src, x, y) for frame in clip.iter_frames()]
        fps, num_frames = clip.fps, min(clip.reader.nframes, len(frames))
        audio = clip.audio.subclip(0 / fps, num_frames / fps)
        clip = ImageSequenceClip(frames, fps=fps).set_audio(audio)
        clip.write_videofile(os.path.splitext(path)[0] + '.mp4', fps=fps, audio_codec="aac", threads=5)
        audio.close()
        clip.close()
    except ValueError:
        pass


def video_image(path, output_dir=""):
    """
    视频保存图片
    :param path: the video path
    :param output_dir: output fold dir
    :return:
    """
    try:
        if not os.path.exists(path):
            return
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        clip = VideoFileClip(path, has_mask=True, audio=False)
        for i, (frame, alpha) in enumerate(zip(clip.iter_frames(), clip.mask.iter_frames())):
            frame = np.dstack((frame, (alpha * 255).astype('uint8')))
            file_name = (output_dir + "/%s.png") % i
            cv2.imwrite(file_name, cv2.cvtColor(np.asarray(frame), cv2.COLOR_RGBA2BGRA))
        clip.close()
    except ValueError:
        pass


def video_erase(path, border=[0, 0, 0, 0], color=(0, 0, 0), fps=None):
    """
    视频擦除边框
    :param path: the video path
    :param border: border list -> [up, down, left, right]
    :param color: color tuple -> (r, g, b)
    :param fps:
    :return:
    """
    try:
        clip = VideoFileClip(path)
        fps, num_frames = clip.fps if fps is None else fps, clip.reader.nframes
        if num_frames > 2000:
            frames = []
            for i, frame in enumerate(clip.iter_frames()):
                file_name = "%s.jpg" % i
                frame = erase_border(frame, border, color)
                cv2.imwrite(file_name, cv2.cvtColor(np.array(frame), cv2.COLOR_RGB2BGR))
                frames.append(file_name)
        else:
            frames = [erase_border(frame, border, color) for frame in clip.iter_frames()]

        num_frames = min(clip.reader.nframes, len(frames))
        audio = clip.audio.subclip(0 / fps, num_frames / fps)
        clip = ImageSequenceClip(frames, fps=fps).set_audio(audio)
        clip.write_videofile(os.path.splitext(path)[0] + '.mp4', fps=fps, audio_codec="aac", threads=5)
        audio.close()
        clip.close()
    except ValueError:
        pass


def video_speed(path, fps):
    """
    视频变速
    :param path: the video path
    :param fps:
    :return:
    """
    try:
        if not os.path.exists(path):
            return

        clip = VideoFileClip(path, has_mask=True)
        frames = [frame for frame in clip.iter_frames()]
        num_frames = min(clip.reader.nframes, len(frames))
        audio = clip.audio.subclip(0 / fps, num_frames / fps)
        clip = ImageSequenceClip(frames, fps=fps).set_audio(clip.audio)
        clip.write_videofile(os.path.splitext(path)[0] + '.mp4', fps=fps, audio_codec="aac", threads=5)
        audio.close()
        clip.close()
    except ValueError:
        pass


def video_cut(path, start, end):
    """
    视频裁掉片段
    :param path: the video path
    :param start: first frame to cut
    :param end: last frame to cut
    :return:
    """
    try:
        if not os.path.exists(path):
            return

        clip = VideoFileClip(path, has_mask=True)
        frames = [frame for frame in clip.iter_frames()]
        fps, num_frames = clip.fps, min(clip.reader.nframes, len(frames))
        if start < 0 or end > num_frames - 1 or end < start:
            return
        video = []
        if start > 0:
            audio = clip.audio.subclip(0 / fps, start / fps)
            temp = ImageSequenceClip(frames[0:start], fps=fps).set_audio(audio)
            video.append(temp)
        if end < num_frames - 1:
            audio = clip.audio.subclip((end + 1) / fps, num_frames / fps)
            temp = ImageSequenceClip(frames[(end + 1):num_frames], fps=fps).set_audio(audio)
            video.append(temp)

        if len(video) == 0:
            return
        clip = concatenate_videoclips(video)
        clip.write_videofile(os.path.splitext(path)[0] + '.mp4', fps=fps, audio_codec="aac", threads=5)

        for v in video:
            v.close()

        audio.close()
        temp.close()
        clip.close()
    except ValueError:
        pass
