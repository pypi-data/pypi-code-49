import os
import subprocess

url = "http://yann.lecun.com/exdb/mnist/"

files = [
    "train-images-idx3-ubyte.gz",
    "train-labels-idx1-ubyte.gz",
    "t10k-images-idx3-ubyte.gz",
    "t10k-labels-idx1-ubyte.gz",
]


def raw(raw_dir):
    raw_dir = os.path.realpath(raw_dir)
    if not os.path.exists(raw_dir):
        os.makedirs(raw_dir)
    cwd = os.getcwd()
    os.chdir(raw_dir)
    for f in files:
        curl_out = subprocess.Popen('curl {} -O'.format(url + f).split(' '),
                                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        curl_stdout, curl_stderr = curl_out.communicate()
        print(curl_stdout.decode('utf-8'))
        if curl_stderr is not None:
            print(curl_stderr.decode('utf-8'))

        gunzip_out = subprocess.Popen('gunzip {}'.format(f).split(' '),
                                      stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        gunzip_stdout, gunzip_stderr = gunzip_out.communicate()
        print(gunzip_stdout.decode('utf-8'))
        if gunzip_stderr is not None:
            print(gunzip_stderr.decode('utf-8'))
    os.chdir(cwd)
