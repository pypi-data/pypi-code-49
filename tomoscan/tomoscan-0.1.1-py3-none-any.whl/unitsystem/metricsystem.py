# coding: utf-8
# /*##########################################################################
#
# Copyright (c) 2016-2020 European Synchrotron Radiation Facility
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# ###########################################################################*/
__authors__ = ["H. Payno"]
__license__ = "MIT"
__date__ = "01/09/2016"


from typing import Union

meter = 1.0
m = meter


centimeter = meter / 100.0
cm = centimeter

millimeter = 0.1 * centimeter
mm = millimeter

micrometer = 1e-6 * meter

nanometer = 1e-9 * meter
nm = nanometer

mm2 = millimeter * millimeter
cm2 = centimeter * centimeter
m2 = meter * meter


def getUnitName(value: Union[float, int]) -> str:
    """
    :return: name in (None, nm, cm, m, mm) from the given unit
    """
    if value == nanometer:
        return 'nm'
    if value == millimeter:
        return 'mm'
    if value == centimeter:
        return 'cm'
    if value == meter:
        return 'm'
    return None


