from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from .utils import *
from ..backend.common import floatx
from .data_provider import *
from .dataset import *

try:
    from urllib.request import urlretrieve
except ImportError:
    from six.moves.urllib.request import urlretrieve

_session = get_session()
_trident_dir = os.path.join(get_trident_dir(), 'datasets')
_backend = _session.backend

if 'TRIDENT_BACKEND' in os.environ:
    _backend = os.environ['TRIDENT_BACKEND']

if not os.path.exists(_trident_dir):
    try:
        os.makedirs(_trident_dir)
    except OSError:
        # Except permission denied and potential race conditions
        # in multi-threaded environments.
        pass


def to_onehot(arr):
    if isinstance(arr, list):
        arr = np.array(arr)
    elif not isinstance(arr, np.ndarray):
        raise ValueError('You should input a list of integer or ndarray.')
    items = np.unique(arr)
    items = np.argsort(items)
    if np.min(items) < 0:
        raise ValueError('Negative value cannot convert to onhot.')
    elif np.sum(np.abs(np.round(arr) - arr)) > 0:
        raise ValueError('Only integer value can convert to onhot.')
    else:
        max_value = int(np.max(items))

        output_shape = list(arr.shape)
        output_shape.append(max_value + 1)
        output = np.zeros(output_shape, dtype=floatx())
        arr = arr.astype(np.uint8)
        for i in range(max_value):
            onehot = np.zeros(max_value + 1, dtype=floatx())
            onehot[i] = 1
            output[arr == i] = onehot
        return output


#
# def download_image(image, temproot, imageroot, flog=None):
#     # Check existing file.
#     try:
#         temppath, imagepath = (os.path.join(root, image['path']) for root in (temproot, imageroot))
#
#     except Exception as e:
#         sys.stderr('Unexpected exception before attempting download of image {0}.'.format(e))
#
#
#     # GET and save to temp location.
#     try:
#         r = requests.get(image['url'])
#         if r.status_code == 200:
#             ensure_parent_dir(temppath)
#             with open(temppath, 'wb') as fout:
#                 for chunk in r.iter_content(1024): fout.write(chunk)
#             logmsg('Saved  {}.'.format(temppath), flog=flog)
#         else:
#             logmsg('Status code {} when requesting {}.'.format(r.status_code, image['url']))
#             return DownloadResult.DOWNLOAD_FAILED
#     except Exception as e:
#         stderr('Unexpected exception when downloading image {!r}.'.format(image), e, flog=flog)
#         return DownloadResult.DOWNLOAD_FAILED
#     # Check contents.
#     try:
#         if check_image(image, temppath):
#             stderr('Image contents look good.)
#         else:
#             stderr('Image contents are wrong.')
#             return DownloadResult.MD5_FAILED
#     except Exception as e:
#         stderr('Unexpected exception when checking file contents for image {!r}.'.format(image), e)
#         return DownloadResult.MYSTERY_FAILED
#     # Move image to final location.
#     try:
#         ensure_parent_dir(imagepath)
#         os.rename(temppath, imagepath)
#     except Exception as e:
#         stderr('Unexpected exception when moving file from {} to {} for image {!r}.'.format(temppath, imagepath,
#         image), e, flog=flog)
#         return DownloadResult.MYSTERY_FAILED
#     return DownloadResult.NEW_OK


def load_mnist(dataset_name='mnist', **kwargs):
    dataset_name = dataset_name.strip().lower().replace('minist', 'mnist')

    if dataset_name.lower() not in ['mnist', 'fashion-mnist']:
        raise ValueError('Only mnist or fashion-mnist are valid  dataset_name.')

    base = 'http://yann.lecun.com/exdb/mnist/'
    if dataset_name == 'fashion-mnist':
        base = 'http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/'

    dirname = os.path.join(_trident_dir, dataset_name)
    if not os.path.exists(dirname):
        try:
            os.makedirs(dirname)
        except OSError:
            # Except permission denied and potential race conditions
            # in multi-threaded environments.
            pass

    """Load MNIST data from `path`"""
    trainData = None
    testData = None
    for kind in ['train', 'test']:
        labels_file = '{0}-labels-idx1-ubyte.gz'.format('t10k' if dataset_name in ('mnist','fashion-mnist') and kind == 'test' else kind)
        images_file = '{0}-images-idx3-ubyte.gz'.format('t10k' if dataset_name in ('mnist','fashion-mnist') and kind == 'test' else kind)
        # if dataset_name == 'emnist' :
        #     labels_file='emnist-balanced-'+labels_file
        #     images_file = 'emnist-balanced-' + images_file

        download_file(base + labels_file, dirname, labels_file, dataset_name + '_labels_{0}'.format(kind))
        download_file(base + images_file, dirname, images_file, dataset_name + '_images_{0}'.format(kind))
        labels_path = os.path.join(dirname, labels_file)
        images_path = os.path.join(dirname, images_file)
        labeldata = None
        imagedata = None
        with gzip.open(labels_path, 'rb') as lbpath:
            labels = np.frombuffer(lbpath.read(), dtype=np.uint8, offset=8)
            labels = np.squeeze(labels).astype(np.int64)
            labeldata = LabelDataset(labels.tolist())

        with gzip.open(images_path, 'rb') as imgpath:
            images = np.frombuffer(imgpath.read(), dtype=np.uint8, offset=16)
            images = np.reshape(images, (len(labels), 784)).astype(dtype=_session.floatx)
            images = np.reshape(images, (-1, 28, 28))
            imagedata = ImageDataset(images, expect_image_type=ExpectImageType.gray,
                                     get_image_mode=GetImageMode.processed)

        if kind == 'train':
            trainData = IterableDataset(data=imagedata, label=labeldata)
        else:
            testData = IterableDataset(data=imagedata, label=labeldata)

    dataset = DataProviderV2(dataset_name, traindata=trainData, testdata=testData)

    dataset.binding_class_names(
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] if dataset_name == 'mnist' else ['T-shirt/top', 'Trouser', 'Pullover', 'Dress',
                                                                        'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag',
                                                                        'Ankle boot'], 'en-US')

    return dataset


def load_cifar(dataset_name='cifar10'):
    dataset_name = dataset_name.strip().lower().replace(' ', '')

    if dataset_name.lower() not in ['cifar10', 'cifar100']:
        raise ValueError('Only cifar10 or cifar100 are valid  dataset_name.')
    baseURL = 'https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz'
    if dataset_name == 'cifar100':
        baseURL = 'https://www.cs.toronto.edu/~kriz/cifar-100-python.tar.gz'

    dirname = os.path.join(_trident_dir, dataset_name.strip())
    if not os.path.exists(dirname):
        try:
            os.makedirs(dirname)
        except OSError:
            # Except permission denied and potential race conditions
            # in multi-threaded environments.
            pass

    """Load CIFAR data from `path`"""

    download_file(baseURL, dirname, baseURL.split('/')[-1].strip(), dataset_name)
    file_path = os.path.join(dirname, baseURL.split('/')[-1].strip())
    if '.tar' in file_path:
        extract_archive(file_path, dirname, archive_format='tar')
    extract_path = os.path.join(dirname, baseURL.split('/')[-1].strip().split('.')[0])
    filelist = [f for f in os.listdir(extract_path) if os.path.isfile(os.path.join(extract_path, f))]

    data, labels = open_pickle(os.path.join(extract_path, 'train'), 'data', 'fine_labels')
    testdata, testlabels = open_pickle(os.path.join(extract_path, 'test'), 'data', 'fine_labels')
    data = data.reshape(data.shape[0], 32, 32,3).astype(_session.floatx)
    testlabels = testlabels.reshape(testlabels.shape[0], 32, 32, 3).astype(_session.floatx)
    labels = np.squeeze(labels).astype(np.int64)
    testlabels = np.squeeze(testlabels).astype(np.int64)

    trainData = IterableDataset(data=ImageDataset(data.tolist()), label=LabelDataset(labels.tolist()))
    testData = IterableDataset(data=ImageDataset(testdata.tolist()),  label=LabelDataset(testlabels.tolist()))
    dataset = DataProviderV2(dataset_name, traindata=trainData, testdata=testData)
    dataset.binding_class_names(['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship',
                                 'truck'] if dataset_name == 'cifar10' else [], 'en-US')
    return dataset


def load_birdsnap(dataset_name='birdsnap', kind='train', is_flatten=None, is_onehot=None):
    dataset_name = dataset_name.strip().lower().replace(' ', '')

    if dataset_name.lower() not in ['birdsnap']:
        raise ValueError('Only _birdsnap are valid  dataset_name.')

    if _backend in ['tensorflow', 'cntk'] and is_onehot is None:
        is_onehot = True

    baseURL = 'http://thomasberg.org/datasets/birdsnap/1.1/birdsnap.tgz'
    dirname = os.path.join(_trident_dir, dataset_name.strip())
    if not os.path.exists(dirname):
        try:
            os.makedirs(dirname)
        except OSError:
            # Except permission denied and potential race conditions
            # in multi-threaded environments.
            pass

    """Load BirdSnap data from `path`"""
    download_file(baseURL, dirname, baseURL.split('/')[-1].strip(), dataset_name)
    file_path = os.path.join(dirname, baseURL.split('/')[-1].strip())
    if '.tar' in file_path:
        extract_archive(file_path, dirname, archive_format='tar')
    else:
        extract_archive(file_path, dirname, archive_format='auto')
    extract_path = os.path.join(dirname, baseURL.split('/')[-1].strip().split('.')[0])
    pid = subprocess.Popen([sys.executable, os.path.join(extract_path, "get_birdsnap.py")], stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE, stdin=subprocess.PIPE)  # call subprocess

    filelist = [f for f in os.listdir(extract_path) if os.path.isfile(os.path.join(extract_path, f))]
    #
    #
    # images = np.frombuffer(imgpath.read(), dtype=np.uint8, offset=16).reshape(len(labels), 784).astype(
    #     dtype=floatx())
    # if is_flatten == False:
    #     images = np.reshape(images, (-1, 28, 28))
    #
    #
    # labels = np.frombuffer(os.path.join(extract_path,'species.txt'), dtype=np.uint8, offset=8).astype(dtype=floatx())
    # if _backend == 'pytorch':
    #     labels = np.squeeze(labels).astype(np.int64)
    # if is_onehot == True:
    #     if _backend == 'pytorch':
    #         warnings.warn('Pytorch not prefer onehot label, are you still want onehot label?',
    #                       category='data loading', stacklevel=1, source='load_mnist')
    #     labels = to_onehot(labels)
    images = []
    labels = []
    return (images, labels)


def load_text(filname, delimiter=',', skiprows=0, label_index=None, is_onehot=None, shuffle=True):
    if _backend in ['tensorflow', 'cntk'] and is_onehot is None:
        is_onehot = True
    arr = np.genfromtxt(filname, delimiter=delimiter, skip_header=skiprows, dtype=floatx(), filling_values=0,
                        autostrip=True)
    data, labels = None, None
    if label_index is None:
        data = arr
    else:
        if label_index == 0:
            data, labels = arr[:, 1:], arr[:, 0:1]
        elif label_index == -1 or label_index == len(arr) - 1:
            data, labels = arr[:, :-1], arr[:, -1:]
        else:
            rdata, labels = np.concatenate([arr[:, :label_index], arr[:, label_index + 1:]], axis=0), arr[:,
                                                                                                      label_index:label_index + 1]
    labels = np.squeeze(labels)
    if _backend == 'pytorch':
        labels = np.squeeze(labels).astype(np.int64)
    if is_onehot == True:
        if _backend == 'pytorch':
            warnings.warn('Pytorch not prefer onehot label, are you still want onehot label?', category='data loading',
                          stacklevel=1, source='load_text')
        labels = to_onehot(labels)
    idxes = np.arange(len(data))
    dataset = DataProvider(filname.split('/')[-1].strip().split('.')[0], data=data, labels=labels, scenario='train')

    return dataset


def load_folder_images(dataset_name='', base_folder=None, shuffle=True, folder_as_label=True,
                       expect_image_type=ExpectImageType.rgb):
    if base_folder is not None and os.path.exists(base_folder):
        if base_folder[-1] in ['\\', '/']:
            base_folder = base_folder[:-1]
        if folder_as_label == True:
            sub_folders = glob.glob(base_folder + '/*/')
            class_names = []
            if len(sub_folders) == 0:
                raise ValueError('No subfolder in base folder.')
            else:
                class_names = [os.path.normpath(folder).split('\\')[-1] for folder in sub_folders]
                class_names = list(sorted(set(class_names)))
            labels = []
            imgs = []
            for i in range(len(class_names)):
                class_name = class_names[i]
                class_imgs = glob.glob(base_folder + '/{0}/*.*g'.format(class_name))
                labels.extend((np.ones(len(class_imgs)) * i).astype(np.int64).tolist())
                imgs.extend(class_imgs)

            imagedata = ImageDataset(imgs, expect_image_type=expect_image_type, get_image_mode=GetImageMode.processed)
            labelsdata = LabelDataset(labels)
            labelsdata.binding_class_names(class_names)

            traindata = IterableDataset(data=imagedata, label=labelsdata)
            dataset = DataProviderV2(dataset_name, traindata=traindata)
            dataset.binding_class_names(class_names)

        else:
            imgs = glob.glob(base_folder + '/*.*g')
            imagedata = ImageDataset(imgs, expect_image_type=expect_image_type, get_image_mode=GetImageMode.processed)
            traindata = IterableDataset(data=imagedata)
            dataset = DataProviderV2(dataset_name, traindata=traindata)
        return dataset
    else:
        raise ValueError('')


def load_stanford_cars(dataset_name='cars', kind='train', is_flatten=None, is_onehot=None):
    dataset_name = dataset_name.strip().lower()

    if dataset_name.lower() not in ['car', 'cars']:
        raise ValueError('Only Cars is valid  dataset_name.')
    kind = kind.strip().lower().replace('ing', '')
    if _backend in ['tensorflow', 'cntk'] and is_onehot is None:
        is_onehot = True

    train_url = 'http://imagenet.stanford.edu/internal/car196/cars_train.tgz'
    test_url = 'http://imagenet.stanford.edu/internal/car196/cars_test.tgz'
    label_url = 'https://ai.stanford.edu/~jkrause/cars/car_devkit.tgz'
    dirname = os.path.join(_trident_dir, dataset_name)
    if not os.path.exists(dirname):
        try:
            os.makedirs(dirname)
        except OSError:
            # Except permission denied and potential race conditions
            # in multi-threaded environments.
            pass

    download_file(train_url, dirname, train_url.split('/')[-1], dataset_name + '_images_{0}'.format('train'))
    train_imgs_path = os.path.join(dirname, train_url.split('/')[-1])

    download_file(test_url, dirname, test_url.split('/')[-1], dataset_name + '_images_{0}'.format('test'))
    test_imgs_path = os.path.join(dirname, test_url.split('/')[-1])

    download_file(label_url, dirname, label_url.split('/')[-1], dataset_name + '_labels_{0}'.format(kind))
    labels_path = os.path.join(dirname, label_url.split('/')[-1])

    extract_archive(os.path.join(dirname, train_url.split('/')[-1].strip()), dirname, archive_format='tar')
    extract_archive(os.path.join(dirname, test_url.split('/')[-1].strip()), dirname, archive_format='tar')
    extract_archive(os.path.join(dirname, label_url.split('/')[-1].strip()), dirname, archive_format='tar')

    extract_path = os.path.join(dirname, label_url.split('/')[-1].strip().split('.')[0].replace('car_devkit', 'devkit'))
    cars_meta = read_mat(os.path.join(extract_path, 'cars_meta.mat'))['class_names'][0]  # size 196

    cars_annos = read_mat(os.path.join(extract_path, 'cars_train_annos.mat'))['annotations'][0]
    if kind == 'test':
        cars_annos = read_mat(os.path.join(extract_path, 'cars_test_annos.mat'))['annotations'][0]

    images_path = []
    labels = []
    for item in cars_annos:
        bbox_x1, bbox_x2, bbox_y1, bbox_y2, classid, fname = item
        images_path.append(fname)
        labels.append(np.array([bbox_x1, bbox_y1, bbox_x2, bbox_y2, classid]))

    dataset = DataProvider(dataset_name, data=images_path, labels=labels, scenario='train')
    dataset.binding_class_names(cars_meta, 'en-US')

    return dataset


def load_lfw(kind='train', is_flatten=None, is_onehot=None):
    dataset_name = 'lfw'
    kind = kind.strip().lower().replace('ing', '')
    if _backend in ['tensorflow', 'cntk'] and is_onehot is None:
        is_onehot = True

    dirname = os.path.join(_trident_dir, dataset_name)
    if not os.path.exists(dirname):
        try:
            os.makedirs(dirname)
        except OSError:
            # Except permission denied and potential race conditions
            # in multi-threaded environments.
            pass

    download_file('http://vis-www.cs.umass.edu/lfw/lfw.tgz', dirname, 'lfw.tgz')
    download_file('http://vis-www.cs.umass.edu/lfw/pairsDevTrain.txt', dirname, 'pairsDevTrain.txt')
    download_file('http://vis-www.cs.umass.edu/lfw/pairsDevTest.txt', dirname, 'pairsDevTest.txt')

    train_imgs_path = os.path.join(dirname, 'lfw.tgz')
    extract_path = os.path.join(_trident_dir, 'lfw')
    extract_archive(train_imgs_path, dirname, archive_format='tar')
    dataset = load_folder_images(dataset_name, dirname)

    extract_archive(train_imgs_path, dirname, archive_format='tar')
    dataset = load_folder_images(dataset_name, dirname)
    return dataset


def load_examples_data(dataset_name):
    dataset_name = dataset_name.strip().lower()
    if dataset_name.lower() not in ['pokemon', 'hanzi', 'animals', 'nsfw','simpsons','horse2zebra','people','autodrive']:
        raise ValueError('Not a  valid  dataset_name.')
    dataset_name = 'examples_' + dataset_name
    dirname = os.path.join(_trident_dir, dataset_name)
    if not os.path.exists(dirname):
        try:
            os.makedirs(dirname)
        except OSError:
            # Except permission denied and potential race conditions
            # in multi-threaded environments.
            pass

    if dataset_name == 'examples_pokemon':
        download_file_from_google_drive('1U-xc54fX9j9BcidvRa0ow6qjssMlSF2A', dirname, 'pokemon.tar')
        train_imgs_path = os.path.join(dirname, 'pokemon.tar')
        extract_path = os.path.join(dirname, 'pokemon')
        extract_archive(train_imgs_path, dirname, archive_format='tar')
        dataset = load_folder_images(dataset_name,extract_path, folder_as_label=False)
        print('get pokemon images :{0}'.format(len(dataset)))
        return dataset
    elif dataset_name == 'examples_hanzi':
        download_file_from_google_drive('13UEzSG0az113gpRPKPyKrIE2HDaA2P4H', dirname, 'hanzi.tar')
        train_imgs_path = os.path.join(dirname, 'hanzi.tar')
        extract_path = os.path.join(dirname, 'hanzi')
        extract_archive(train_imgs_path, dirname, archive_format='tar')
        dataset = load_folder_images(dataset_name, os.path.join(dirname, 'train'), folder_as_label=True,
                                     expect_image_type=ExpectImageType.gray)
        dataset_test = load_folder_images(dataset_name, os.path.join(dirname, 'test'), folder_as_label=True,
                                          expect_image_type=ExpectImageType.gray)

        dataset.testdata = dataset_test.traindata
        dataset.class_names['zh-cn'] = dataset.class_names['en-us']
        return dataset

    elif dataset_name == 'examples_animals':
        download_file_from_google_drive('19Cjq8OO6qd9k9TMZxlPjDpejDOdiHJoW', dirname, 'animals.tar')
        train_imgs_path = os.path.join(dirname, 'animals.tar')
        extract_path = os.path.join(dirname, 'animals')
        extract_archive(train_imgs_path, dirname, archive_format='tar')
        dataset = load_folder_images(dataset_name, dirname)
        return dataset
    elif dataset_name == 'examples_nsfw':
        download_file_from_google_drive('1EXpV2QUrSFJ7zJn8NqtqFl1k6HvXsUzp', dirname, 'nsfw.tar')
        train_imgs_path = os.path.join(dirname, 'nsfw.tar')
        extract_path = os.path.join(dirname, 'nsfw')
        extract_archive(train_imgs_path, dirname, archive_format='tar')
        trainData = np.load(os.path.join(dirname, 'train_porn_detector64_small.npy'), allow_pickle=True)
        testData = np.load(os.path.join(dirname, 'test_porn_detector64_small.npy'), allow_pickle=True)

        trainarray = ImageDataset(np.array(trainData[0].tolist()).transpose([0, 2, 3, 1]), expect_image_type=ExpectImageType.rgb, get_image_mode=GetImageMode.processed)
        trainlabel = LabelDataset(trainData[1].tolist())
        train_iter = IterableDataset(data=trainarray, label=trainlabel)

        testarray = ImageDataset(np.array(testData[0].tolist()).transpose([0, 2, 3, 1]),  expect_image_type=ExpectImageType.rgb, get_image_mode=GetImageMode.processed)
        testlabel = LabelDataset(testData[1].tolist())
        test_iter = IterableDataset(data=testarray, label=testlabel)
        print('training images: {0}  test images:{1}'.format(len(trainarray),len(testarray)))

        dataset = DataProviderV2(dataset_name, traindata=train_iter, testdata=test_iter)
        dataset.binding_class_names(['drawing', 'hentai', 'neutral', 'porn', 'sexy'], 'en-us')
        dataset.binding_class_names(['繪畫', '色情漫畫', '中性', '色情', '性感'], 'zh-tw')
        dataset.binding_class_names(['绘画', '色情漫画', '中性', '色情', '性感'], 'zh-cn')
        dataset.scenario = 'train'
        return dataset
    elif dataset_name == 'examples_simpsons':
        download_file_from_google_drive('1hGNFbfBv3EZ4nx4Qod6PtSYzO8H4QIxC', dirname, 'simpsons.tar')
        train_imgs_path = os.path.join(dirname, 'simpsons.tar')
        extract_path = os.path.join(dirname, 'simpsons')
        extract_archive(train_imgs_path, extract_path, archive_format='tar')
        dataset = load_folder_images(dataset_name, extract_path, folder_as_label=False)
        dataset.traindata.label=RandomNoiseDataset(shape=(100),random_mode='normal')
        print('get simpsons images :{0}'.format(len(dataset)))
        return dataset
    elif dataset_name == 'examples_horse2zebra':
        download_file_from_google_drive('1pqj-T90Vh4wVNBV09kYZWgVPsZUA2f7U', dirname, 'horse2zebra.tar')
        train_imgs_path = os.path.join(dirname, 'horse2zebra.tar')
        extract_path = os.path.join(dirname, 'horse2zebra')
        extract_archive(train_imgs_path, dirname, archive_format='tar')
        trainA= ImageDataset(list_pictures(os.path.join(dirname, 'trainA')), expect_image_type=ExpectImageType.rgb, get_image_mode=GetImageMode.processed)
        trainB= ImageDataset(list_pictures(os.path.join(dirname, 'trainB')), expect_image_type=ExpectImageType.rgb, get_image_mode=GetImageMode.processed)
        testA= ImageDataset(list_pictures(os.path.join(dirname, 'testA')), expect_image_type=ExpectImageType.rgb, get_image_mode=GetImageMode.processed)
        testB= ImageDataset(list_pictures(os.path.join(dirname, 'testB')), expect_image_type=ExpectImageType.rgb, get_image_mode=GetImageMode.processed)

        dataset = load_folder_images(dataset_name, extract_path, folder_as_label=False)

        print('get horse2zebra images :{0}'.format(len(dataset)))
        return dataset
    elif dataset_name == 'examples_people':
        download_file_from_google_drive('1H7mJJfWpmXpRxurMZQqY4N_UXWLbQ2pT', dirname, 'people.tar')
        train_imgs_path = os.path.join(dirname, 'people.tar')
        extract_path = os.path.join(dirname, 'people')
        extract_archive(train_imgs_path, dirname, archive_format='tar')
        dataset = load_folder_images(dataset_name, os.path.join(dirname, 'imgs'), folder_as_label=False)

        print('get people images :{0}'.format(len(dataset)))
        return dataset
    elif dataset_name == 'examples_autodrive':
        download_file_from_google_drive('1JqPPeHqhWLqnI6bD8nuHcVx-Y56oIZMK', dirname, 'autodrive.tar')
        train_imgs_path = os.path.join(dirname, 'autodrive.tar')
        extract_path = os.path.join(dirname, 'autodrive')
        extract_archive(train_imgs_path, dirname, archive_format='tar')
        dataset = load_folder_images(dataset_name, os.path.join(dirname, 'images'), folder_as_label=False)

        print('get autodrive images :{0}'.format(len(dataset)))
        return dataset

    else:
        return None