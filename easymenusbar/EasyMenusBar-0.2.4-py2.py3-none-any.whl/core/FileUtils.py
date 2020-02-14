import os

from typing import List
import rx
import shutil
import sys


class FileUtils:
    def createDir(self, path, name):
        os.mkdir(os.path.join(path, name))

    def deleteDir(self, path):
        if os.path.exists(path) and os.path.isdir(path):
            shutil.rmtree(path)

    def getProjectPath(self):
        return os.path.dirname(sys.argv[0])

    def createFile(self, path, name, default: List = None):
        with open(os.path.join(path, name), mode='w') as file:
            if default:
                for item in default:
                    if not item.endswith("\n\n"):
                        item = item + "\n\n"
                    file.write(item)
            print(file.name)

    def updateFile(self, filePath: str, content) -> rx.Observable:
        _filePath = filePath
        _data = content

        def _createObserver(subscription, scheduler):
            with open(_filePath, mode='w') as f:
                f.write(_data)
            subscription.on_completed()

        return rx.create(_createObserver)

    def deleteFile(self, name):
        if os.path.exists(name) and os.path.isfile(name):
            os.remove(name)
