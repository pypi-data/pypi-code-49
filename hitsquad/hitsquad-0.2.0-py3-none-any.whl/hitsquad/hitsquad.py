import subprocess
import argparse
import logging
import threading
import time
import io
import time
import subprocess
import sys


def thread_function(cmd):
    subprocess.call(cmd,shell=True)

def run_parallel(creds,cmd,sshpass):
    print(cmd)
    threads = []
    for (ip,password) in creds:
        cmd = "{} -p {} ssh {} {}".format(sshpass,password,ip,cmd)
        x = threading.Thread(target=thread_function, args=(cmd,))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        thread.join()

def main(): 
    parser = argparse.ArgumentParser(prog ='hitsquad', 
                                     description ='sshpass based stuff') 
    parser.add_argument('--ipfile', help='file with <user@ip or ip,pass> pairs on different rows',required=True)
    parser.add_argument('--parallel',dest='parallel', action='store_const',const=True, default=False, help='parallelize over threads')
    parser.add_argument('--command', help='command to run')
    args = parser.parse_args()
    sshpass = "/".join(__file__.split("/")[:-1])+"/sshpass"
    f = open(args.ipfile,"r")
    creds = []
    for row in f.readlines():
        if not row:
            continue
        print(row)
        (ip,password) = row.strip().split(",")
        creds.append((ip,password))
    
    if args.parallel:
        run_parallel(creds,args.command,sshpass)
    else:
        print("----- {} -----".format(ip))
        subprocess.call("{} -p {} ssh {} {}".format(sshpass,password,ip,args.command),shell=True)

main()