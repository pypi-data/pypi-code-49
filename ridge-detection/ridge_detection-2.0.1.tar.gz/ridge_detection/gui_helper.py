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

from tkinter import Tk, messagebox,Button, Label,scrolledtext,INSERT
from os import path, listdir

class gen_id(object):
    """
    Generator, that returns the current row for the grid alignment
    """
    def __init__(self):
        self.row=0
    def __next__(self):
        return self.next()
    def next(self):
        self.row=self.row+1
        return self.row
    def prev(self):
        self.row=max(self.row-1,0)
        return self.row
    def current(self):
        return self.row

def click_exit():
    exit()


# message box info for the params

def click_info_setfile():
    messagebox.showinfo("Set file","Select the image to analyze")

def click_info_general():
    messagebox.showinfo("General","They are used to estimate the mandatory parameters.\n\nAt version 1.3.0 they are still not implemented")
def click_info_line_width():
    messagebox.showinfo("Line Width","The line diameter in pixels.\nIt estimates the mandatory parameter 'Sigma'")
def click_info_high_contrast():
    messagebox.showinfo("High Contrast","Highest grayscale value of the line.\nIt estimates the mandatory parameter 'Upper threshold'")
def click_info_low_contrast():
    messagebox.showinfo("Low Contrast","Lowest grayscale value of the line.\nIt estimates the mandatory parameter 'Lower threshold'")
def click_info_sigma():
    messagebox.showinfo("Sigma","Determines  the sigma for the derivatives. It depends on the line width")
def click_info_threshold_lw():
    messagebox.showinfo("Lower_Threshold","Line points with a response smaller as this threshold are rejected")
def click_info_threshold_up():
    messagebox.showinfo("Upper_Threshold","Line points with a response larger as this threshold are accepted")
def click_info_darkline():
    messagebox.showinfo("DarkLine","Determines whether dark or bright lines are extracted by the ridge detection tool")
def click_info_overlap():
    messagebox.showinfo("Overlap resolution"," You can select a method to attempt automatic overlap resolution. The accuracy of this method will depend on the structure of your data")
def click_info_correct_position():
    messagebox.showinfo("Correct position","Correct the line position if it has different contrast on each side of it")
def click_info_estimate_width():
    messagebox.showinfo("Estimate width","If this option is selected the width of the line is estimated")
def click_info_do_extend_line():
    messagebox.showinfo("Do ExtendLine","Try to extend the lines at their end_points to find additional junctions")
def click_info_show_junctions():
    messagebox.showinfo("Show junction point","Show the junction points in the output image")
def click_info_show_ids():
    messagebox.showinfo("Show IDs","The ID of each line will be shown.\n\nAt version 1.3.0 they are still not implemented")
def click_info_display_results():
    messagebox.showinfo("Display results","All contours and junctions are filled into a results table\n\nAt version 1.3.0 they are still not implemented")
def click_info_preview():
    messagebox.showinfo("Preview","Show the results before saving on disk")
def click_info_make_binary():
    messagebox.showinfo("Make binary","Binarize the output.\n\nAt version 1.3.0 they are still not implemented")


def show_info():
    """
    It creates the info windows. each botton open a message info about the selected parameter
    :return:
    """
    id_row = gen_id()
    id_col_detection = gen_id()
    id_col_filtering = gen_id()
    id_col_general = gen_id()
    window_info = Tk()
    window_info.title("Parameters information")
    window_info.geometry('1300x250')

    lbl = Label(window_info, text="Selection path image:")
    lbl.grid(column=0, row=id_row.current())
    btn = Button(window_info, text="Set file", command=click_info_setfile)
    btn.grid(column=1, row=id_row.current())

    lbl = Label(window_info)
    lbl.grid(column=id_col_detection.current(), row=id_row.next())
    lbl = Label(window_info, text="Mandatory Parameters:")
    lbl.grid(column=id_col_detection.current(), row=id_row.next())
    btn = Button(window_info, text="Sigma", command=click_info_sigma)
    btn.grid(column=id_col_detection.current(), row=id_row.next())
    btn = Button(window_info, text="Lower_Threshold", command=click_info_threshold_lw)
    btn.grid(column=id_col_detection.next(), row=id_row.current())
    btn = Button(window_info, text="Upper_Threshold", command=click_info_threshold_up)
    btn.grid(column=id_col_detection.next(), row=id_row.current())
    btn = Button(window_info, text="DarkLine", command=click_info_darkline)
    btn.grid(column=id_col_detection.next(), row=id_row.current())
    btn = Button(window_info, text="Overlap", command=click_info_overlap)
    btn.grid(column=id_col_detection.next(), row=id_row.current())

    lbl = Label(window_info)
    lbl.grid(column=id_col_general.current(), row=id_row.next())
    lbl = Label(window_info, text="Optional Parameters")
    lbl.grid(column=id_col_general.current(), row=id_row.next())
    lbl = Label(window_info, text="( not available at the current version):")
    lbl.grid(column=id_col_general.next(), row=id_row.current())
    btn = Button(window_info, text="General", command=click_info_general)
    btn.grid(column=id_col_general.prev(), row=id_row.next())
    btn = Button(window_info, text="Line width", command=click_info_line_width)
    btn.grid(column=id_col_general.next(), row=id_row.current())
    btn = Button(window_info, text="High contrast", command=click_info_high_contrast)
    btn.grid(column=id_col_general.next(), row=id_row.current())
    btn = Button(window_info, text="Low contrast", command=click_info_low_contrast)
    btn.grid(column=id_col_general.next(), row=id_row.current())

    lbl = Label(window_info)
    lbl.grid(column=id_col_filtering.current(), row=id_row.next())
    lbl = Label(window_info, text="Further Parameters:")
    lbl.grid(column=id_col_filtering.current(), row=id_row.next())
    btn = Button(window_info, text="Correct position", command=click_info_correct_position)
    btn.grid(column=id_col_filtering.current(), row=id_row.next())
    btn = Button(window_info, text="Estimate width", command=click_info_estimate_width)
    btn.grid(column=id_col_filtering.next(), row=id_row.current())
    btn = Button(window_info, text="Do ExtendLine", command=click_info_do_extend_line)
    btn.grid(column=id_col_filtering.next(), row=id_row.current())
    btn = Button(window_info, text="Show junction point", command=click_info_show_junctions)
    btn.grid(column=id_col_filtering.next(), row=id_row.current())
    btn = Button(window_info, text="Show IDs", command=click_info_show_ids)
    btn.grid(column=id_col_filtering.next(), row=id_row.current())
    btn = Button(window_info, text="Display results", command=click_info_display_results)
    btn.grid(column=id_col_filtering.next(), row=id_row.current())
    btn = Button(window_info, text="Preview", command=click_info_preview)
    btn.grid(column=id_col_filtering.next(), row=id_row.current())
    btn = Button(window_info, text="Make Binary", command=click_info_make_binary)
    btn.grid(column=id_col_filtering.next(), row=id_row.current())



    window_info.mainloop()