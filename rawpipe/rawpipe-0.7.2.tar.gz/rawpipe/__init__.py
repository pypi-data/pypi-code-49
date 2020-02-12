"""A collection of camera raw processing algorithms.

A collection of reference ISP algorithms, sufficient for producing a reasonably
good looking image from raw sensor data. Each algorithm takes in a frame in RGB
or raw format and returns a modified copy of the frame. The frame is expected to
be a NumPy float array with either 2 or 3 dimensions, depending on the function.
Some of the algorithms can be applied in different orders (demosaicing before or
after linearization, for example), but the reference ordering is as shown below.

Example:
  algs = rawpipe.Algorithms(verbose=True)
  raw = algs.downsample(raw, iterations=2)
  raw = algs.linearize(raw, blacklevel=64, whitelevel=1023)
  rgb = algs.demosaic(raw, "RGGB")
  rgb = algs.lsc(rgb, my_vignetting_map)
  rgb = algs.lsc(rgb, my_color_shading_map)
  rgb = algs.resize(rgb, 400, 300)
  rgb = algs.wb(rgb, [1.5, 2.0])
  rgb = algs.ccm(rgb, my_3x3_color_matrix)
  rgb = algs.tonemap(rgb, "Reinhard")
  rgb = algs.chroma_denoise(rgb)
  rgb = algs.gamma(rgb, "sRGB")
  rgb = algs.quantize(rgb, 255)
"""

from .rawpipe import Algorithms

__version__ = "0.7.2"
__all__ = ["Algorithms"]
