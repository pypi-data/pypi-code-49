from skimage.color import rgb2hed
import numpy as np
import cv2


if __name__ == '__main__':
    #                           R       G      B
    deconv_matrix = np.array([[1.88,  -0.07, -0.60],     # Hematoxylin
                              [-1.02,  1.13, -0.48],     # Eosin
                              [-0.55, -0.13, 1.57]])     # DAB
    deconv_matrix = rgb2hed
    tissue = cv2.imread('../../../data/muscular_tissue.png')
    cv2.imshow('Tissue', tissue)
    cv2.waitKey(0)
    tissue = cv2.cvtColor(tissue, cv2.COLOR_BGR2RGB)
    dec = rgb2hed(tissue)
    print(dec[:, :, 0])
    norm = np.empty(shape=dec.shape, dtype=np.uint8)
    for i in range(dec.shape[2]):
        norm[:, :, i] = cv2.normalize(dec[:, :, i], None, 0, 255, cv2.NORM_MINMAX, 8)

    cv2.imshow('Hematoxylin', norm[:, :, 0])
    cv2.imshow('Eosin', norm[:, :, 1])
    cv2.imshow('DAB', norm[:, :, 2])
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.namedWindow('Classification')
    cv2.createTrackbar('Cutoff Nucleus', 'image', 0, 255, lambda x: print(x))
    cv2.imshow('image', tissue)
    cv2.waitKey(0)
