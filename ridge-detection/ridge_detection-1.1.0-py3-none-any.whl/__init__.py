__version__ = "1.1.0"

"""
0.0.1 first running version
0.0.2 change the structures of the package
0.0.3 vectorization critical 'convolve_row_gauss' and 'convolve_cols_gauss' and optimized 'convolve_gauss' flow
0.0.4 added function to skeletonize the detected lines
0.0.5 speed up the code precalculating the '_ctable' table of Correct obj in width.py:
      It took 0.002 second per call but it was called for each point found. Now it is called for each lines ( e.g: 80 times instead of 22000)
1.0.0 First stable version and optimized version. Added all the tests
1.0.1 Added a logger . The code generates the 'ridge_detection_X_Y.log' file. Where X=day Y=starting time
1.1.0 Moved the function called and implemented in the main.py in the helper.py to make the package uploadable to pipy 
"""

#todo
"""
For now __version__ = "1.1.0" it is possible to run the code always using the mandatory params ... hence it is not possible calculate them from the 'optional paramter' as written in the README.md
"""