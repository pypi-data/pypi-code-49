import wget,fire
import requests,json,os,shutil,glob
class Remote:
    def __init__(self,server_url='http://wangpeii.com/post_and_download'):
        self.server_url=server_url
        self.download_url=self.server_url+'/download'
    def download(self,path,out=None,bar=None):
        url=self.download_url+'/'+path
        if not out:
            out=os.path.basename(path)
        if not bar:
            wget.download(url, out)
        wget.download(url,out,bar)
    def request(self,url,server_url=None):
        server_url=server_url or self.server_url
        data={'url':url}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url=server_url, headers=headers, data=json.dumps(data))
        print(response.text)
        return response

if __name__ == '__main__':
    ft=Remote('http://192.168.1.7/post_and_download')
    ft.request('https://csdnimg.cn/public/favicon.ico')
    ft.download('favicon.ico')