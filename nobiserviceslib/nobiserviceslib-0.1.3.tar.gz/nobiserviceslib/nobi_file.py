import csv
import os


def check_fmt(filename):
    return os.path.basename(filename).split('.')[-1]


def read_csv(filename, ignore_first_line=False):
    result = []
    with open(filename ,'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            result.append(row)
    return result if not ignore_first_line else result[1:]


def strlist_to_floatlist(strlist):
    return [float(i) for i in strlist]
