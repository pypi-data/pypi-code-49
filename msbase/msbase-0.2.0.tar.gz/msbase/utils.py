import json
import jsonlines
import time
import os

def load_json(path: str):
    with open(path, "r") as f:
        s = f.read()
        try:
            return json.loads(s)
        except json.decoder.JSONDecodeError:
            return json.loads(s.encode().decode('utf-8-sig'))

def write_json(stuff, path: str):
    with open(path, 'w') as f:
        f.write(json.dumps(stuff, sort_keys=True))

def write_pretty_json(stuff, path: str):
    with open(path, 'w') as f:
        f.write(json.dumps(stuff, indent=4, sort_keys=True))

def append_pretty_json(stuff, path: str):
    with jsonlines.open(path, mode='a') as f:
        f.write(stuff)

def datetime_str():
    return time.strftime("%Y-%m-%dT%H:%M:%SZ")

def load_jsonl(path: str):
    with jsonlines.open(path) as reader:
        return [obj for obj in reader]

def file_size(path: str):
    return os.stat(path).st_size

def file_size_mb(path: str):
    return file_size(path) / 1024.0  / 1024.0

def find_files(dirpath, file_ext=None, dir_ext=None):
    for root, dirs, files in os.walk(dirpath, followlinks=True):
        if file_ext:
            for f in files:
                if f.endswith(file_ext):
                     yield os.path.join(root, f)
        if dir_ext:
            for d in dirs:
                if d.endswith(dir_ext):
                     yield os.path.join(root, d)

def unzip(ijs):
    return [ i for i, j in ijs ], [ j for i, j in ijs ]

def sha256sum(apk_path):
    stdout, _, _ = try_call_std(["sha256sum", apk_path])
    return stdout.split()[0].strip()

