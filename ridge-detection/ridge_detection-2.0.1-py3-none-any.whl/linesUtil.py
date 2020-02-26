"""
MIT License

Copyright (c) 2020 Max Planck Institute of Molecular Physiology

Author: Luca Lusnig (luca.lusnig@mpi-dortmund.mpg.de)
Author: Thorsten Wagner (thorsten.wagner@mpi-dortmund.mpg.de)
Author: Markus Stabrin (markus.stabrin@mpi-dortmund.mpg.de)
Author: Fabian Schoenfeld (fabian.schoenfeld@mpi-dortmund.mpg.de)
Author: Tapu Shaikh (tapu.shaikh@mpi-dortmund.mpg.de)
Author: Adnan Ali (adnan.ali@mpi-dortmund.mpg.de)


Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""



from math import ceil

""" list of constant present in LineUtils.java"""
DERIV_R = 1  # Derivative in row direction
DERIV_C = 2  # Derivative in column direction
DERIV_RR = 3  # Second derivative in row direction
DERIV_RC = 4  # Second derivative in row and column direction
DERIV_CC = 5  # Second derivative in column direction
MODE_LIGHT = 1  # Extract bright lines
MODE_DARK = 2  # Extract dark lines
INITIAL_SIZE = 100
REALLOC_FACTOR = 2
MAX_SIZE_MASK_0 = 3.09023230616781  # Size for Gaussian mask
MAX_SIZE_MASK_1 = 3.46087178201605  # Size for 1st derivative mask
MAX_SIZE_MASK_2 = 3.82922419517181  # Size for 2nd derivative mask
ERR_SOR = "Sigma out of range:"
COUNTOUR_DICT=  {
                'cont_no_junc': 0,           # The cont no junc.
                'cont_start_junc': 1,        # The cont start junc ... no end point is a junction
                'cont_end_junc': 2,          # The cont end junc ... only the start point of the line is a junction
                'cont_both_junc': 3,         # The cont both junc ... both end points of the line are junctions
                'cont_closed': 4             # the contour is closed
                }

""" functions declared in LineUtils.java"""
def mask_size(maximum, sigma):
    """
    :param maximum:
    :param sigma:
    :return: maximum mask index
    """
    return int( ceil(maximum*sigma))

def lincoord(row, col,width):
    """
    Translate row and column coordinates of an image into an index into its one-dimensional array
    :param row:
    :param col:
    :param width:
    :return:
    """
    return row * width + col

def br(row,height):
    """Mirror the row coordinate at the borders of the image; height must be a defined variable in the calling function containing the image height."""
    if row<0:
        return -row
    elif row >= height:
        return height - row + height - 2
    return row

def bc(col, width):
    """Mirror the column coordinate at the borders of the image; width must be a defined variable in the calling function containing the image width"""
    if col<0:
        return -col
    elif col >= width:
        return width - col + width - 2
    return col

