"""
A collection of reference ISP algorithms.
"""

import time             # built-in library
import numpy as np      # pip install numpy
import cv2              # pip install opencv-python


class Algorithms:
    """
    A collection of ISP algorithms. See help(rawpipe) for documentation.
    """

    def __init__(self, verbose=False):
        """
        Initialize self. If verbose is True, progress information will be printed
        to stdout.
        """
        self.verbose = verbose

    def downsample(self, frame, iterations=1):
        """
        Downsample the given RGB/Bayer frame by a factor of two in both directions,
        that is, to a quarter of its original size. This is repeated a given number
        of iterations. If iterations is zero, the frame is returned untouched. See
        resample() for arbitrary resizing with proper interpolation in RGB domain.
        """
        if iterations >= 1:
            t0 = time.time()
            orgh, orgw = frame.shape[:2]
            if frame.ndim == 3:  # RGB mode
                mode = "RGB"
                frame = frame[::2*iterations, ::2*iterations]
            if frame.ndim == 2:  # Bayer mode
                mode = "Bayer"
                for _ in range(iterations):
                    imgh, imgw = frame.shape[:2]
                    ch1 = frame[0::2, 0::2][::2, ::2]
                    ch2 = frame[0::2, 1::2][::2, ::2]
                    ch3 = frame[1::2, 0::2][::2, ::2]
                    ch4 = frame[1::2, 1::2][::2, ::2]
                    frame = np.zeros(shape=(imgh // 2, imgw // 2), dtype=frame.dtype)
                    frame[0::2, 0::2] = ch1
                    frame[0::2, 1::2] = ch2
                    frame[1::2, 0::2] = ch3
                    frame[1::2, 1::2] = ch4
            imgh, imgw = frame.shape[:2]
            factor = f"{2**iterations} x {2**iterations}"
            self._vprint(f"{_elapsed(t0)} - {mode} downsampling [{factor}] from {orgw} x {orgh} to {imgw} x {imgh}")
        return frame

    def resize(self, frame, target_width, target_height):
        """
        Resize the given RGB frame to the given target width and height using Lanczos
        interpolation. If target width and height are the same as current width and
        height, the frame is returned untouched.
        """
        t0 = time.time()
        orgh, orgw = frame.shape[:2]
        dsth, dstw = int(target_height), int(target_width)
        if (dstw, dsth) != (orgw, orgh):
            frame = cv2.resize(frame, (dstw, dsth), cv2.INTER_LANCZOS4)
            dsth, dstw = frame.shape[:2]
            self._vprint(f"{_elapsed(t0)} - resizing [Lanczos] from {orgw} x {orgh} to {dstw} x {dsth}")
        return frame

    def linearize(self, frame, blacklevel=None, whitelevel=None, num_clipped=1000):
        """
        Linearize the given frame such that pixels are first clipped to the range
        [BL, WL] and then remapped to [0, 1], where BL and WL are the given black
        level and white level, respectively. If blacklevel is None, it is taken to
        be the Nth smallest pixel value within the frame, where N = num_clipped+1.
        A missing whitelevel is similarly estimated as the Nth largest pixel value.
        This algorithm is format-agnostic, although it's typically applied on raw
        sensor data.
        """
        if blacklevel is None:
            t0 = time.time()
            percentile = num_clipped / frame.size * 100.0
            blacklevel = np.percentile(frame, percentile)
            self._vprint(f"{_elapsed(t0)} - estimating black level: {percentile:5.2f}th percentile = {blacklevel:.2f}")
        if whitelevel is None:
            t0 = time.time()
            percentile = (1.0 - num_clipped / frame.size) * 100.0
            whitelevel = np.percentile(frame, percentile)
            self._vprint(f"{_elapsed(t0)} - estimating white level: {percentile:5.2f}th percentile = {whitelevel:.2f}")
        if (blacklevel, whitelevel) != (0, 1):
            t0 = time.time()
            frame = np.clip(frame, blacklevel, whitelevel)
            frame -= blacklevel
            frame /= whitelevel - blacklevel
            self._vprint(f"{_elapsed(t0)} - linearizing from [{blacklevel:.2f}, {whitelevel:.2f}] to [0, 1]")
        return frame

    def demosaic(self, frame, bayer_pattern):
        """
        Demosaic the given sensor raw frame using the Edge Aware Demosaicing (EAD)
        algorithm. Bayer order must be specified by the caller, and must be "RGGB",
        "GBRG", "BGGR", or "GRBG".
        """
        t0 = time.time()
        bayer_to_cv2 = {"RGGB": cv2.COLOR_BAYER_BG2RGB_EA,
                        "GBRG": cv2.COLOR_BAYER_GR2RGB_EA,
                        "BGGR": cv2.COLOR_BAYER_RG2RGB_EA,
                        "GRBG": cv2.COLOR_BAYER_GB2RGB_EA}
        frame = (frame * 65535).astype(np.uint16)
        frame = cv2.cvtColor(frame, bayer_to_cv2[bayer_pattern.upper()])
        frame = frame / 65535.0
        self._vprint(f"{_elapsed(t0)} - demosaicing [EAD, {bayer_pattern}]: range = {_minmax(frame)}")
        return frame

    def lsc(self, frame, lscmap):
        """
        Multiply the given RGB frame by the given lens shading correction (LSC)
        map. The LSC map may be grayscale to correct vignetting only, or RGB to
        correct both vignetting and color shading. If lscmap is None, the frame
        is returned untouched.
        """
        if lscmap is not None:
            t0 = time.time()
            imgh, imgw = frame.shape[:2]
            lsch, lscw = lscmap.shape[:2]
            need_resize = lscmap.shape[:2] != frame.shape[:2]
            if need_resize:
                xgrid = np.linspace(0, lscw - 1, imgw)
                ygrid = np.linspace(0, lsch - 1, imgh)
                mgrid = np.dstack(np.meshgrid(xgrid, ygrid, indexing="xy"))
                numthreads = cv2.getNumThreads()
                cv2.setNumThreads(0)  # work-around for OpenCV 4.1.2 deadlock
                lscmap = cv2.remap(lscmap, mgrid.astype(np.float32), None, cv2.INTER_LINEAR)
                cv2.setNumThreads(numthreads)
            lscmap = np.atleast_3d(lscmap)  # {RGB, monochrome} => RGB
            frame = frame * lscmap
            with np.printoptions(formatter={'float': lambda x: f"{x:.3f}"}):
                gains = np.amax(lscmap, axis=(0, 1))
                self._vprint(f"{_elapsed(t0)} - applying lens shading correction {gains}: range = {_minmax(frame)}")
        return frame

    def wb(self, frame, gains):
        """
        Multiply the RGB channels of the given frame by the given white balance
        coefficients. If there are only two coefficients instead of three, they
        are applied on the R and B channels. If gains is None, the frame is
        returned untouched.
        """
        if gains is not None:
            t0 = time.time()
            gains = np.array(gains)
            gains = np.insert(gains, 1, 1.0) if len(gains) == 2 else gains
            frame = frame * gains
            with np.printoptions(formatter={'float': lambda x: f"{x:.3f}"}):
                self._vprint(f"{_elapsed(t0)} - applying WB gains {gains}: range = {_minmax(frame)}")
        return frame

    def ccm(self, frame, matrix):
        """
        Apply the given color correction matrix on the given RGB frame. Input
        colors are clipped to [0, 1] to avoid "pink sky" artifacts caused by the
        combination of clipped highlights and less-than-1.0 coefficients in the
        CCM. In other words, no attempt is made at gamut mapping or highlight
        recovery. If matrix is None, the frame is returned untouched.
        """
        if matrix is not None:
            t0 = time.time()
            frame = np.clip(frame, 0, 1)
            frame = np.matmul(frame, matrix.T)
            with np.printoptions(formatter={'float': lambda x: f"{x:.2f}"}):
                sums = f"with column sums {np.sum(matrix, axis=0).T}"
                self._vprint(f"{_elapsed(t0)} - applying CCM {sums}: range = {_minmax(frame)}")
        return frame

    def tonemap(self, frame, mode="Reinhard"):
        """
        Apply Reinhard tonemapping on the given RGB frame, compressing the range
        [0, N] to [0, 1]. Negative values are clipped to zero. This algorithm is
        format-agnostic. If mode is not "Reinhard", the frame is returned untouched.
        """
        if mode is not None:
            if mode == "Reinhard":
                t0 = time.time()
                frame = np.maximum(frame, 0)
                frame = frame.astype(np.float32)  # can't handle float64
                algo = cv2.createTonemapReinhard(gamma=1.0, intensity=0.0, light_adapt=0.0, color_adapt=0.0)
                frame = algo.process(frame)
                self._vprint(f"{_elapsed(t0)} - tonemapping [{mode}]: range = {_minmax(frame)}")
        return frame

    def chroma_denoise(self, frame, strength=6, winsize=17):
        """
        Apply non-local means denoising (Buades et al. 2011) on the given RGB frame.
        Input colors are clipped to [0, 1] prior to denoising. Increasing the values
        of filter strength and search window size make the denoising more aggressive
        and more time-consuming. If strength is 0, the frame is returned untouched.
        """
        if strength > 0:
            t0 = time.time()
            maxval, dtype = (255, np.uint8)  # OpenCV denoising can't handle 16-bit color
            frame = np.clip(frame * maxval + 0.5, 0, maxval)
            frame = frame.astype(dtype)
            frame = cv2.fastNlMeansDenoisingColored(frame, h=0, hColor=strength, searchWindowSize=winsize)
            frame = frame.astype(np.float32) / maxval
            self._vprint(f"{_elapsed(t0)} - chroma denoising [s={strength:.2f}, w={winsize}]: range = {_minmax(frame)}")
        return frame

    def gamma(self, frame, mode="sRGB", lut=None):
        """
        Apply rec709 or sRGB gamma or a custom tone curve on the given frame.
        In "LUT" mode, a look-up table with N entries must be provided, where
        N equals 2 ** bpp (e.g., N=4096 for 12-bit colors). This algorithm is
        format-agnostic. If mode is None, the frame is returned untouched.
        """
        if mode is not None:
            t0 = time.time()
            realmode = mode
            frame = np.clip(frame, 0, 1)  # can't handle values outside of [0, 1]
            if realmode in ["sRGB", "rec709"]:
                bpp = 14
                N = 2 ** bpp
                maxval = 2 ** bpp - 1
                lut = np.linspace(0, 1, N)
                mode = "LUT"
            if realmode == "sRGB":
                srgb_lo = 12.92 * lut
                srgb_hi = 1.055 * np.power(lut, 1.0/2.4) - 0.055
                threshold_mask = (lut > 0.0031308)
                lut = srgb_hi * threshold_mask + srgb_lo * (~threshold_mask)
                lut = lut * maxval
            if realmode == "rec709":
                srgb_lo = 4.5 * lut
                srgb_hi = 1.099 * np.power(lut, 0.45) - 0.099
                threshold_mask = (lut > 0.018)
                lut = srgb_hi * threshold_mask + srgb_lo * (~threshold_mask)
                lut = lut * maxval
            if mode == "LUT":
                maxval = len(lut) - 1
                verbose, self.verbose = self.verbose, False
                frame = self.quantize(frame, maxval)  # [0, 1] ==> [0, maxval]
                frame = lut[frame]                    # [0, maxval] ==> [0, maxval]
                frame = frame / maxval                # [0, maxval] ==> [0, 1]
                self.verbose = verbose
            self._vprint(f"{_elapsed(t0)} - applying gamma curve [{realmode}]: range = {_minmax(frame)}")
        return frame

    def quantize(self, frame, maxval, dtype=np.uint16):
        """
        Clip the given frame to [0, 1], rescale it to [0, maxval], and convert
        it to the given dtype with proper rounding. This algorithm is format-
        agnostic.
        """
        t0 = time.time()
        frame = np.clip(frame * maxval + 0.5, 0, maxval)
        frame = frame.astype(dtype)
        self._vprint(f"{_elapsed(t0)} - clipping to [0, 1] and rescaling to [0, {maxval}]")
        return frame

    def _vprint(self, message, **kwargs):
        if self.verbose:
            print(message, **kwargs)


def _elapsed(t0):
    elapsed = (time.time() - t0) * 1000
    elapsed = f"{elapsed:8.2f} ms"
    return elapsed


def _minmax(frame):
    minmax = f"[{np.min(frame):.2f}, {np.max(frame):.2f}]"
    return minmax
