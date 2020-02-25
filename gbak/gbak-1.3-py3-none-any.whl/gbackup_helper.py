from gbackup import Client

def upload(config,input):
    c = Client(config, "upload", input, "")
    c.run()
def download(config,input,output):
    c = Client(config, "download", input, output)
    c.run()