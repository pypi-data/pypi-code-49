import pandas as pd
import os
import json
from typing import List, Callable
from multiprocessing import Lock, Pool, Manager
from functools import partial
from queue import Empty
from simple_salesforce import Salesforce
from dotenv import load_dotenv
from pathlib import Path
from datetime import datetime


def print_error(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            print(str(e))
    return wrapper


def strtime() -> str:
    return datetime.now().strftime('%Y_%m_%d_%H_%M_%S')


def write_results(filename: str,
                  data: List[dict],
                  lock: Lock = None,
                  ) -> None:
    fn = f'~/Downloads/{filename}.csv'
    df = pd.DataFrame.from_dict(data)
    if lock:
        lock.acquire()
    if not os.path.isfile(fn):
        df.to_csv(fn, encoding='utf-8', index=False)
    else:
        df.to_csv(filename, mode='a', header=False, encoding='utf-8', index=False)
    if lock:
        lock.release()


def _add_attributes(
                    data: dict,
                    object_name: str,
                    ref_id: str = None
                    ) -> dict:
    ta = {'type':object_name}
    attr = {**ta, **{'referenceId': ref_id}} if ref_id else ta
    return {**data, **{'attributes': attr}}


def _bulk_change(success_lock: Lock,
                 failure_lock: Lock,
                 object_name: str,
                 method: str,
                 session: Salesforce,
                 url: str,
                 results_file_name: str,
                 recs: List[dict],
                 ) -> None:
    recs = [_add_attributes(r, object_name) for r in recs]
    load = {'allOrNone':False,'records':recs}
    results = session._call_salesforce(method=method,
                                       url=url,
                                       data=json.dumps(load)).json()
    merged = [{**recs[i], **results[i]} for i in range(len(results))]
    successes = [r for r in merged if r.get('success') == True]
    failures = [r for r in merged if r.get('success') == False]
    if successes:
        success_file_name = f'{results_file_name}_successes'
        write_results(success_file_name, successes, success_lock)
    if failures:
        failure_file_name = f'{results_file_name}_failures'
        write_results(failure_file_name, failures, failures)


def _bulk_delete(success_lock: Lock,
                 failure_lock: Lock,
                 session: Salesforce,
                 url: str,
                 results_file_name: str,
                 recs: List[dict],
                 ) -> None:
    ids = [r['id'] for r in recs]
    id_url = f"{url}?ids={','.join(ids)}&allOrNone=false"
    results = session._call_salesforce(method='DELETE',
                                       url=id_url).json()
    successes = [r for r in results if r.get('success') == True]
    failures = [r for r in results if r.get('success') == False]
    if successes:
        success_file_name = f'successes_{results_file_name}'
        write_results(success_file_name, successes, success_lock)
    if failures:
        failure_file_name = f'failures_{results_file_name}'
        write_results(failure_file_name, failures, failures)


def _read_and_chunk(file_name: str) -> List[List[dict]]:
    df = pd.read_csv(file_name)
    df.columns = map(str.lower, df.columns)
    data = df.to_dict('records')
    chunks = (data[i : i+200] for i in range(0, len(data), 200))
    return chunks


def _gen_file_name(file_name: str) -> str:
    sp_fn = file_name.split('/')
    name = sp_fn[len(sp_fn)-1]
    results_file_name = f'{name[:-4]}_{strtime()}'
    return results_file_name


def _bulk_operation(func: partial,
                    chunks: List[List[dict]],
                    threads: int
                    ) -> None:
    try:
        pool = Pool(threads)
        pool.map(func, chunks)
    finally:
        pool.close()
        pool.join()


def bulk_delete(args: str, session: Salesforce, base_url: str, threads: int) -> None:
    url = f'{base_url}/composite/sobjects/'
    arg_list = args.split(' ')
    file_name = arg_list[0]
    chunks = _read_and_chunk(file_name)
    results_file_name = _gen_file_name(file_name)
    m = Manager()
    func = partial(_bulk_delete,
                   m.Lock(),
                   m.Lock(),
                   session,
                   url,
                   results_file_name)
    _bulk_operation(func, chunks, threads)


def bulk_change(args: str,
                method: str,
                session: Salesforce,
                base_url: str,
                threads: int
                ) -> None:
    url = f'{base_url}/composite/sobjects/'
    arg_list = args.split()
    object_name = arg_list[0]
    file_name = arg_list[1]
    chunks = _read_and_chunk(file_name)
    results_file_name = _gen_file_name(file_name)
    m = Manager()
    func = partial(_bulk_change,
                    m.Lock(),
                    m.Lock(),
                    object_name,
                    method,
                    session,
                    url,
                    results_file_name)
    _bulk_operation(func, chunks, threads)


def _get_os_var(var: str, suffix: str) -> str:
    base = f'SALESFORCE_{var}'
    var = f'{base}_{suffix.upper()}' if suffix != 'default' else base
    return os.getenv(var)


def start_session(version: float, env_suffix: str) -> (Salesforce, str):
    env_path = os.path.expanduser('~/.env')
    load_dotenv(dotenv_path=env_path)
    un = _get_os_var('USERNAME', env_suffix)
    pw = _get_os_var('PASSWORD', env_suffix)
    st = _get_os_var('SECURITY_TOKEN', env_suffix)
    dm = _get_os_var('DOMAIN', env_suffix)
    if not (un and pw and st):
        raise Exception(f'{env_suffix} username, password or security token variables not set')
    return Salesforce(username=un, password=pw, security_token=st, domain=dm, version=version), dm
