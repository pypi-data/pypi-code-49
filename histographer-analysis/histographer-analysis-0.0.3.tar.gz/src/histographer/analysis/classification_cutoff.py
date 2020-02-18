from skimage.color import rgb2hed
import cv2
import numpy as np


if __name__ == '__main__':
    def nothing(x):
        pass

    winname = 'Bayesian Classifier'
    
    # Create a black image, a window
    cv2.namedWindow(winname)

    # create trackbars for color change
    cv2.createTrackbar('Cutoff Nucleus', winname, 0, 255, nothing)
    cv2.createTrackbar('Cutoff Tissue', winname, 0, 255, nothing)

    tissue = cv2.imread('../../../data/muscular_tissue.png')
    cv2.imshow('Tissue', tissue)
    hed = rgb2hed(cv2.cvtColor(tissue, cv2.COLOR_BGR2RGB))

    # Normalize channels
    hedn = np.zeros(hed.shape, np.uint8)
    for i in range(hed.shape[2]):
        hedn[..., i] = cv2.normalize(hed[..., i], None, 0, 255, cv2.NORM_MINMAX, 8).copy()

    img = tissue.copy()
    while True:
        cv2.imshow(winname, img)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

        # get current positions of four trackbars
        cn = cv2.getTrackbarPos('Cutoff Nucleus', winname)
        ct = cv2.getTrackbarPos('Cutoff Tissue', winname)

        img[:] = tissue.copy()
        img[hedn[..., 1] > ct, ...] = [0, 0,   255]
        img[hedn[..., 0] > cn, ...] = [0, 255, 0]


    cv2.destroyAllWindows()
