import numpy as np
import cv2
import torch
from skimage import transform
from ..libs.basnet import BASNet
from .FaceDetector import FaceDetector

__all__ = ['ImageCrop', 'HCenter', 'VCenter']

FEATURE_DETECT_MAX_CORNERS = 50
FEATURE_DETECT_QUALITY_LEVEL = 0.1
FEATURE_DETECT_MIN_DISTANCE = 10


class HCenter:
    def __init__(self, model_name="basnet.pth", ctx_id=-1):
        self.device = torch.device("cuda:" + str(ctx_id)) if ctx_id > -1 else torch.device("cpu")
        self.net = self.load_model(model_name)

    def load_model(self, model_name):
        net = BASNet(3, 1)
        net.load_state_dict(torch.load(model_name, map_location=None if torch.cuda.is_available() else "cpu"))
        if torch.cuda.is_available():
            net.to(self.device)
        net.eval()
        return net

    @staticmethod
    def _cal_center(pred, width, height):
        w, h = pred.shape[0], pred.shape[1]
        image = pred.cpu().data.numpy()
        image = np.asarray(image * 255).astype(np.uint8)
        ret, image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)
        contours = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
        if len(contours) == 0:
            return (width - 1) / 2, (height - 1) / 2

        max_i = np.argmax([contour.size for contour in contours])
        if contours[max_i].size <= 8:
            return (width - 1) / 2, (height - 1) / 2

        M = cv2.moments(contours[max_i])
        if M["m00"] == 0.0:
            return (width - 1) / 2, (height - 1) / 2

        return (M["m10"] / M["m00"]) * (width / w), (M["m01"] / M["m00"]) * (height / h)

    @staticmethod
    def to_tensor(image):
        image = image if np.max(image) < 1e-6 else image / np.max(image)
        temp = np.zeros((image.shape[0], image.shape[1], 3))
        if len(image.shape) == 2:
            image = image.reshape(image.shape[0], image.shape[1], 1)
            temp[:, :, 0] = (image[:, :, 0] - 0.485) / 0.229
            temp[:, :, 1] = (image[:, :, 0] - 0.485) / 0.229
            temp[:, :, 2] = (image[:, :, 0] - 0.485) / 0.229
        else:
            temp[:, :, 0] = (image[:, :, 0] - 0.485) / 0.229
            temp[:, :, 1] = (image[:, :, 1] - 0.456) / 0.224
            temp[:, :, 2] = (image[:, :, 2] - 0.406) / 0.225
        temp = temp.transpose((2, 0, 1))
        return torch.from_numpy(temp)

    def predict(self, image):
        width, height = image.shape[:2][::-1]
        temp = transform.resize(image, (256, 256), mode='constant', anti_aliasing=False)
        temp = self.to_tensor(temp)
        temp = temp.type(torch.FloatTensor).unsqueeze(0)
        if torch.cuda.is_available():
            temp = temp.to(self.device)
        temp = self.net(temp).squeeze()

        return self._cal_center(temp, width, height)


class VCenter:
    def __init__(self, ctx_id=-1):
        self.net = FaceDetector(ctx_id=ctx_id)

    def _face_center(self, image):
        """
        获取图片中最大人脸的中心位置
        :param image: numpy data
        :return: center
        """
        boxes, _ = self.net.detect(image)
        if len(boxes) == 0:
            return -1, -1

        area = [(x2 - x1) * (y2 - y1) for (x1, y1, x2, y2) in boxes]
        i = np.argmax(area)
        x = (boxes[i][0] + boxes[i][2]) / 2
        y = (boxes[i][1] + boxes[i][3]) / 2

        return x, y

    @staticmethod
    def _feature_center(image):
        """
        获取图片中特征值中心加权位置
        :param image: numpy data
        :return: center
        """
        if len(image.shape) < 3:
            gray = image
        elif image.shape[-1] == 4:
            gray = cv2.cvtColor(image, cv2.COLOR_RGBA2GRAY)
        else:
            gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        corners = cv2.goodFeaturesToTrack(gray,
                                          FEATURE_DETECT_MAX_CORNERS,
                                          FEATURE_DETECT_QUALITY_LEVEL,
                                          FEATURE_DETECT_MIN_DISTANCE)

        if corners is None or len(corners) == 0:
            return -1, -1

        x, y, weight = 0, 0, 0
        for point in corners:
            weight += 1
            x += point[0][0]
            y += point[0][1]

        return x / weight, y / weight

    @staticmethod
    def to_tensor(image):
        dst = np.zeros((image.shape[0], image.shape[1], 3))
        if len(image.shape) == 2:
            temp = image.reshape(image.shape[0], image.shape[1], 1)
            dst[:, :, 0] = temp[:, :, 0]
            dst[:, :, 1] = temp[:, :, 0]
            dst[:, :, 2] = temp[:, :, 0]
        else:
            dst[:, :, 0] = image[:, :, 0]
            dst[:, :, 1] = image[:, :, 1]
            dst[:, :, 2] = image[:, :, 2]
        return dst

    def predict(self, image):
        """
        获取图片中心位置
        :param image: numpy data
        :return: center
        """
        temp = self.to_tensor(image)
        center = self._face_center(temp)
        return self._feature_center(image) if center == (-1, -1) else center


class ImageCrop:
    def __init__(self, model_name="basnet.pth", ctx_id=-1):
        """
        图像裁剪
        :param model_name: 模型路径
        :param ctx_id: 指定GPU，-1表示CPU
        """
        # 初始化HCenter模型
        self._hcenter = HCenter(model_name, ctx_id)
        # 初始化VCenter模型
        self._vcenter = VCenter(ctx_id=ctx_id)

    @staticmethod
    def _cal_size(size1, size2):
        """
        计算目标尺寸
        :param size1: 原尺寸
        :param size2: 目标尺寸
        :return: width, height, scale
        """
        w1, h1 = size1
        w2, h2 = size2
        if w1 / h1 <= w2 / h2:
            w = w1
            h = round(w1 * h2 / w2)
        else:
            h = h1
            w = round(h1 * w2 / h2)
        s = (w2 / w, h2 / h)
        return w, h, s

    @staticmethod
    def _cal_margin(size1, size2, center):
        """
        计算裁剪区域
        :param size1: 原尺寸
        :param size2: 目标尺寸
        :param center: 裁剪中心
        :return: top, down, left, right
        """
        w1, h1 = size1
        w2, h2 = size2
        x, y = center
        assert (w1 == w2 or h1 == h2)
        top, down, left, right = 0, h1 - 1, 0, w1 - 1
        if h1 == h2:
            left = max(int(round(x - (w2 - 1) / 2)), 0)
            offset = left + w2 - 1
            if offset > w1 - 1:
                left = left - (offset - (w1 - 1))
            right = left + w2 - 1
        else:
            top = max(int(round(y - (h2 - 1) / 2)), 0)
            offset = top + h2 - 1
            if offset > h1 - 1:
                top = top - (offset - (h1 - 1))
            down = top + h2 - 1
        return top, down, left, right

    def crop_margin(self, image, size):
        """
        计算图片裁剪边缘大小
        :param image: 输入图像（numpy data）
        :param size: 目标尺寸（w, h）
        :return: 输出边框（up, down, left, right）
        """
        size1 = image.shape[:2][::-1]
        width, height, scale = self._cal_size(size1, size)
        center = self._hcenter.predict(image) if height == size1[1] else self._vcenter.predict(image)

        return self._cal_margin(size1, (width, height), center)

    def crop_image(self, image, size):
        """
        图片裁剪
        :param image: 输入图像（numpy data）
        :param size: 目标尺寸（w, h）
        :return: 输出图像（numpy data）
        """
        bbox = self.crop_margin(image, size)
        dst = image[bbox[0]:bbox[1] + 1, bbox[2]:bbox[3] + 1]

        size1 = image.shape[:2][::-1]
        width, height, scale = self._cal_size(size1, size)
        _size = (int(round(width * scale[0])), int(round(height * scale[1])))
        return dst if scale == (1.0, 1.0) else cv2.resize(dst, _size)
