import tripgoparserv2 as tgp
import pandas as pd
import logging
import os
from functools import partial
from multiprocessing.pool import Pool
import multiprocessing
from time import time

# Needs rewrite for git upload
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger('requests').setLevel(logging.CRITICAL)
logger = logging.getLogger(__name__)

def getCompiledResults(i):
    csv = pd.read_csv('70120.csv')
    jsonData = tgp.openJson(csv.tripid[i], str(int(csv.startime[i]))).open()
    data = tgp.ODPair(jsonData, csv.tripid[i], str(int(csv.startime[i]))).compiled_results
    
    return data


def main():
    ts = time()
    
    with Pool(processes=4) as pool:
        results = pool.map(getCompiledResults, range(10000))
        df = pd.DataFrame(results)
        df.to_csv('tester.csv')


    logging.info('Took %s seconds', time() - ts)
    
if __name__ == "__main__":
    main()

