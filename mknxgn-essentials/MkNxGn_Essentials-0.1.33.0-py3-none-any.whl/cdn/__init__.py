import requests, os

def DownloadDatastore(filedir, is_dir=False, SERVER="https://cdn.mknxgn.pro/datastore/"):
    print("MkNxGn CDN - GET: " + filedir)
    resp = requests.get(url=SERVER + "GET/" + filedir, stream=True)
    if resp.status_code == 200:
        if 'is_dir' in resp.headers:
            print("Downloading Directory:", filedir)
            files = resp.json()
            for file in files:
                path = os.path.split(file)[0]
                os.makedirs(path, exist_ok=True)
                DownloadDatastore(file, is_dir=True)
            print("DIR DOWNLOAD: OK")
        else:
            filesize = int(resp.headers['file_size'])
            if is_dir == False:
                filedir = os.path.split(filedir)[1]
            with open(filedir, "wb") as file:
                i = 0
                for chunk in resp.iter_content(chunk_size=500):
                    if chunk:
                        i += len(chunk)
                        file.write(chunk)
                        print(("Downloading: " + "█"*(int((i*40)/filesize))).ljust(54) + (str(round(i*0.000001, 3)).ljust(6, "0") + "/" + str(round(filesize*0.000001, 3)).ljust(6, "0") + " MB ") + "STATUS: DOWNLOADING", end="\r")
            print(("Downloading: " + "█"*(int((i*40)/filesize))).ljust(54) + (str(round(i*0.000001, 3)).ljust(6, "0") + "/" + str(round(filesize*0.000001, 3)).ljust(6, "0") + " MB ") + "STATUS: OK                     ")
    else:
        print("FAILED")