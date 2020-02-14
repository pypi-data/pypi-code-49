# -*- coding: utf-8 -*-
"""
Created on some day of 2018 or 2019
@author: cottephi@gmail.com
"""

import os
import time
import pandas as pd
from copy import deepcopy
from pathlib import Path

"""
Class used to produce a ready-to-compile .tex file containing a table from a
pandas.DataFrame object. Can also compile the .tex to produce a .pdf. Handles
using additional latex packages.
The given DataFrame is copied so any modification of the said DataFrame after
instensiation of the TableWriter object has no effect on the TableWriter
object, and vice-versa.

This class uses pandas.DataFrame.to_latex and adds some more options to produce a
.pdf by itself. Any option that must be given to the to_latex method can be given
to the TableWriter through the to_latex_args argument.

If you want to modify the DataFrame contained in the TableWriter object, use get_data
to get a deepcopy of the DataFrame, modify the DataFrame, then reset it to TableWriter
using set_data.
"""


class TableWriter:
    
    VERBOSE = 0
    @classmethod
    def set_verbose(cls, v):
        TableWriter.VERBOSE = v
    
    @classmethod
    def printv(cls, s):
        if TableWriter.VERBOSE > 0:
            print(s)
    
    @classmethod
    def set_print(cls, method):
        global print
        print = method
    
    # //////////////////
    # // Initialisers //
    # //////////////////
    
    def __init__(self, **kwargs):
        """
        All parameters are optionnal and can be modified by dedicated setters.
        
        Parameters
        ----------
        data : {DataFrame type}
            Data to transform to table
        to_latex_args : {dict type}
            Dict of arguments to give to the DataFrame.to_latex method. See valid
            arguments at
            https://pandas.pydata.org/pandas-docs/stable/reference/api
            /pandas.DataFrame.to_latex.html
        path : {string or pathlib.Path type}
            Path to the .tex file to create
        label : {string type}
            Label to use for the table (callable by LateX's \\ref)
        caption : {string type}
            Caption to use for the table
        packages : {{string: {string:value}} type}
            Packages to use. Keys of first dict are the package names.
            values are dict of option: value options to use with the package. Can
            be empty if no options are to be specified.
        read_args : {dict type}
            Dict of argument to pass to the read_csv or read_excel method.
            Must contain at least \"filepath_or_buffer\" (for a csv) or \"oi\"
            (for an excel) argument.
        paperwidth : {int or float type}
            Width of the output table in the pdf
        paperheight : {int or float type}
            Height of the page of the output pdf. If table is too long to fit on
            the page, it will be split in several pages using longtable package.
        number : {int type}
            Number LateX should show after \"Table\". Default is 1.
        hide_numbering : {bool type}
            Do not show \"Table N\" in the caption.
        """
        
        self.__header = ""
        self.__body = "\\begin{document}\\end{document}"
        self.__footer = ""
        
        expected = ["data", "to_latex_args", "path", "label", "caption",
                    "packages", "read_args", "paperwidth", "paperheight",
                    "number", "hide_numbering"]
        for name in kwargs:
            if name not in expected:
                raise ValueError("Unexpected argument " + name)
        
        self.__data = kwargs.get("data", pd.DataFrame())
        self.__to_latex_args = kwargs.get("to_latex_args", {})
        self.__path = kwargs.get("path", None)
        self.__label = kwargs.get("label", None)
        self.__caption = kwargs.get("caption", None)
        self.__packages = kwargs.get("packages", {})
        read_args = kwargs.get("read_args", {})
        self.__paperwidth = kwargs.get("paperwidth", 0)
        self.__paperheight = kwargs.get("paperheight", 0)
        self.__number = kwargs.get("number", "1")
        self.__hide_numbering = kwargs.get("hide_numbering", False)
        
        self.__special_char = ["_", "^", "%", "&"]
        
        if self.__data is not None:
            if not isinstance(self.__data, pd.DataFrame):
                raise ValueError("Data must be a DataFrame")
        
        if not isinstance(self.__number, str):
            self.__number = str(int(self.__number))
        if self.__path is not None:
            if not isinstance(self.__path, Path):
                self.__path = Path(self.__path)
            if self.__path.suffix != ".tex":
                self.__path = self.__path.with_suffix(".tex")
        if len(read_args) > 0:
            self.load_from_file(read_args)

    def load_from_file(self, read_args):
        """
        Loads a table from a .csv or a .excel file
        
        Parameters
        ----------
        read_args: {dict}
            Arguments to pass to the read_csv or read_excel method.
        """
        
        if "path" in read_args:
            path = Path(read_args["path"])
            if path.suffix == ".csv":
                read_args["filepath_or_buffer"] = path
            elif path.suffix == ".xslx":
                read_args["io"] = path
            else:
                raise ValueError("Unkown extension " + path.suffix)
            del read_args["path"]
        
        if "filepath_or_buffer" in read_args:
            path = read_args["filepath_or_buffer"]
            if not isinstance(path, Path):
                path = Path(path)
            if not path.is_file():
                raise ValueError(str(path) + " file not found.")
            self.__data = pd.read_csv(**read_args)
        elif "io" in read_args:
            path = read_args["io"]
            if not isinstance(path, Path):
                path = Path(path)
            if not path.is_file():
                raise ValueError(str(path) + " file not found.")
            self.__data = pd.read_excel(**read_args)
        else:
            raise ValueError("\"filepath_or_buffer\" (for a csv) or \"io\""
                             " (for an excel) must be in read_args")

    # /////////////
    # // Setters //
    # /////////////

    def set_data(self, data):
        """
        Set content of the table.
        
        Parameters
        ----------
        data : {DataFrame type}
        """
        
        if not isinstance(self.__data, pd.DataFrame):
            raise ValueError("Argument \"data\" must be a pandas.DataFrame object.")
        self.__data = data

    def set_to_latex_args(self, args):
        self.__to_latex_args = args

    def set_path(self, path):
        if isinstance(path, str):
            path = Path(path)
        if path.suffix != ".tex":
            path = path.with_suffix(".tex")
        self.__path = path

    def set_label(self, label):
        self.__label = label

    def set_caption(self, caption):
        self.__caption = caption

    def set_packages(self, packages):
        self.__packages = packages

    def set_paperwidth(self, pw):
        self.__paperwidth = pw

    def set_paperheight(self, ph):
        self.__paperheight = ph

    def set_number(self, number):
        self.__number = number
        if not isinstance(self.__number, str):
            self.__number = str(int(self.__number))

    def set_hide_numbering(self, hn):
        self.__hide_numbering = hn

    def add_to_latex_arg(self, arg, value):
        self.__to_latex_args[arg] = value

    def add_package(self, package, options):
        self.__packages[package] = options

    # /////////////
    # // Getters //
    # /////////////

    def get_data(self):
        return deepcopy(self.__data)

    def get_path(self):
        return self.__path

    def get_label(self):
        return self.__label

    def get_caption(self):
        return self.__caption

    def get_packages(self):
        return deepcopy(self.__packages)

    def get_paperwidth(self):
        return self.__paperwidth

    def get_paperheight(self):
        return self.__paperheight

    def get_number(self):
        return self.__number

    def get_hide_numbering(self):
        return self.__hide_numbering

    # ////////////
    # // Makers //
    # ////////////

    def _make_header(self):
        """
        Makes the header of the tex file
        """
        
        TableWriter.printv("  Making Header...")
        # Try to guess a kind of optimal width for the table
        if self.__paperwidth == 0 and not self.__data.empty:
            charswidth = (len("".join(list(self.__data.columns.dropna())))
                          + max([len(ind) for ind in self.__data.index.dropna()])) * 0.178
            self.__paperwidth = charswidth + 0.8 * (len(self.__data.columns)) + 1
            if self.__paperwidth < 9:
                self.__paperwidth = 9
        # Same for height
        if self.__paperheight == 0 and not self.__data.empty:
            self.__paperheight = 3.5 + (len(self.__data.index)) * 0.45
            if self.__paperheight < 4:
                self.__paperheight = 4
            if self.__paperheight > 24:
                self.__paperheight = 24  # Limit page height to A4's 24 cm
        
        self.__header = "\\documentclass{article}\n"
        self.__header += ("\\usepackage[margin=0.5cm, paperwidth="
                          + str(self.__paperwidth) + "cm, paperheight="
                          + str(self.__paperheight) + "cm]{geometry}\n")
        self.__header += ("\\usepackage{caption}\n")
        
        lt = True
        if "longtable" in self.__to_latex_args:
            lt = self.__to_latex_args["longtable"]
        else:
            self.__to_latex_args["longtable"] = True
        if lt:
            self.__header += "\\usepackage{longtable}\n"
        
        self.__header += ("\\usepackage[dvipsnames]{xcolor}\n"
                          + "\\usepackage{booktabs}\n"
                          + "\\usepackage[utf8]{inputenc}\n")
        
        # Add specified packages if any
        for p in self.__packages:
            if len(self.__packages[p]) == 0:
                self.__header += "\\usepackage{" + p + "}\n"
            else:
                self.__header += "\\usepackage["
                for o in self.__packages[p]:
                    if self.__packages[p][o] is None:
                        self.__header += o + ","
                        
                    else:
                        self.__header += o + "=" + self.__packages[p][o] + ","
                self.__header = self.__header[:-1] + "]{" + p + "}\n"
        self.__header += ("\\begin{document}\n\\nonstopmode\n\\setcounter{table}{"
                          + self.__number + "}\n")
        
        TableWriter.printv("  ...done")

    def _make_body(self):
        """
        Makes the main body of tex file
        """
        
        TableWriter.printv("  Making Body...")
        if "column_format" not in self.__to_latex_args:
            self.__to_latex_args["column_format"] = (
                "|l|" + len(self.__data.columns) * "c" + "|")
        
        # Needed if you do not want long names to be truncated with "..."
        # by pandas, giving bullshit results in the .tex file
        def_max_col = pd.get_option('display.max_colwidth')
        if pd.__version__.split(".")[0] == "0":  # pandas is older than 1.0.0
            pd.set_option('display.max_colwidth', -1)
        else:  # pandas is 1.0.0 or newer
            pd.set_option('display.max_colwidth', None)
        
        if self.__data.empty:
            self.__body = self.__caption + ": Empty Dataframe\n"
            TableWriter.printv("  ...Dataframe is empty")
            return
        else:
            self.__body = self.__data.to_latex(**self.__to_latex_args)
        pd.set_option('display.max_colwidth', def_max_col)
        
        append_newline = False
        if self.__caption is not None:
            in_table = self.__body.find("\\toprule")
            pre_table = self.__body[:in_table]
            post_table = self.__body[in_table:]
            if not self.__hide_numbering:
                pre_table += "\\caption{" + self.__caption + "}\n"
            else:
                pre_table += "\\caption*{" + self.__caption + "}\n"
            self.__body = pre_table + post_table
            append_newline = True
        
        if self.__label is not None:
            in_table = self.__body.find("\\toprule")
            pre_table = self.__body[:in_table]
            post_table = self.__body[in_table:]
            pre_table += "\\label{" + self.__label + "}\n"
            self.__body = pre_table + post_table
            append_newline = True
        
        if append_newline:
            self.__body = self.__body.replace("\n\\toprule", "\\\\\n\\toprule")
        TableWriter.printv("  ...done")
        print(self.__body)

    def _make_footer(self):
        """
        Makes the footer of tex file
        """
        
        TableWriter.printv("  Making Footer...")
        self.__footer = ("\\end{document}\n")
        TableWriter.printv("  ...done")

    def _escape_special_chars(self, s):
        """ Will add '\\' before special characters outside of mathmode
        """

        if not isinstance(s, str):
            return s
        in_math = False
        previous_c = ""
        s2 = ""
        for c in s:
            if c == "$":
                in_math = not in_math
            if in_math:
                s2 += c
                previous_c = c
                continue
            if c in self.__special_char and not previous_c == "\\":
                c = "\\" + c
            previous_c = c
            s2 += c
        return s2

    # //////////////////
    # // Output files //
    # //////////////////

    def create_tex_file(self):
        """
        Create the tex file
        """
        
        if self.__path is None:
            raise ValueError("Must specify a file path.")
        
        TableWriter.printv("Creating .tex file at " + str(self.__path) + "...")
        with open(self.__path, "w") as outfile:
            # escape argument only works on column names. We need to apply it on
            # entier DataFrame, so do that then set it to False
            if "escape" in self.__to_latex_args:
                if self.__to_latex_args["escape"]:
                    self.__data.index = [self._escape_special_chars(s)
                                         for s in self.__data.index]
                    self.__data.columns = [self._escape_special_chars(s)
                                           for s in self.__data.columns]
                    self.__data = self.__data.applymap(self._escape_special_chars)
            self.__to_latex_args["escape"] = False
            self._make_header()
            outfile.write(self.__header)
            self._make_body()
            outfile.write(self.__body)
            self._make_footer()
            outfile.write(self.__footer)
        TableWriter.printv("...done")
    
    def compile(self, silenced=True, recreate=True,
                clean=True, clean_tex=False):
        """ Compile the pdf.
        
        Parameters
        ----------
        silenced : {bool type}
            Will or will not print on terminal the pdflatex output. Default True.
        recreate : {bool type}
            If False and .tex file exists, compile from it. If True, recreate
            the .tex file first.
        clean : {bool type}
            Removes all files created by the compilation which are not the .tex or
            the .pdf file.
        clean_tex : {bool type}
            Also removes the .tex file, leaving only the .pdf.
        """
        
        if self.__path is None:
            raise ValueError("Must specify a file path.")
        if recreate or not self.__path.is_file():
            self.create_tex_file()
        
        TableWriter.printv("Creating .pdf file from " + str(self.__path) + "...")
        if not self.__path.is_file():
            raise ValueError("Tex file " + str(self.__path) + " not found.")
        
        command = "pdflatex -synctex=1 -interaction=nonstopmode "
        parent = self.__path.parents[0]
        if parent != ".":
            command = command + "-output-directory=\"" + str(parent) + "\" "
        
        command = command + "\"" + str(self.__path) + "\""
        if silenced:  # unix
            if os.name == "posix":
                command = command + " > /dev/null"
            else:  # windows
                command = command + " > NUL"
        print(self.__body)
        TableWriter.printv(command)
        x = os.system(command)
        time.sleep(0.5)
        x = os.system(command)
        time.sleep(0.5)
        x = os.system(command)
        
        if x != 0:
            raise ValueError("Failed to compile pdf")
        TableWriter.printv("...done")
        
        if clean:
            self.clean(clean_tex)

    def clean(self, clean_tex=False):
        to_keep = [".pdf", ".csv", ".excel"]
        if not clean_tex:
            to_keep.append(".tex")
        files = list((self.__path.parent).glob(self.__path.stem + "*"))
        for f in files:
            if f.suffix not in to_keep:
                TableWriter.printv("Cleaning file " + str(f.name) + "...")
                f.unlink()


def remove_color(obj):
    """
    Remove coloration of given object.
    
    Parameters
    ----------
    obj : {string type}
           The object from which to remove the color
    
    Return
    ------
    {string type}
    Object without color
    """
    
    if "\\textcolor{" not in obj:
        return obj
    to_find = "\\textcolor{"
    before_color = obj[:obj.find(to_find)]
    after_color = obj[obj.find("textcolor") + 10:]
    no_color = after_color[after_color.find("{") + 1:].replace("}", "", 1)
    return before_color + no_color


def set_color(obj, color):
    """
    Add color to a given object.
    
    Parameters
    ----------
    obj : {any type}
          The object from which to remove the color. Must be castable to string.
    color : {string type}
            Must be a valid LateX color string
    
    Return
    ------
    {string type}
        Object with color
    """
    if pd.isna(obj):
        return obj
    return "\\textcolor{" + color + "}{" + str(obj) + "}"


def set_color_dataframe(df, color, index=False, columns=False):
    """
    Sets color for the entier DataFrame's or Series's entries
    
    To change the color of some elements in the dataframe under some condition,
    do:
    
    dff = dff.mask(dff < 0, TableWriter.set_color_dataframe(dff, "red"))
    dff = pd.DataFrame(columns=dff.columns,
                       index=dff.index,
                       data=dff.values.astype(str))
    dff = dff.mask(dff == "nan", "")
    writer = TableWriter(data=dff)
    
    Parameters
    ----------
    df : {DataFrame or Series type}
         The DataFrame or Series to change the colors of
    
    color: {String type}, default ''
            LateX-recognized color string
    Return
    ------
    {DataFrame type} Colored DataFrame or Series (content will be string)
    """
    if isinstance(df, pd.DataFrame):
        df_c = df.applymap(lambda x: set_color(x, color))
    else:
        df_c = df.apply(lambda x: set_color(x, color))
    if index:
        df_c.index = [set_color(x, color) for x in df_c.index]
    if columns:
        df_c.columns = [set_color(x, color) for x in df_c.columns]
    return df_c
