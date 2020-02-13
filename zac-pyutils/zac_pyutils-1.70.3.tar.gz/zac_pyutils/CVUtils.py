# author: zac
# create-time: 2019-10-28 16:54
# usage: -
import sys
import urllib.request
import numpy as np
from io import BytesIO
import importlib
from PIL import Image
from sklearn.cluster import MiniBatchKMeans
import logging
import os
logging.disable(logging.WARNING)

def _get_module(name):
    # return sys.modules.get(name, default=__import__(name))
    return sys.modules.get(name, importlib.import_module(name))


def _is_url(inp_str):
    return inp_str.startswith("http://") or inp_str.startswith("https://")


def cos_sim(arr1, arr2):
    return np.dot(arr1, arr2) / (np.linalg.norm(arr1) * np.linalg.norm(arr2))


def cos_sim_nested(hist1, hist2, weight=None):
    if weight is None:
        weight = [1] * hist1.shape[0]
    sim_list = [cos_sim(hist1[i, :], hist2[i, :]) * weight[i] for i in range(hist1.shape[0])]
    return sum(sim_list) / len(sim_list)

class Load:
    @staticmethod
    def image_by_cv2_from(img_path: str):
        """
        automatic discern input between url and local-file
        default format is [BGR].
        return None if load url request failed
        """
        cv2 = _get_module("cv2")
        if _is_url(img_path):
            # load from url
            if ".webp" in img_path:
                assert False, "at 2019-10-28, cv2 does not support webp (it's a python-opencv binding bug)  " \
                              "refer to this: https://github.com/opencv/opencv/issues/14978\n\n" \
                              "*********** use Loader.load_image_by_pil_from() **********"
            try:
                url_response = urllib.request.urlopen(img_path)
                img_array = np.array(bytearray(url_response.read()), dtype=np.uint8)
                img = cv2.imdecode(img_array, -1)
                return img
            except Exception as e:
                print("load img from url failed: " + str(e))
                return None
        else:
            # load from file
            return cv2.imread(img_path)

    @staticmethod
    def image_by_pil_from(img_path: str):
        """
        automatic discern input between url and local-file
        default format is [RGB].
        return None if load url request failed
        """
        if _is_url(img_path):
            # load from url
            try:
                url_response = urllib.request.urlopen(img_path)
                image = Image.open(BytesIO(url_response.read()))
                return image
            except Exception as e:
                print("[ERROR] load img from url failed: " + str(e))
                return None
        else:
            # load from file
            return Image.open(img_path)

    @staticmethod
    def image_by_caffe_from_fp(img_path: str):
        if _is_url(img_path):
            assert False, "caffe only support load from local file"
        caffe = _get_module("caffe")
        return [caffe.io.load_image(img_path)]


class Convert:
    @staticmethod
    def pre_cv2caffe(img_inp):
        cv2 = _get_module("cv2")
        img = cv2.cvtColor(img_inp, cv2.COLOR_BGR2RGB) / 255.0
        return [img]

    @staticmethod
    def pre_cv2Image(img_inp):
        cv2 = _get_module("cv2")
        img = cv2.cvtColor(img_inp, cv2.COLOR_BGR2RGB)
        return Image.fromarray(img)


class PlotHist:
    @staticmethod
    def plot_hist_from_pil_image(img_inp):
        assert img_inp.mode == 'RGB', "only support rgb"
        plt = _get_module("matplotlib.pyplot")
        color_map = ['r', 'g', 'b']
        for idx, each_hist in enumerate(np.reshape(img_inp.histogram(), (3, 256))):
            # plt.subplot(2,2,idx+1)
            plt.plot(each_hist / sum(each_hist), color=color_map[idx])
            plt.xlim([0, 256])
        plt.show()

    @staticmethod
    def plot_hist_from_cv2_image(img_inp):
        plt = _get_module("matplotlib.pyplot")
        img_rgb = Image.fromarray(img_inp)
        color_map = ['r', 'g', 'b']
        for idx, each_hist in enumerate(np.reshape(img_rgb.histogram(), (3, 256))):
            # plt.subplot(2,2,idx+1)
            plt.plot(each_hist / sum(each_hist), color=color_map[idx])
            plt.xlim([0, 256])
        plt.show()

    @staticmethod
    def plot_hist_from_arr_image(img_inp):
        return PlotHist.plot_hist_from_cv2_image(img_inp)

    @staticmethod
    def plot_hist_crops(hist_inp, crops_inp, color_map=None, dont_show=None):
        plt = _get_module("matplotlib.pyplot")
        GRAY_MODE = ['F', 'L']
        default_color_map = {
            "RGB": ['r', 'g', 'b'],
            "YCbCr": ['r', 'black', 'b'],
            "F": ['black'],
            "L": ['black'],
        }
        row, col = crops_inp.shape
        crops_inp_img = np.concatenate(crops_inp, axis=0)
        mode = crops_inp_img[0].mode
        if mode == 'RGB':
            print("not recommend RGB for similarity, try YCbCr")
        is_gray = mode in GRAY_MODE

        if dont_show is None:
            dont_show = []

        if color_map is None:
            try:
                color_map = default_color_map[mode]
            except Exception:
                print("can't auto define color_map. must feed this param")

        fig = plt.figure(figsize=(10, 10))
        fig.set_tight_layout(True)
        for idx, (crop_hist, crop_img) in enumerate(zip(hist_inp, crops_inp_img)):
            fig.add_subplot(row, 2 * col, 2 * idx + 1)
            plt.title("hist_{}".format(mode))
            for idx_, i in enumerate(crop_hist):
                if color_map[idx_] in dont_show:
                    continue
                plt.plot(i, color=color_map[idx_])
                plt.xlim([0, crop_hist.shape[-1]])  # 手工设置x轴的最大值（默认用数据里的最大值）
                plt.ylim([0, 1])
            fig.add_subplot(row, 2 * col, 2 * idx + 2)
            plt.title("RGB_{}".format(idx))
            plt.axis('off')
            plt.tight_layout(h_pad=1, w_pad=0.2)
            if is_gray:
                plt.imshow(crop_img, cmap='gray')
            else:
                plt.imshow(crop_img.convert("RGB"), cmap='viridis')
        return fig


class StandardCV:
    @staticmethod
    def custom_cut_to_matrix(imgPIL, row, col):
        # 0 1 2
        # 3 4 5
        # 6 7 8
        #    col0       col1       col2       col3
        # (  0,  0)  (1/3,  0)  (2/3,  0)  (3/3,  0)   row0
        # (  0,1/3)  (1/3,1/3)  (2/3,1/3)  (3/3,1/3)   row1
        # (  0,2/3)  (1/3,2/3)  (2/3,2/3)  (3/3,2/3)   row2
        # (  0,3/3)  (1/3,3/3)  (2/3,3/3)  (3/3,3/3)   row3
        crop_matrix = []
        base_w, base_h = imgPIL.size[0] // col, imgPIL.size[1] // row
        for r in range(row):
            crop_one_row = []
            for c in range(col):
                anchor_lt = (base_w * c, base_h * r)  # 左上角的anchor
                anchor_rb = (base_w * (c + 1), base_h * (r + 1))  # 右下角的anchor
                crop_one_row.append(imgPIL.crop((anchor_lt[0], anchor_lt[1], anchor_rb[0], anchor_rb[1])))
            crop_matrix.append(crop_one_row)
        return np.array(crop_matrix, dtype='object')

    @staticmethod
    def get_hist(imgPIL, row=1, col=1, bins=None, weights=None, return_crops=False):
        """
        输入要求是PIL的image
        根据 row,col 会切分图像，最后返回时 all_crops 的size是(row, col, img_w, img_h, img_channel)
        各区域单独计算hist然后拼接到一起
        :param bins: 设定各个通道的bins个数，默认[32]*3。如果不是一样大的会padding到和max一样大
                     例如R通道4个bins: [16,16,16,32]，G通道2个bins：[32,48]，G会padding为[32,48,0,0]
        :param weights: 各个区域hist权重，默认都为1
        """
        if bins is None:
            bins = [32] * 3
        if weights is None:
            weights = [1.0] * row * col
        is_gray = len(np.array(imgPIL).shape) == 2
        # 切块
        all_crops = StandardCV.custom_cut_to_matrix(imgPIL, row, col)  # come with row x col
        all_crops_flatten = np.concatenate(all_crops, axis=0)  # flattent to (16, 128, 128, 3)

        hist_features = []
        for cropIdx, cropPIL in enumerate(all_crops_flatten):
            cropArr = np.array(cropPIL)
            # np.array(crop).shape[-1] 取通道数
            # np.histogram 返回结果两个， hist, bins_edge —— 直方图和bin的方位
            if is_gray:
                # 灰度图的hist为了方便后面统一使用，也在外面包上一个维度
                hist_of_all_channel = [np.histogram(cropArr, bins=bins[0], range=[0, 256])[0]]
            else:
                hist_of_all_channel = [np.histogram(cropArr[:, :, c], bins=bins[c], range=[0, 256])[0] for c in range(cropArr.shape[-1])]
            # normalize
            hist_of_all_channel = [hist / sum(hist) for hist in hist_of_all_channel]
            # 不同通道bins可能有不同，末尾padding到相同
            # 例如R通道4个bins: [16,16,16,32]，G通道2个bins：[32,48]，G会padding为[32,48,0,0]
            max_bin = max(bins)
            hist_of_all_channel = [np.pad(hist, (0, max_bin - bins[idx]), 'constant') for idx, hist in enumerate(hist_of_all_channel)]
            # 此区域三通道的hist都乘上权重
            hist_of_all_channel = [i * weights[cropIdx] for i in hist_of_all_channel]
            hist_features.append(np.stack(hist_of_all_channel, axis=0))

        hist_features = np.stack(hist_features, axis=0)  # [row*col, 3, bins]
        if return_crops:
            return hist_features, all_crops
        else:
            return hist_features

    @staticmethod
    def get_lbp_imgPIL(imgPIL, R=1, P=None):
        local_binary_pattern = _get_module("skimage.feature").local_binary_pattern
        if P is None:
            P = 8 * R
        return Image.fromarray(np.array(local_binary_pattern(np.array(imgPIL.convert("L")), P=P, R=R)))


class Vectorize:
    class VectorFromNN:
        import tensorflow as tf
        import tensorflow_hub as hub
        class _BasePattern:
            default_model = None
            url = None
            IMAGE_SHAPE = (224, 224)  # 大部分都适用224x224

            # 如果有特殊情况子类自行重写此方法
            def get_default_model(self):
                if self.default_model is None:
                    self.default_model = tf.keras.Sequential([hub.KerasLayer(self.url, trainable=False)])
                return self.default_model

            # 如果有特殊情况子类自行重写此方法
            def pre_format_pilImage(self, imgPIL):
                return np.array(imgPIL.resize(self.IMAGE_SHAPE)) / 255.0

            # fundamental function
            def imgArr2vec_batch(self, imgArr_batch, model=None):
                if model is None:
                    model = self.get_default_model()
                return model.predict(imgArr_batch)

            # ->imgArr2vec->imgArr2vec_batch
            def imgPIL2vec(self, imgPIL, model=None):
                imgArr = self.pre_format_pilImage(imgPIL)
                return self.imgArr2vec(imgArr, model=model)

            # ->imgArr2vec_batch
            def imgPIL2vec_batch(self, imgPIL_batch, model=None):
                imgArr_batch = np.array([self.pre_format_pilImage(imgPIL) for imgPIL in imgPIL_batch])
                return self.imgArr2vec_batch(imgArr_batch, model=model)

            # ->imgArr2vec_batch
            def imgArr2vec(self, imgArr, model=None):
                return self.imgArr2vec_batch(imgArr[np.newaxis, :], model=model)[0]

        class InceptionV3(_BasePattern):
            url = "https://tfhub.dev/google/imagenet/inception_v3/feature_vector/4"
            IMAGE_SHAPE = (299, 299)

        class InceptionV1(_BasePattern):
            url = "https://tfhub.dev/google/imagenet/inception_v1/feature_vector/4"

        class InceptionResNet(_BasePattern):
            url = "https://tfhub.dev/google/imagenet/inception_resnet_v2/feature_vector/4"
            IMAGE_SHAPE = (299, 299)

    class VectorFromHist:
        class ColorHist:
            def __init__(self, crop_shape=(4, 4), bins=None, p_weight=None):
                if bins is None:
                    self.bins = [32, 64, 32]
                if p_weight is None:
                    if crop_shape == (4, 4):
                        self.p_weight = np.array([[1., 1., 1., 1.],
                                             [1., 1.2, 1.2, 1.],
                                             [1., 1.2, 1.2, 1.],
                                             [1., 1., 1., 1.]])
                    else:
                        self.p_weight = np.ones(crop_shape)
                self.crop_shape = crop_shape
                assert self.crop_shape == self.p_weight.shape, f"切割shape为 {crop_shape}, 权重shape为 {p_weight.shape}, 二者必须一致"

            def imgPIL_to_Vec(self, imgPIL):
                """
                hist的结果reshape，将3通道的各个bins都合到一起，整体向量实际是一个nested的结果，shape=[row*col,3*bins]
                目的是为了后面各区域的相似度取均值，这样的效果比所有子区域hist直接flatten成一个大向量要好
                """
                hist_features = StandardCV.get_hist(imgPIL, row=self.crop_shape[0], col=self.crop_shape[1], bins=self.bins,
                                                    weights=self.p_weight.flatten(), return_crops=False)
                return hist_features.reshape(self.crop_shape[0]*self.crop_shape[1], -1)

            def imgPIL2Vec(self, imgPIL):
                return self.imgPIL_to_Vec(imgPIL)

        class LBPHist:
            def __init__(self, crop_shape=(4, 4), bins=None, p_weight=None, lbp_R=1, lbp_P=None):
                if bins is None:
                    self.bins = [32]
                if p_weight is None:
                    if crop_shape == (4, 4):
                        self.p_weight = np.array([[1., 1., 1., 1.],
                                                  [1., 1.2, 1.2, 1.],
                                                  [1., 1.2, 1.2, 1.],
                                                  [1., 1., 1., 1.]])
                    else:
                        self.p_weight = np.ones(crop_shape)
                self.crop_shape = crop_shape
                assert self.crop_shape == self.p_weight.shape
                self.local_binary_pattern = _get_module("skimage.feature").local_binary_pattern
                self.lbp_R = lbp_R
                self.lbp_P = 8 * lbp_R if lbp_P is None else lbp_P

            def imgPIL_to_Vec(self, imgPIL):
                imgLBP = StandardCV.get_lbp_imgPIL(imgPIL, self.lbp_R, self.lbp_P)
                hist_features = StandardCV.get_hist(imgLBP, row=self.crop_shape[0], col=self.crop_shape[1], bins=self.bins,
                                                    weights=self.p_weight.flatten(), return_crops=False)
                return hist_features.reshape(self.crop_shape[0] * self.crop_shape[1], -1)

            def imgPIL2Vec(self, imgPIL):
                return self.imgPIL_to_Vec(imgPIL)

    class VectorFromThemeColor:
        class KMeansColor:
            def __init__(self, cluster=5):
                self.km = MiniBatchKMeans(n_clusters=cluster)

            def imgPIL2Vec(self, imgPIL):
                img_arr = np.array(imgPIL)
                return self.imgArr2Vec(img_arr)

            def imgArr2Vec(self, imgArr):
                h, w, c = imgArr.shape
                pixel = np.reshape(imgArr, (h*w, c))
                self.km.fit(pixel)
                return self.km.cluster_centers_


class ImageGenerator:
    allow_type = ['.jpg', '.png']
    MODE_CATEGORICAL = 'categorical'
    MODE_SPARSE = 'sparse'

    def __init__(self, rescale=1 / 255.0):
        self.rescale = rescale

    def process_img_pil(self, imgPIL):
        # 暂时只有rescale到0，1
        return np.array(imgPIL) * self.rescale

    def flow_from_directory(self, root_path, classes=None, image_shape=None, batch_size=10, class_mode=None, verbose=True):
        if class_mode is None:
            class_mode = self.MODE_CATEGORICAL
        if image_shape is None:
            image_shape = (224, 224)
        if classes is None:
            find_classes = [os.path.join(root_path, i) for i in os.listdir(root_path) if not i.startswith(".")]
        else:
            find_classes = [os.path.join(root_path, i) for i in os.listdir(root_path) if not i.startswith(".") and i in classes]

        if class_mode == self.MODE_CATEGORICAL:
            one_hot = [0] * len(find_classes)
            class_dict = {}
            for idx, class_ in enumerate(find_classes):
                one_hot_ = one_hot.copy()
                one_hot_[idx] = 1
                class_dict.update({class_: one_hot_})
        elif class_mode == self.MODE_SPARSE:
            class_dict = {class_: idx for idx, class_ in enumerate(find_classes)}
        else:
            assert False, f"class_mode should be supplied (currently is '{class_mode}'')"

        allow_files = [(class_dir, filename) for class_dir in find_classes for filename in os.listdir(class_dir) if
                       os.path.splitext(filename)[-1] in self.allow_type]
        fp_list = [(os.path.join(root_path, class_dir, filename), class_dict[class_dir]) for (class_dir, filename) in allow_files]
        if verbose:
            print(f"Found {len(fp_list)} images belonging to {len(class_dict)} classes")
            for k, v in class_dict.items():
                print(v, len([cla for fp, cla in fp_list if cla == v]), k)

        for i in range(0, len(fp_list), batch_size):
            img_cla_batch = [(self.process_img_pil(Image.open(fp).resize(image_shape)), cla) for fp, cla in fp_list[i:i + batch_size]]
            img_cla_batch = np.array(img_cla_batch)
            yield np.stack(img_cla_batch[:, 0]), img_cla_batch[:, 1]

if __name__ == '__main__':
    # 验证切图是否正常 | plt绘图耗时会比较久
    def test_case0():
        print(">>> 验证切图是否正常")
        cropsPIL_matrix = StandardCV.custom_cut_to_matrix(test_img, row=4, col=4)
        for i in range(cropsPIL_matrix.shape[0]):
            for j in range(cropsPIL_matrix.shape[1]):
                plt.subplot(4, 4, i * 4 + (j + 1))
                plt.imshow(cropsPIL_matrix[i, j])

        print(">>> 展示切割后各部分的直方图")
        hist, crops = StandardCV.get_hist(test_img, row=4, col=4, return_crops=True)
        PlotHist.plot_hist_crops(hist, crops)
        plt.show()

    # 验证直方图方式相似度量
    def test_case1():
        print(">>> 验证StandardCV的直方图方式相似度量")
        transformer = Vectorize.VectorFromHist.ColorHist()
        transformer_lbp = Vectorize.VectorFromHist.LBPHist()
        print("多个子区域的直方图独立计算cos_sim然后取平均: {:.4f}".format(cos_sim_nested(transformer.imgPIL_to_Vec(test_img), transformer.imgPIL_to_Vec(test_img2))))
        print("多个子区域的LBP直方图独立计算cos_sim然后取平均: {:.4f}".format(cos_sim_nested(transformer_lbp.imgPIL_to_Vec(test_img), transformer_lbp.imgPIL_to_Vec(test_img2))))

    # 验证NN相似向量
    def test_case2():
        print(">>> 验证NN相似向量")
        transformer = Vectorize.VectorFromNN.InceptionV3()
        vec1 = transformer.imgPIL2vec(test_img)
        vec2 = transformer.imgPIL2vec(test_img2)
        print("NN取最后一层计算cos_sim: {:.4f}".format(cos_sim(vec1, vec2)))
        print(f"    向量一: {vec1.shape} {type(vec1)}\n", vec1)
        print(f"    向量二: {vec2.shape} {type(vec2)}\n", vec2)

    # 验证图片generator是否正常
    def test_case3():
        root_path = "/Users/zac/Downloads/Image_samples"
        g = ImageGenerator()
        img_generator = g.flow_from_directory(root_path, classes=['cg_background', 'landscape'])
        for image_batch, label_batch in img_generator:
            print("Image batch shape: ", image_batch.shape)
            print("Label batch shape: ", label_batch.shape)
            break

    import matplotlib.pyplot as plt

    test_url = "http://www.kedo.gov.cn/upload/resources/image/2017/04/24/150703.png"
    test_url2 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcThwIfzyp-Rv5zYM0fwPmoM5k1f9eW3ETYuPcL8j2I0TuG0tdb5&s"
    test_img = Load.image_by_pil_from(test_url).convert("YCbCr")
    test_img2 = Load.image_by_pil_from(test_url2).convert("YCbCr")
    test_img.show()
    test_img2.show()

    # test_case0()
    # test_case1()
    # test_case2()
    test_case3()
