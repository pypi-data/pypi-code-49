from recvani.rv_client import rv_client
from recvani.rv_requests import simple_interaction
from config import *
import time

def main():
    si = simple_interaction("USER1", "STORY1", 1.0, int(time.time()))
    rc  = rv_client(API_KEY, MODEL,  SECRET_KEY)
    print(rc.send(si))

if __name__ == '__main__':
    main()
