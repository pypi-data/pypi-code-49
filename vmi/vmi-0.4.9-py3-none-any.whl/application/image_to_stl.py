import hashlib
import json
import pathlib
import pickle
import threading
import requests
from typing import Dict, Any

import gridfs
import pydicom
import pymongo
import vtk
import nibabel as nib

import vmi

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtWidgets import QInputDialog


def from_image_to_stl(uid=None):
    if uid is not None:
        # 获取图像信息
        search_dict = {'SeriesInstanceUID': uid}
        md5_key = image_data_db.find_one(search_dict)
        data_image = image_file_db.find_one({'md5': md5_key['predicted_md5'][-1]})

        # 保存图像文件
        file_name = md5_key['file_name']
        save_file = open(file_name, 'wb')
        save_file.write(data_image.read())
        save_file.close()

        # 读取图像文件
        reader = vtk.vtkNIFTIImageReader()
        reader.SetFileName(file_name)
        reader.Update()
        pelvis_image = reader.GetOutput()

        # 等值面提取
        pd = vmi.imIsosurface(pelvis_image, 1)

        # 保存STL文件
        stl_filename = uid + '.stl'
        w = vtk.vtkSTLWriter()
        w.SetInputData(pd)
        w.SetFileName(stl_filename)
        w.SetFileTypeToBinary()
        w.Update()

        # 上传STL文件
        stl_file = open(stl_filename, 'rb')
        file_data = stl_file.read()
        model_md5 = hashlib.md5(file_data).hexdigest()

        if not model_file_db.exists({'md5': model_md5}):
            file_id = model_file_db.put(file_data, fileType='.stl', filename=stl_filename, SeriesInstanceUID=uid)

            # 检查上传结果是否与本地一致
            if model_file_db.find_one({'_id': file_id}).md5 != model_md5:
                model_file_db.delete(file_id)
                return print('文件上传失败')
            else:
                # 替换旧数据,增加STL数据的md5
                if not model_data_db.find_one(search_dict):
                    model_data_db.insert_one(search_dict)

                key_data_dict = model_data_db.find_one(search_dict)
                value_data_dict = {**key_data_dict, 'filename': stl_filename, 'model_md5': model_md5}
                model_data_db.find_one_and_replace(key_data_dict, value_data_dict)

        return pd


def return_globals():
    return globals()


if __name__ == '__main__':
    client = pymongo.MongoClient('mongodb://root:medraw123@192.168.11.122:27017/admin', 27017)

    image_data_db: pymongo.collection.Collection = client.testDB.spinePelvis_Predict
    image_file_db = gridfs.GridFS(client.testDB, collection='spinePelvis_Predict')

    model_data_db: pymongo.collection.Collection = client.testDB.spinePelvis_Model
    model_file_db = gridfs.GridFS(client.testDB, collection='spinePelvis_Model')

    view = vmi.View()

    data = from_image_to_stl("1.2.840.113704.1.111.8820.1476174747.11")

    pelvis_prop = vmi.PolyActor(view)
    pelvis_prop.setData(data)
    view.setCamera_FitAll()

    main = vmi.Main(return_globals)
    main.setAppName('image_to_stl')
    main.setAppVersion(vmi.version)
    main.excludeKeys += ['main']

    main.layout().addWidget(view, 0, 0, 1, 1)
    vmi.appexec(main)  # 执行主窗口程序
    vmi.appexit()  # 清理并退出程序
