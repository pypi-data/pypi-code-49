from glob import glob
from itertools import cycle, islice
from os import mkdir
from os import path as pth
from math import atan, sin
from shutil import rmtree
from subprocess import call
from sys import argv
from time import time_ns, time
from pydub import AudioSegment, utils
from skein import skein512


def mds(no):
    nn = no ** 2
    return nn % (10 ** no)


def handle_video(path):
    sfp = pth.dirname(path)
    arr = []
    cmd = "scenedetect -i {0} -o {1} -q detect-content save-images"\
        .format(path, sfp + r"\del\\")
    call(cmd)
    for x in glob(sfp + r"\del\*.jpg"):
        with open(x, "rb") as h:
            arr.append(int(skein512(h.read()).hexdigest(), 16))
            h.close()
    return arr


def handle_audio(path, interval):
    aud = AudioSegment.from_file(path, 'mp4')
    p = pth.dirname(path)
    chunks = utils.make_chunks(aud, interval * 1000)
    arr = []
    for i, c in enumerate(chunks):
        c.export(p + r"\del\{0}.wav".format(i), format="wav")
    for x in glob(p + r"\del\*wav"):
        with open(x, "rb") as y:
            arr.append(int(skein512(y.read()).hexdigest(), 16))
    return arr


def return_all(path, ai=1, cs=17):
    """Main AVRNG function. Arguments: path, extraction interval, output length."""
    p = pth.dirname(path) + r"\del\\"
    if not pth.exists(p):
        mkdir(p)
    video = handle_video(path)
    audio = handle_audio(path, ai)
    time = skein512(str(time_ns()).encode('utf-8')).hexdigest()
    lg = max([video, audio], key=len)
    sh = min([audio, video], key=len)
    sh = list(islice(cycle(sh), len(lg)))
    time = [int(x, 16) for x in list(islice(cycle(time), len(lg)))]
    nos = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0,
           "7": 0, "8": 0, "9": 0}
    amts = {}
    r = []
    for i, x in enumerate(sh):
        a = list("".join(str(e + f + g) for e, f, g in zip(lg, sh, time)))
        for c in a:
            nos[c] += 1
        r += a
    sor = sorted(nos, key=nos.get, reverse=True)
    st = sor[5:]
    la = sor[:5]
    for i, x in enumerate(st):
        if int(la[4 - i]) != 0:
            amts[x] = nos[x] / int(la[4 - i])
    for a in r:
        n = sin(atan(mds(int(a))))
        for i, c in enumerate(a):
            if c in amts and abs(n - amts[c]) < 0.5:
                a[i] = str(9 - int(c))
    r = "".join([str(x) for x in r])
    r = [r[i:i + cs] for i in range(0, len(r), cs)]
    rmtree(p)
    with open(pth.dirname(path) + r"\output.txt", "w+") as x:
        for a in r:
            x.write(f"{a}\n")
    return r


if __name__ == "__main__":
    st = time()
    arr = return_all(argv[1], int(argv[2]), int(argv[3]))
    print(arr)
    print("Completed in " + str(time() - st) + " seconds.")
