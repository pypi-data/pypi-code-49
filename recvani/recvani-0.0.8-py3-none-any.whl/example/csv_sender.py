from recvani.rv_client import rv_client
from recvani.rv_requests import simple_interaction, batch_interaction
import multiprocessing
import os
import time 
from config import *
import sys

def _send(arr):
    batch_interactions = [batch_interaction(arr[i:i+mbatch]) for i in range(0, len(arr), mbatch)]
    rc  = rv_client(API_KEY, MODEL,  SECRET_KEY)
    for interactions in batch_interactions:
        rc.send(interactions)
    
def send(arr):
    mp = multiprocessing.Process(target=_send, args=(arr,)) 
    mp.start()
    return mp

def send_file(fname):
    print ("Reading file " +  fname)
    fstream = open(fname)
    arr = []
    threads = []
    for line in fstream:
        vec = line.strip().split(",")
        si = simple_interaction(vec[0], vec[1], float(vec[2]), int(time.time()))
        arr.append(si)
        if (len(arr) == bsize):
            threads.append(send(arr))
            arr = []
        if (len(threads) == no_of_process):
            for thread in threads:
                thread.join()
            threads = []
    
    send(arr)
    fstream.close()

def main():
    if (len(sys.argv) < 2):
        print("Please provide the directory for csv")
        exit(0)
    directory = sys.argv[1]
    
    files = os.listdir(directory)
    files = [os.path.join(directory, f) for f in files]
    for f in files:
        send_file(f)

if __name__ == '__main__':
    main()
