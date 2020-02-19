import subprocess
import argparse
import logging
import threading
import time
import io
import time
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor


def thread_function(cmd):
    subprocess.call(cmd,shell=True)

def run_parallel(creds,base_cmd,sshpass):
    executor = ThreadPoolExecutor(len(creds))
    futures = []
    for (ip,password) in creds:
        cmd = "{} -p {} ssh -o \"UserKnownHostsFile=/dev/null\" -o \"StrictHostKeyChecking=no\" {} \"{}\"".format(sshpass,password,ip,base_cmd)
        future = executor.submit(thread_function, (cmd))
        futures.append(future)

    for future in futures:
        print(future.result())


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

    args.command =  '\"'.join(args.command.split('"'))
    if args.parallel:
        run_parallel(creds,args.command,sshpass)
    else:
        print("----- {} -----".format(ip))
        subprocess.call("{} -p {} ssh -o \"UserKnownHostsFile=/dev/null\" -o \"StrictHostKeyChecking=no\" {} \"{}\"".format(sshpass,password,ip,args.command),shell=True)

main()