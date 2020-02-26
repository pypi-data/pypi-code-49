from aiofile import AIOFile, LineReader


class Reader:
    def __init__(self):
        return

    async def _async_read(self, file_path):
        async with AIOFile(file_path, "r") as afp:
            return await afp.read()

    def read(self, file_path):
        reader = open(file_path,'r')
        data = reader.read()
        reader.close()
        return data
    
    def read_line(self, file_path):
        reader = open(file_path,'r')
        return reader
