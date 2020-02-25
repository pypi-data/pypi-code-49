######################################################
#
#           nazobase distribution
#           by F@NAZOrip
#           Version 0.2.1
#           Latest release : 
#
######################################################
#
# functinos included:
#   check
#   dataloader
#   diff
#   gp
#   nazo3d
#   quickresize
#   wf2x
#
######################################################
#
# Special thanks to mawen1250 
# (https://github.com/mawen1250) 's mvsfunc tool.
# Since he did't uploaded his script to pypi,
# I had to place it in this folder as attchment
# for importing ,instead of using package manager.
# 
######################################################
######################################################
######################################################
#
#            Function Description
#
######################################################
# 
'''
# Function name : [[check]]
######################################################

  Automatically adjust format/bit depth/FPS of clip those in clips to clipa,
  and then return a interleaved clip.
  
  The script will automatically traceback your output node ,and label on top left corner using text.Text()

  You should not use it nested ,since based on string backtracing ,that will cause confuse.

######################################################
  Attributes:

      VideoNode clipa:
          target videonode for adjusting.

      *(VideoNode clipbs:)
          one or more videonode to adjust.
          of course you can also leave it empty.
  
  Usage:

      # a simple demo for checking the relationships between
      # the Cb plane and edge of Luma Plane

      import vapourysynth as vs
      import nazobase as nazo

      core = vs.core

      src10 = nazo.dataloader('video.mp4')

      nazo.check(nazo.getplane(src10,1) , core.tcanny.Tcanny(src10) ).set_output()

  Wrong use:

      from nazobase import *
      
      ...

      check(check(clipa, clipb), clipc).set_output()

  
######################################################
# Function name : [[dataloader]]
######################################################

  
  Script helps loads data conveniently.

  Auto checks if your input is a video or image.
  *(support type jpg/png/bmp ,ignore case)

  Auto loads the depth you want ,
  support one or more request.

######################################################
  Attributes:

      string source:
          Your source path
          Last two character of each node matters,
          cause depth conversion depends on them.

      (int first:)
                          
      (int last:)
          Returns the frames between the arguments first and last

      (bool info:)
          Switch if you want to attach media info of source into frames.


  Usage:
      
      import vapoursynth as vs
      import nazobase as nazo

      core = vs.core

      src8, src10, src16 = nazo.dataloader('video.mp4')
      src16.set_output()

      ↑ Thus you'll get three clips with specific depth respectively
      based on string check.

  Have fun.

  
######################################################
# Function name : [[diff]]
######################################################


  Easy function helps you check out differences between clips.
  Expression : luminance = abs( clipa - clipb ) * amp

######################################################
  Attributes:

      VideoNode clipa:
          
      VideoNode clipb:
          Format insensitive ,
          Clipb will be converted into the vary format of clipa at first.

      (int amp:) 
          Adjust strength of the amplifier.

      (int[] planes:)
          
      (bool binarize:)
          If true, each pair of pixel who are not exactly the same
          will be highlight labeled. 

      (bool maskedmerge:)
          Showing a merged picture of differences between pixels like using alpha channel.
          Trun on this if you don't like "check(src1,diff(src1,src2))".

  
######################################################
# Function name : [[gp]]
######################################################

  fast std.ShufflePlanes()
  
######################################################
# Function name : [[nazo3d]]
######################################################

  Wrapper of BM3D ,with optional degrain method,
  and final estimate corrections.

######################################################
  Attributes:

      VideoNode clip:
          Target.
          RGB24 to RGBS ;
          YUV420 / 422 / 444 P8/P16/P32 ;
          GRAY8 to GRAYS accepted.

      (float nrluma:)
          The strength of denoising, valid range [0, +inf)

      (float nrchroma:)
          The strength of denoising, valid range [1, +inf).
          Processing method of chroma planes will switch between BM3D and NL-meansbe ,which is selected by whether this value is larger than 1.6 .

      (str profile:)
          Preset profiles of BM3D.
          A table below shows the default parameters for each profile.

          "fast" - Fast Profile (default)
          "lc" - Low Complexity Profile
          "np" - Normal Profile
          "high" - High Profile
          "vn" - Very Noisy Profile

      (int d:)
          Set the number of past and future frame that the filter uses for denoising the current frame of KNL-means. d=0 uses 1 frame, while d=1 uses 3 frames and so on. Usually, larger it the better the result of the denoising. Temporal size = (2 * d + 1).
      
      (int a:)
          Set the radius of the search window. a=0 uses 1 pixel, while a=1 uses 9 pixels and so on. Usually, larger it the better the result of the denoising. Spatial size = (2 * a + 1)^2.  

          Tip: total search window size = temporal size * spatial size.

      (int s:)
          Set the radius of the similarity neighbourhood window of KNL-means ,which take effect in processing chroma planes. The impact on performance is low, therefore it depends on the nature of the noise. Similarity neighborhood size = (2 * s + 1)^2.

  Usage:

      # load source
      ... 
      # 
      src16 = ToYUV(src , css = '444' , depth = 16)
      nr16 = nazo3d(src16 , profile = 'np')
      nr16.set_output()
  
  
######################################################
# Function name : [[quickresize]]
######################################################

  resize avoids resampling lose in YUV/RGB converting ,
  use this if there's no need to change color space.

  Default using BT709 & TVrange for animation processing.

######################################################
  Attributes:

      VideoNode clip:
          Target.

      (int width:)
          Width will not change if not specified.

      (int height:)
          Height will not change if not specified.

      (str Kernel:)
          The resize kernel we used is components from vapoursynth standard library. Input as string and it will be converted into function by black magic eval().

          Case insensitive.

      (resize_kwargs:)
          Custom resize attributes if you want.

  Usage:

      from nazobase import *

      src = dataloader('video.mp4')
      # convert with bicubic b/c = 1/3
      res = quickresize(src, 1920, 1080, 'bicubic', filter_param_a = 1/3, filter_param_b = 1/3)

      res.set_output()
  
  
######################################################
# Function name : [[wf2x]]
######################################################

  Wrapper of waifu2x-caffe ,speed up your procedure
  by slicing stream into interleave frames ,and
  process them multithreadly.
  It's highly recommended to run some memory load test
  before production.

######################################################
  Attributes:

      VideoNode clip:
          Target. YUV/RGB/Gray is accepted.

      (int noise:)
          Denoise level from waifu2x-caffe params.

      (int scale:)
          Geometry xN scale ,from waifu2x-caffe params.

      (int block_w:)
          Block width of each individual process.
          The higher block size brings you higher speed ,
          however larger RAM usage combined.

      (int block_h:)
          Same.
                  
      (int model:)
          Resize neural network kernel of waifu2x.

      (int slice:)
          Turn waifu2x into n threads running ,
          helps you squeezing all power of you PC.
          Theoretically this option will brings you 
          n times speed along with n times memory 
          use under enough compute power.

      (int depth:)
          Output depth.
      
      (float shift:)
          Chroma shift of resizing.

      (str shrink:)
          Kernel of shrink method while you convert
          back to YUV after drawing.
          options:
              'dekernel' : always brings more Sharpness.
              'dpid' : new gen scaling algorithm.
              'normal' : general processing.
  
  
######################################################
'''


from .base import *