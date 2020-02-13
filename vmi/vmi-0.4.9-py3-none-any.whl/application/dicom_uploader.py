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
import base64

import vmi

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtWidgets import QInputDialog


def input_dicom():
    global series_list
    dcmdir = vmi.askDirectory('DICOM')

    if dcmdir is not None:
        series_list = vmi.sortSeries(dcmdir)
        input_series()


def input_series():
    global series_dict
    series = vmi.askSeries(series_list)
    if series is not None:
        series_dict = series.toKeywordValue()
        input_image(series.read())


def input_image(image: vtk.vtkImageData):
    series_volume.setData(image)
    series_view.setCamera_FitAll()
    series_view.updateAtOnce()
    vmi.appupdate()


def update_series_opcity():
    series_volume.setOpacityScalar({series_opacity_range[0] - 1: 0,
                                    series_opacity_range[0]: 1,
                                    series_opacity_range[1]: 1,
                                    series_opacity_range[1] + 1: 0})
    series_volume.setColor({series_opacity_range[0]: [1, 1, 0.9],
                            series_opacity_range[1]: [1, 1, 0.1]})


def output_nifti():
    if series_dict:
        vmi.imSaveFile_NIFTI(series_volume.data())


def upload(image: vtk.vtkImageData, kw_value: Dict[str, Any]):
    data_id = ''

    def func():
        # 图像序列化为文件，计算特征码
        vmi.setPickleNIFTI_gz(False)
        image_bytes = pickle.dumps(image)
        image_md5 = hashlib.md5(image_bytes).hexdigest()

        # 上传文件，避免重复上传完全一样的文件
        if not file_db.exists({'SeriesInstanceUID': kw_value['SeriesInstanceUID']}):
            file_id = file_db.put(image_bytes,
                                  fileType='.nii',
                                  scalarType=image.GetScalarTypeAsString(),
                                  SeriesInstanceUID=kw_value['SeriesInstanceUID'])
            # 检查上传结果是否与本地一致
            if file_db.find_one({'_id': file_id}).md5 != image_md5:
                file_db.delete(file_id)
                return print('远端MD5校验失败 {}'.format(repr(kw_value)))

        # 数据项，引用图像文件特征码
        data_dict = {**kw_value}

        # 上传数据项，避免重复上传完全一样的数据项
        nonlocal data_id
        data_one = data_db.find_one(data_dict)
        if data_one is None:
            data_one = data_db.insert_one(data_dict)
            data_id = data_one.inserted_id
        else:
            data_id = data_one['_id']

    t = threading.Thread(target=func)
    t.start()
    vmi.appwait(t)
    return data_id


def output_upload():
    # 标注信息
    label = [QLabel('医生姓名:'), QLabel('联系方式:'), QLabel('销售姓名:'), QLabel('手术时间:')]
    text = []

    size_policy_min = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)

    dialog = QDialog()
    dialog.setSizePolicy(size_policy_min)
    dialog.setWindowTitle('Upload')
    dialog.setLayout(QVBoxLayout())
    dialog.setMinimumWidth(200)

    combo_box = QComboBox()
    combo_box.addItem("导板名称：THA手术导板")
    combo_box.addItem("导板名称：TKA手术导板")
    dialog.layout().addWidget(combo_box)

    for i in range(len(label)):
        text.append(QLineEdit())
        dialog.layout().addWidget(label[i])
        dialog.layout().addWidget(text[i])

    button = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, dialog)
    button.setSizePolicy(size_policy_min)
    button.accepted.connect(dialog.accept)
    button.rejected.connect(dialog.reject)
    dialog.layout().addWidget(button)

    if dialog.exec_() == QDialog.Accepted:
        if series_dict:
            # Web通讯
            data = {
                "Uuid": QUuid.createUuid().toString(),
                "PatientSex": series_dict["PatientSex"],
                "PatientAge": series_dict["PatientAge"],
                "GuideType": combo_box.currentIndex(),
                "SeriesInstanceUID_str": series_dict['SeriesInstanceUID'],
                "DoctorName": text[0].text(),
                "ContactInformation": text[1].text(),
                "SalesName": text[2].text(),
                "OperationTime": text[3].text()
            }
            print(str(data))
            # response = requests.post("http://192.168.11.174:2333/newUID", data=str(data))
            response = requests.post("http://192.168.11.174:3333/test_newUID", data=str(data))

            image_str = response.text.split(',')
            image_file = open('image.png', 'wb')
            image_file.write(base64.b64decode(image_str[1]))
            image_file.close()

            if response.text != "-1":
                # 上传数据
                upload(series_volume.data(), series_dict)
                # requests.post("http://192.168.11.174:3333/aiStart", data='1')

                # 显示二维码
                dialog = QDialog()
                dialog.setSizePolicy(size_policy_min)
                dialog.setWindowTitle('扫描二维码访问')
                dialog.setLayout(QVBoxLayout())

                image = QImage()
                image.load('image.png')

                label = QLabel()
                label.setPixmap(QPixmap.fromImage(image))
                label.setSizePolicy(size_policy_min)

                dialog.layout().addWidget(label)
                dialog.exec_()


def LeftButtonPressRelease(**kwargs):
    global series_opacity_range
    if kwargs['picked'] is series_opacity_range_box[0]:
        v = vmi.askInt(-10000, series_opacity_range[0], series_opacity_range[1])
        if v is not None:
            series_opacity_range[0] = v
        series_opacity_range_box[0].draw_text('min {:.0f}'.format(series_opacity_range[0]))
        update_series_opcity()
    elif kwargs['picked'] is series_opacity_range_box[1]:
        v = vmi.askInt(series_opacity_range[0], series_opacity_range[0], 10000)
        if v is not None:
            series_opacity_range[1] = v
        series_opacity_range_box[1].draw_text('min {:.0f}'.format(series_opacity_range[1]))
        update_series_opcity()


def NoButtonWheel(**kwargs):
    global series_opacity_range
    if kwargs['picked'] is series_opacity_range_box[0]:
        series_opacity_range[0] = min(max(series_opacity_range[0] + kwargs['delta'],
                                          -10000), series_opacity_range[1])
        series_opacity_range_box[0].draw_text('min {:.0f}'.format(series_opacity_range[0]))
        update_series_opcity()
    elif kwargs['picked'] is series_opacity_range_box[1]:
        series_opacity_range[1] = min(max(series_opacity_range[1] + kwargs['delta'],
                                          series_opacity_range[0]), 10000)
        series_opacity_range_box[1].draw_text('max {:.0f}'.format(series_opacity_range[1]))
        update_series_opcity()


def return_globals():
    return globals()


if __name__ == '__main__':
    client = pymongo.MongoClient('mongodb://root:medraw123@192.168.11.122:27017/admin', 27017)
    data_db: pymongo.collection.Collection = client.xj_testDB.data
    file_db = gridfs.GridFS(client.xj_testDB, collection='file')
    # 记录标记数据
    markData_db: pymongo.collection.Collection = client.xj_testDB.dataMF
    markFile_db = gridfs.GridFS(client.xj_testDB, collection='fileMF')

    main = vmi.Main(return_globals)
    main.setAppName('dicom_uoloader')
    main.setAppVersion(vmi.version)
    main.excludeKeys += ['main']

    menu_input = main.menuBar().addMenu('输入')
    menu_input.addAction('DICOM').triggered.connect(input_dicom)
    menu_input.addAction('Series').triggered.connect(input_series)

    menu_output = main.menuBar().addMenu('输出')
    menu_output.addAction('NIFTI').triggered.connect(output_nifti)
    menu_output.addAction('上传').triggered.connect(output_upload)

    series_list, series_dict = [], {}
    series_view = vmi.View()
    series_view.setCamera_Coronal()
    series_volume = vmi.ImageVolume(series_view)

    series_opacity_range = [200, 3000]
    update_series_opcity()

    series_opacity_range_box = [vmi.TextBox(series_view, text='min {:.0f}'.format(series_opacity_range[0]),
                                            size=[0.1, 0.03], pos=[0, 0.03], anchor=[0, 0], pickable=True),
                                vmi.TextBox(series_view, text='max {:.0f}'.format(series_opacity_range[1]),
                                            size=[0.1, 0.03], pos=[0.1, 0.03], anchor=[0, 0], pickable=True)]

    for box in series_opacity_range_box:
        box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]
        box.mouse['NoButton']['Wheel'] = [NoButtonWheel]

    main.layout().addWidget(series_view, 0, 0, 1, 1)
    vmi.appexec(main)
    vmi.appexit()
