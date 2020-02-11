# coding=utf-8
from __future__ import absolute_import, print_function

from suanpan import path, runtime
from suanpan.arguments import Arg
from suanpan.components import Result
from suanpan.storage import storage
from suanpan.utils import csv, excel, image, json, npy, text


class StorageArg(Arg):
    def getOutputTmpValue(self, *args):
        return storage.delimiter.join(args)


class File(StorageArg):
    FILENAME = "file"
    FILETYPE = None

    def __init__(self, key, **kwargs):
        fileName = kwargs.pop("name", self.FILENAME)
        fileType = kwargs.pop("type", self.FILETYPE)
        self.fileName = f"{fileName}.{fileType.lower()}" if fileType else fileName
        self.objectPrefix = None
        self.objectName = None
        self.filePath = None
        super(File, self).__init__(key, **kwargs)

    @property
    def isSet(self):
        return True

    def reset(self):
        self.objectPrefix = None
        self.objectName = None
        self.filePath = None
        return super(File, self).reset()

    def load(self, args):
        self.objectPrefix = super(File, self).load(args)
        if self.objectPrefix:
            self.objectName = storage.storagePathJoin(self.objectPrefix, self.fileName)
            self.filePath = storage.getPathInTempStore(self.objectName)
            path.safeMkdirsForFile(self.filePath)
        self.value = self.filePath
        return self.filePath

    def format(self, context):
        if self.filePath:
            _download = (
                storage.download if self.required else runtime.saferun(storage.download)
            )
            _download(self.objectName, self.filePath)
        return self.filePath

    def clean(self, context):
        if self.filePath:
            path.remove(self.filePath)
        return self.filePath

    def save(self, context, result):
        filePath = result.value
        storage.upload(self.objectName, filePath)
        self.logSaved(self.objectName)
        return self.objectPrefix


class Folder(StorageArg):
    def __init__(self, key, **kwargs):
        super(Folder, self).__init__(key, **kwargs)
        self.folderName = None
        self.folderPath = None

    @property
    def isSet(self):
        return True

    def reset(self):
        self.folderName = None
        self.folderPath = None
        return super(Folder, self).reset()

    def load(self, args):
        self.folderName = super(Folder, self).load(args)
        if self.folderName:
            self.folderPath = storage.getPathInTempStore(self.folderName)
        if self.folderPath:
            path.safeMkdirs(self.folderPath)
        self.value = self.folderPath
        return self.folderPath

    def format(self, context):
        if self.folderPath:
            _download = (
                storage.download if self.required else runtime.saferun(storage.download)
            )
            _download(self.folderName, self.folderPath)
        return self.folderPath

    def clean(self, context):
        if self.folderPath:
            path.empty(self.folderPath)
        return self.folderPath

    def save(self, context, result):
        folderPath = result.value
        storage.upload(self.folderName, folderPath)
        self.logSaved(self.folderName)
        return self.folderName


class Data(File):
    FILENAME = "data"


class Json(Data):
    FILETYPE = "json"

    def format(self, context):
        super(Json, self).format(context)
        if self.filePath:
            _load = json.load if self.required else runtime.saferun(json.load)
            self.value = _load(self.filePath)
        return self.value

    def save(self, context, result):
        json.dump(result.value, self.filePath)
        return super(Json, self).save(context, Result.froms(value=self.filePath))


class Csv(Data):
    FILETYPE = "csv"

    def cleanParams(self, params):
        params = super(Csv, self).cleanParams(params)
        return {k: v for k, v in params.items() if k not in ("table", "partition")}

    def format(self, context):
        super(Csv, self).format(context)
        if self.filePath:
            _load = csv.load if self.required else runtime.saferun(csv.load)
            self.value = _load(self.filePath)
        return self.value

    def save(self, context, result):
        csv.dump(result.value, self.filePath)
        return super(Csv, self).save(context, Result.froms(value=self.filePath))


class Table(Csv):
    pass


class Excel(Data):
    FILETYPE = "xlsx"
    LEGACY_FILETYPE = "xls"

    def __init__(self, key, **kwargs):
        self.fileTypeSet = kwargs.get("type") is not None
        super(Excel, self).__init__(key, **kwargs)

    def load(self, args):
        super(Excel, self).load(args)
        if not storage.isFile(self.objectName) and not self.fileTypeSet:
            fileType = self.LEGACY_FILETYPE
            self.fileName = "{}.{}".format(self.fileName.split(".")[0], fileType)
            self.objectName = storage.storagePathJoin(self.objectPrefix, self.fileName)
        self.filePath = storage.getPathInTempStore(self.objectName)
        path.safeMkdirsForFile(self.filePath)
        self.value = self.filePath
        return self.filePath

    def format(self, context):
        super(Excel, self).format(context)
        if self.filePath:
            _load = excel.load if self.required else runtime.saferun(excel.load)
            self.value = _load(self.filePath)
        return self.value

    def save(self, context, result):
        excel.dump(result.value, self.filePath)
        return super(Excel, self).save(context, Result.froms(value=self.filePath))


class Npy(Data):
    FILETYPE = "npy"

    def format(self, context):
        super(Npy, self).format(context)
        if self.filePath:
            _load = npy.load if self.required else runtime.saferun(npy.load)
            self.value = _load(self.filePath)
        return self.value

    def save(self, context, result):
        npy.dump(result.value, self.filePath)
        return super(Npy, self).save(context, Result.froms(value=self.filePath))


class String(Data):
    FILETYPE = "txt"

    def format(self, context):
        super(String, self).format(context)
        if self.filePath:
            _load = text.load if self.required else runtime.saferun(text.load)
            self.value = _load(self.filePath)
        return self.value

    def save(self, context, result):
        text.dump(result.value, self.filePath)
        return super(String, self).save(context, Result.froms(value=self.filePath))


class Visual(String):
    FILENAME = "part-00000"
    FILETYPE = ""


class Model(File):
    FILENAME = "model"


class H5Model(Model):
    FILETYPE = "h5"


class Checkpoint(Model):
    FILETYPE = "ckpt"


class JsonModel(Model):
    FILETYPE = "json"


class Image(File):
    FILENAME = "image"
    FILETYPE = "png"

    def format(self, context):
        super(Image, self).format(context)
        if self.filePath:
            _read = image.read if self.required else runtime.saferun(image.read)
            self.value = _read(self.filePath)
        return self.value

    def save(self, context, result):
        image.save(result.value, self.filePath)
        return super(Image, self).save(context, Result.froms(value=self.filePath))


class Screenshots(Image):
    FILENAME = "screenshots"
