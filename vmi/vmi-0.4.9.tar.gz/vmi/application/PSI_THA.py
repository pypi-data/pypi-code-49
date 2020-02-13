import pathlib
import tempfile
import time

import numpy as np
import pydicom
import vtk
from PySide2.QtGui import *
from numba import jit

import vmi


def read_dicom():
    dcmdir = vmi.askDirectory('DICOM')  # 用户选择文件夹

    if dcmdir is not None:  # 判断用户选中了有效文件夹并点击了确认
        series_list = vmi.sortSeries(dcmdir)  # 将文件夹及其子目录包含的所有DICOM文件分类到各个系列

        if len(series_list) > 0:  # 判断该文件夹内包含有效的DICOM系列
            series = vmi.askSeries(series_list)  # 用户选择DICOM系列

            if series is not None:  # 判断用户选中了有效系列并点击了确认
                with pydicom.dcmread(series.filenames()[0]) as ds:
                    global patient_name
                    patient_name = str(ds.PatientName)
                    patient_name_box.draw_text('姓名：{}'.format(patient_name))
                    patient_name_box.setVisible(True)

                    global dicom_ds
                    dicom_ds = series.toKeywordValue()
                return series.read()  # 读取DICOM系列为图像数据


def on_init_voi():
    size = vmi.askInt(1, 300, 1000, suffix='mm', title='请输入目标区域尺寸')
    if size is not None:
        global LR, original_target, voi_size, voi_center, spcut_center
        original_target = original_view.pickPt_Cell()
        voi_center = np.array([vmi.imCenter(original_slice.data())[0], original_target[1], original_target[2]])
        voi_size = np.array([vmi.imSize(original_slice.data())[0], size, size])
        init_voi()

        LR = 1 if original_target[0] > voi_center[0] else -1
        patient_LR_box.draw_text('患侧：{}'.format('左' if LR > 0 else '右'))
        patient_LR_box.setVisible(True)

        spcut_center = original_target.copy()
        update_spcut()

        voi_view.setCamera_Coronal()
        update_spcut_section()

        voi_view.setCamera_FitAll()
        for v in [voi_view, *spcut_y_views, *spcut_z_views]:
            v.setEnabled(True)


@jit(nopython=True)
def ary_pad(input_ary, constant):
    for k in [0, input_ary.shape[0] - 1]:
        for j in range(input_ary.shape[1]):
            for i in range(input_ary.shape[2]):
                input_ary[k][j][i] = constant
    for k in range(input_ary.shape[0]):
        for j in [0, input_ary.shape[1] - 1]:
            for i in range(input_ary.shape[2]):
                input_ary[k][j][i] = constant
    for k in range(input_ary.shape[0]):
        for j in range(input_ary.shape[1]):
            for i in [0, input_ary.shape[2] - 1]:
                input_ary[k][j][i] = constant


def init_voi():
    global voi_size, voi_center, voi_origin, voi_cs, voi_image
    voi_origin = voi_center - 0.5 * voi_size
    voi_cs = vmi.CS4x4(origin=voi_origin)

    voi_image = vmi.imReslice(original_slice.data(), voi_cs, voi_size, -1024)
    voi_image.SetOrigin(voi_cs.origin())

    voi_ary = vmi.imArray_VTK(voi_image)
    ary_pad(voi_ary, -1024)
    voi_image = vmi.imVTK_Array(voi_ary, vmi.imOrigin(voi_image), vmi.imSpacing(voi_image))
    voi_volume.setData(voi_image)

    pd = vmi.imIsosurface(voi_image, 3000)
    metal_prop.setData(pd)
    pelvis_view.setCamera_Coronal()
    pelvis_view.setCamera_FitAll()


def update_line_cut():
    if len(local_roi_pts) > 1:
        plcut_prop.setData(vmi.ccWire(vmi.ccSegments(local_roi_pts, True)))
    else:
        plcut_prop.setData(None)


@jit(nopython=True)
def ary_mask(input_ary, mask_ary, threshold, target):
    for k in range(input_ary.shape[0]):
        for j in range(input_ary.shape[1]):
            for i in range(input_ary.shape[2]):
                if mask_ary[k][j][i] != 0 and threshold <= input_ary[k][j][i]:
                    input_ary[k][j][i] = target


def plcut_voi_image():
    cs = voi_view.cameraCS()
    d = vmi.imSize_Vt(voi_volume.data(), cs.axis(2))
    pts = [vmi.ptOnPlane(pt, vmi.imCenter(voi_volume.data()), cs.axis(2)) for pt in local_roi_pts]
    pts = [pt - d * cs.axis(2) for pt in pts]
    sh = vmi.ccFace(vmi.ccWire(vmi.ccSegments(pts, True)))
    sh = vmi.ccPrism(sh, cs.axis(2), 2 * d)

    mask = vmi.imStencil_PolyData(vmi.ccPd_Sh(sh),
                                  vmi.imOrigin(voi_volume.data()),
                                  vmi.imSpacing(voi_volume.data()),
                                  vmi.imExtent(voi_volume.data()))
    mask_ary = vmi.imArray_VTK(mask)
    voi_ary = vmi.imArray_VTK(voi_volume.data())
    ary_mask(voi_ary, mask_ary, bone_value, target_value)
    voi_image = vmi.imVTK_Array(voi_ary, vmi.imOrigin(voi_volume.data()), vmi.imSpacing(voi_volume.data()))
    voi_volume.setData(voi_image)

    for v in spcut_z_views + spcut_y_views:
        v.updateInTime()


def spcut_voi_image():
    spcut_image = vmi.imStencil_PolyData(spcut_prop.data(),
                                         vmi.imOrigin(voi_volume.data()),
                                         vmi.imSpacing(voi_volume.data()),
                                         vmi.imExtent(voi_volume.data()))
    spcut_ary = vmi.imArray_VTK(spcut_image)
    voi_ary = vmi.imArray_VTK(voi_volume.data())

    ary_mask(voi_ary, spcut_ary, bone_value, target_value)
    voi_image = vmi.imVTK_Array(voi_ary, vmi.imOrigin(voi_volume.data()), vmi.imSpacing(voi_volume.data()))
    voi_volume.setData(voi_image)


def update_spcut():
    spcut_mesh = vmi.pdSphere(spcut_radius, spcut_center)
    spcut_prop.setData(spcut_mesh)


def update_spcut_section():
    angle = 30
    y_oblique = [vmi.CS4x4().rotate(angle, [0, 0, 1]), vmi.CS4x4(), vmi.CS4x4().rotate(-angle, [0, 0, 1])]
    z_oblique = [vmi.CS4x4().rotate(-angle, [0, 1, 0]), vmi.CS4x4(), vmi.CS4x4().rotate(angle, [0, 1, 0])]

    y_normals = [cs.mvt([0, 1, 0]) for cs in y_oblique]
    z_normals = [cs.mvt([0, 0, 1]) for cs in z_oblique]

    y_cs = [vmi.CS4x4_Coronal(), vmi.CS4x4_Coronal(), vmi.CS4x4_Coronal()]
    y_cs[0] = y_cs[0].rotate(-angle, y_cs[0].axis(1))
    y_cs[2] = y_cs[2].rotate(angle, y_cs[2].axis(1))

    z_cs = [vmi.CS4x4_Axial(), vmi.CS4x4_Axial(), vmi.CS4x4_Axial()]
    z_cs[0] = z_cs[0].rotate(-angle, z_cs[0].axis(1))
    z_cs[2] = z_cs[2].rotate(angle, z_cs[2].axis(1))

    hheight = 50
    hwidth = hheight * spcut_y_views[0].width() / spcut_y_views[0].height()

    for i in range(3):
        y_cs[i].setOrigin(spcut_center - y_cs[i].mpt([hwidth, hheight, 0]))
        z_cs[i].setOrigin(spcut_center - z_cs[i].mpt([hwidth, hheight, 0]))

    for i in range(3):
        spcut_y_slices[i].setSlicePlane(spcut_center, y_normals[i])
        spcut_z_slices[i].setSlicePlane(spcut_center, z_normals[i])

    for i in range(3):
        spcut_y_props[i].setData(vmi.pdPolygon_Regular(spcut_radius, spcut_center, y_normals[i]))
        spcut_z_props[i].setData(vmi.pdPolygon_Regular(spcut_radius, spcut_center, z_normals[i]))

    for i in range(3):
        spcut_y_views[i].setCamera_FPlane(y_cs[i], 2 * hheight)
        spcut_z_views[i].setCamera_FPlane(z_cs[i], 2 * hheight)


def init_pelvis():
    pd = vmi.imResample_Isotropic(voi_volume.data())
    pd = vmi.imIsosurface(pd, bone_value)
    pelvis_prop.setData(pd)

    pelvis_view.setCamera_Coronal()
    pelvis_view.setCamera_FitAll()
    pelvis_view.setEnabled(True)

    origin = np.array(pelvis_prop.data().GetCenter())
    pelvis_cs.setOrigin(origin)
    cup_cs.setOrigin(original_target)


def update_pelvis_MPP():
    global pelvis_cs
    vr = pelvis_view.cameraVt_Right()
    vr = vr if np.dot(vr, np.array([1, 0, 0])) >= 0 else -vr
    if vmi.vtAngle(vr, pelvis_cs.axis(1)) < 1 or vmi.vtAngle(vr, pelvis_cs.axis(1)) > 179:
        return

    pelvis_cs.setAxis(0, vr)
    pelvis_cs.orthogonalize([2, 0])
    update_cup_orientation()
    update_cup()

    origin = pelvis_view.pickPt_FocalPlane([0.5 * pelvis_view.width(), 0.5 * pelvis_view.height()])
    pelvis_cs.setOrigin(origin)
    cs = vmi.CS4x4().reflect(pelvis_cs.axis(0), pelvis_cs.origin())
    pd = vmi.pdMatrix(pelvis_prop.data(), cs.matrix4x4())
    pelvis_MPP_prop.setData(pd)


def update_pelvis_APP():
    global pelvis_cs
    vr = pelvis_view.cameraVt_Right()
    vr = vr if np.dot(vr, np.array([0, 1, 0])) >= 0 else -vr
    if vmi.vtAngle(vr, pelvis_cs.axis(0)) < 1 or vmi.vtAngle(vr, pelvis_cs.axis(0)) > 179:
        return

    pelvis_cs.setAxis(1, vr)
    pelvis_cs.orthogonalize([2, 0])
    update_cup_orientation()
    update_cup()

    cs = pelvis_view.cameraCS()
    pd = vmi.pdMatrix(pelvis_prop.data(), cs.inv().matrix4x4())
    b, c = pd.GetBounds(), pd.GetCenter()
    left_top = np.array([b[0], b[2], c[2]])
    right_top = np.array([b[1], b[2], c[2]])
    left_bottom = np.array([b[0], b[3], c[2]])
    right_bottom = np.array([b[1], b[3], c[2]])
    xn = int(np.round(0.1 * (pd.GetBounds()[1] - pd.GetBounds()[0])))

    lines = []
    for i in range(xn + 1):
        pts = [left_top + i / xn * (right_top - left_top),
               left_bottom + i / xn * (right_bottom - left_bottom)]
        pts = [cs.mpt(pt) for pt in pts]
        line = vmi.ccEdge(vmi.ccSegment(pts[0], pts[1]))
        line = vmi.ccPd_Sh(line)
        lines.append(line)

    pd = vmi.pdAppend(lines)
    pelvis_APP_prop.setData(pd)


def update_cup_orientation():
    cs = pelvis_cs.rotate(-cup_RI, pelvis_cs.axis(1)).rotate(-cup_RA, pelvis_cs.axis(0))
    cup_axis = -cs.axis(2) * np.array([LR, 1, 1])

    cup_cs.setAxis(1, pelvis_cs.axis(1))
    cup_cs.setAxis(2, cup_axis)
    cup_cs.orthogonalize([0, 1])
    cup_cs.setAxis(0, -LR * cup_cs.axis(0))
    cup_cs.normalize()

    # cup_RA = np.rad2deg(np.arctan(-cup_axis[1] / np.sqrt(1 - cup_axis[2] ** 2)))
    # cup_RI = np.rad2deg(-np.abs(cup_axis[0] / cup_axis[2]))


def update_cup():
    plane = vtk.vtkPlane()
    plane.SetNormal(cup_cs.axis(2))
    plane.SetOrigin(cup_cs.origin())

    pd = vmi.pdSphere(cup_radius, cup_cs.origin())
    pd = vmi.pdClip_Implicit(pd, plane)[1]

    pd_border = vmi.pdPolyline_Regular(cup_radius, cup_cs.origin(), cup_cs.axis(2))
    pd = vmi.pdAppend([pd, pd_border])

    cs = vmi.CS4x4().reflect(pelvis_cs.axis(0), pelvis_cs.origin())
    pd_MPP = vmi.pdMatrix(pd, cs.matrix4x4())
    cup_prop.setData(vmi.pdAppend([pd, pd_MPP]))

    if pelvis_slice_box.text() == '断层':
        pd = vmi.pdCut_Implicit(cup_prop.data(), pelvis_slice.slicePlane())
        cup_section_prop.setData(pd)


@jit(nopython=True)
def pt_ary_cs_mask(pt_ary: np.ndarray, cs: np.ndarray, mask: np.ndarray):
    return (pt_ary @ cs) * mask


def init_guide():
    size = np.array([5 * cup_radius, 5 * cup_radius, 5 * cup_radius])
    cs = vmi.CS4x4(origin=cup_cs.origin() - 0.5 * size)
    image = vmi.imReslice(voi_volume.data(), cs, size, -1024)
    image.SetOrigin(cs.origin())

    ary = vmi.imArray_VTK(image)
    ary_pad(ary, -1024)
    image = vmi.imVTK_Array(ary, vmi.imOrigin(image), vmi.imSpacing(image))
    image = vmi.imResample_Isotropic(image)

    pd = vmi.imIsosurface(image, bone_value)
    pd = vmi.pdSmooth_WindowedSinc(pd, 20)
    aceta_prop.setData(pd)

    update_guide_path()
    update_cup_camera_plane()
    guide_view.setEnabled(True)


def update_cup_camera_sagittal():
    cs = vmi.CS4x4(axis1=-pelvis_cs.axis(2), axis2=-LR * pelvis_cs.axis(0))
    cs.orthogonalize([0])
    cs.setOrigin(cup_cs.origin() - 2.25 * cup_radius * cs.axis(0) - 2.25 * cup_radius * cs.axis(1))
    pelvis_view.setCamera_FPlane(cs, 4.5 * cup_radius)
    pelvis_view.updateInTime()


def update_cup_camera_coronal():
    cs = vmi.CS4x4(axis1=-pelvis_cs.axis(2), axis2=pelvis_cs.axis(1))
    cs.orthogonalize([0])
    cs.setOrigin(cup_cs.origin() - 2.25 * cup_radius * cs.axis(0) - 2.25 * cup_radius * cs.axis(1))
    pelvis_view.setCamera_FPlane(cs, 4.5 * cup_radius)
    pelvis_view.updateInTime()


def update_cup_camera_axial():
    cs = vmi.CS4x4(axis1=pelvis_cs.axis(1), axis2=pelvis_cs.axis(2))
    cs.orthogonalize([0])
    cs.setOrigin(cup_cs.origin() - 2.25 * cup_radius * cs.axis(0) - 2.25 * cup_radius * cs.axis(1))
    pelvis_view.setCamera_FPlane(cs, 4.5 * cup_radius)
    pelvis_view.updateInTime()


def update_cup_camera_RA():
    cs = vmi.CS4x4(axis1=-cup_cs.axis(1), axis2=-cup_cs.axis(0))
    cs.orthogonalize([0])
    cs.setOrigin(cup_cs.origin() - 2.25 * cup_radius * cs.axis(0) - 2.25 * cup_radius * cs.axis(1))
    pelvis_view.setCamera_FPlane(cs, 4.5 * cup_radius)
    pelvis_view.updateInTime()


def update_cup_camera_RI():
    cs = vmi.CS4x4(axis1=-cup_cs.axis(0), axis2=cup_cs.axis(1))
    cs.orthogonalize([0])
    cs.setOrigin(cup_cs.origin() - 2.25 * cup_radius * cs.axis(0) - 2.25 * cup_radius * cs.axis(1))
    pelvis_view.setCamera_FPlane(cs, 4.5 * cup_radius)
    pelvis_view.updateInTime()


def update_cup_camera_plane():
    cs = vmi.CS4x4(axis1=-cup_cs.axis(0), axis2=-cup_cs.axis(2))
    cs.orthogonalize([0])
    cs.setOrigin(cup_cs.origin() - 2.25 * cup_radius * cs.axis(0) - 2.25 * cup_radius * cs.axis(1))
    pelvis_view.setCamera_FPlane(cs, 4.5 * cup_radius)
    pelvis_view.updateInTime()


def update_guide_path():
    global cup_cs, body_cs, large_z, small_t
    large_z, small_t = 100, 5
    body_vt_x = cup_cs.rotate(LR * (body_angle + 45), -cup_cs.axis(2)).mvt([1, 0, 0])
    body_cs = vmi.CS4x4(origin=cup_cs.mpt([0, 0, large_z]), axis0=body_vt_x, axis2=-cup_cs.axis(2))
    body_cs.orthogonalize([1, 0])
    body_cs.normalize()

    global body_xr, body_yr, head_xr, head_yr, body_x_negtive
    head_yr = body_yr
    body_x_negtive = body_yr / np.sin(np.deg2rad(72))

    global body_wire
    body_pts = [body_cs.mpt([body_xr + head_xr, LR * -body_yr, 0]),
                body_cs.mpt([body_xr + head_xr, LR * body_yr, 0]),
                body_cs.mpt([-body_x_negtive * np.cos(np.deg2rad(72)), LR * body_yr, 0]),
                body_cs.mpt([-body_x_negtive, 0, 0]),
                body_cs.mpt([-body_x_negtive * np.cos(np.deg2rad(72)), LR * -body_yr, 0])]

    body_wire = body_cs.workplane().polyline(
        [body_cs.inv().mpt(pt)[:2].tolist() for pt in body_pts]).close().val().wrapped
    body_axis = vmi.ccEdge(vmi.ccSegment(body_cs.mpt([0, 0, 0]), body_cs.mpt([0, 0, 2 * large_z])))

    global body_hole_wire
    body_hole_radius = small_t
    body_hole_wire = vmi.ccWire(vmi.ccEdge(
        vmi.ccCircle(body_hole_radius, body_cs.origin(), body_cs.axis(2), body_cs.axis(0))))

    global head_cs
    head_cs = body_cs.copy()
    head_cs.setOrigin(body_cs.mpt([body_xr, 0, 0]))

    global slider_length, slider_area_wire, bolt_r
    bolt_r = 3
    slider_area_pts = [head_cs.mpt(
        [-slider_length * np.sin(np.deg2rad(t)),
         -LR * (slider_length * np.cos(np.deg2rad(t)) - (head_yr - bolt_r * 2)),
         0]) for t in range(-30, 90)]
    slider_area_pts += [head_cs.mpt(
        [-slider_length * np.sin(np.deg2rad(t)),
         -LR * (slider_length * np.cos(np.deg2rad(t)) + (head_yr - bolt_r * 2)),
         0]) for t in reversed(range(-30, 90))]
    slider_area_wire = vmi.ccWire(vmi.ccSegments(slider_area_pts))

    global guide_path, guide_path_prop
    guide_path = vmi.ccBoolean_Union([body_wire, body_axis, body_hole_wire, slider_area_wire])
    guide_path_prop.setData(guide_path)
    return


def update_guide_plate():
    global UDI, UDI_time
    UDI_time = time.localtime()
    UDI = '{}{}'.format('TH', vmi.convert_base(int(time.mktime(UDI_time) * 1e3)).upper())

    time_start, time_prev = time.time(), time.time()

    global body_cs, body_xr, body_yr, head_cs, head_xr, head_yr, large_z, small_t, slider_length, bolt_r
    mold_xr = body_xr + head_xr
    mold_yr = body_yr + slider_length - bolt_r * 2
    res = 1
    xn, yn = int(np.ceil(mold_xr / res)) + 1, int(np.ceil(mold_yr / res)) + 1
    body_mold, body_z_array = [], []
    body = vmi.ccMatchSolid_Rect(
        aceta_prop.data(), body_cs, xn, yn, res, small_t, 2 * large_z - small_t, 0.2, body_mold, body_z_array)

    time_stop = time.time() - time_prev
    time_prev = time.time()
    print('match body', time_stop)

    nx, ny = int(np.ceil(head_xr / res)) + 1, int(np.ceil(head_yr / res)) + 1
    head_z_array = []
    vmi.ccMatchSolid_Rect(
        aceta_prop.data(), head_cs, nx, ny, res, small_t, 2 * large_z - small_t, 0.2, None, head_z_array)

    time_stop = time.time() - time_prev
    time_prev = time.time()
    print('match head', time_stop)

    global head_height
    head_height = 10
    head_z = np.min(head_z_array[0]) - small_t

    global guide_mold, guide_mold_prop
    mold_max_z = head_z + small_t + body_xr + head_xr
    mold_wire = body_cs.workplane([0, -LR * 0.5 * (mold_yr - mold_xr), 0]).rect(
        2 * mold_xr, mold_xr + mold_yr).val().wrapped
    mold_box = vmi.ccPrism(vmi.ccFace(mold_wire), body_cs.axis(2), mold_max_z)
    guide_mold = vmi.ccBoolean_Intersection([body_mold[0], mold_box])

    time_stop = time.time() - time_prev
    time_prev = time.time()
    print('mold', time_stop)

    label_cs = vmi.CS4x4(origin=body_cs.mpt([0, LR * 0.5 * (mold_xr - mold_yr), mold_max_z - 1]),
                         axis1=-LR * body_cs.axis(1), axis2=-body_cs.axis(2))
    label_cs.orthogonalize([0])

    label_wire = label_cs.workplane().rect(2 * mold_xr, mold_xr + mold_yr + small_t * 4).val().wrapped
    label_box = vmi.ccPrism(vmi.ccFace(label_wire), body_cs.axis(2), 2)
    guide_mold = vmi.ccBoolean_Union([guide_mold, label_box])

    label_cs = vmi.CS4x4(origin=body_cs.mpt([0, -LR * (mold_yr + small_t), mold_max_z]),
                         axis1=-LR * body_cs.axis(1), axis2=-body_cs.axis(2))
    label_cs.orthogonalize([0])
    text = '{} {}'.format(patient_name, 'L' if LR > 0 else 'R')
    label_text = label_cs.workplane().text(text, small_t, 3, font='DengXian', kind='bold').val().wrapped
    guide_mold = vmi.ccBoolean_Union([guide_mold, label_text])

    label_cs = vmi.CS4x4(origin=body_cs.mpt([0, LR * (mold_xr + small_t), mold_max_z]),
                         axis1=-LR * body_cs.axis(1), axis2=-body_cs.axis(2))
    label_cs.orthogonalize([0])
    label_text = label_cs.workplane().text(UDI, small_t, 3, font='DengXian', kind='bold').val().wrapped
    guide_mold = vmi.ccBoolean_Union([guide_mold, label_text])

    guide_mold_prop.setData(guide_mold)
    # guide_mold_prop.setData(vmi.pdTriangle(vmi.ccPd_Sh(guide_mold), 0, 0))

    time_stop = time.time() - time_prev
    time_prev = time.time()
    print('label', time_stop)

    global body_x_negtive
    body_pts = [[body_xr + head_xr, LR * -body_yr, head_z - head_height],
                [body_xr + head_xr, LR * body_yr, head_z - head_height],
                [-body_x_negtive * np.cos(np.deg2rad(72)), LR * body_yr, head_z - head_height],
                [-body_x_negtive, 0, head_z - head_height],
                [-body_x_negtive * np.cos(np.deg2rad(72)), LR * -body_yr, head_z - head_height]]
    body_wire = vmi.ccWire(vmi.ccSegments([body_cs.mpt(pt) for pt in body_pts], True))
    body_box = vmi.ccPrism(vmi.ccFace(body_wire), body_cs.axis(2), 2 * large_z)
    body = vmi.ccBoolean_Intersection([body, body_box])

    body_pts = [[body_xr + head_xr, LR * body_yr, 2 * large_z],
                [body_xr + head_xr, LR * body_yr, head_z - head_height],
                [body_xr - head_xr, LR * body_yr, head_z - head_height],
                [body_xr - head_xr, LR * body_yr, head_z],
                [-body_x_negtive, LR * body_yr, head_z],
                [-body_x_negtive, LR * body_yr, 2 * large_z]]
    body_wire = vmi.ccWire(vmi.ccSegments([body_cs.mpt(pt) for pt in body_pts], True))
    body_box = vmi.ccPrism(vmi.ccFace(body_wire), -LR * body_cs.axis(1), 2 * body_yr)
    body = vmi.ccBoolean_Intersection([body, body_box])

    time_stop = time.time() - time_prev
    time_prev = time.time()
    print('body', time_stop)

    global body_hole_wire
    body_hole = vmi.ccPrism(vmi.ccFace(body_hole_wire), body_cs.axis(2), 2 * large_z)

    bolt_margin = 0.1
    head_chute_pts = [[bolt_r, -LR * (head_yr - bolt_r), head_z - head_height - 1 - bolt_margin]]
    head_chute_pts_z = head_chute_pts[-1][2]
    while head_chute_pts_z + 3 <= head_z:
        # head_chute_pts += [[bolt_r - 1, -LR * (head_yr - bolt_r), head_chute_pts_z + 1],
        #                    [bolt_r, -LR * (head_yr - bolt_r), head_chute_pts_z + 1],
        #                    [bolt_r - 1, -LR * (head_yr - bolt_r), head_chute_pts_z + 3]]
        head_chute_pts += [[bolt_r, -LR * (head_yr - bolt_r), head_chute_pts_z + 1],
                           [bolt_r - 1, -LR * (head_yr - bolt_r), head_chute_pts_z + 3]]
        head_chute_pts_z = head_chute_pts[-1][2]
    slider_bolt_pts = head_chute_pts.copy()
    head_chute_pts += [[head_chute_pts[-1][0], head_chute_pts[-1][1], head_chute_pts[-1][2] + 1]]
    head_chute_pts += [[-pt[0], pt[1], pt[2]] for pt in reversed(head_chute_pts)]
    head_chute_pts = [head_cs.mpt(pt) for pt in head_chute_pts]
    head_chute_wire = vmi.ccWire(vmi.ccSegments(head_chute_pts, True))
    head_chute = vmi.ccPrism(vmi.ccFace(head_chute_wire), LR * head_cs.axis(1), 2 * head_yr)

    slider_bolt_pts = [[pt[0] - bolt_margin, 0, pt[2]] for pt in slider_bolt_pts]
    slider_bolt_pts += [[0, 0, slider_bolt_pts[-1][2]]]
    slider_bolt_pts += [[0, 0, head_z - head_height - 1 - bolt_margin]]
    slider_bolt_pts = [head_cs.mpt(pt) for pt in slider_bolt_pts]
    slider_bolt_wire = vmi.ccWire(vmi.ccSegments(slider_bolt_pts, True))
    slider_bolt = vmi.ccRevolve(vmi.ccFace(slider_bolt_wire), head_cs.origin(), head_cs.axis(2), 360)

    slider_kirs_depth = 20
    slider_max_z = head_z - head_height - bolt_margin
    slider_xr = bolt_r + 2
    slider_pts = [[slider_xr, LR * slider_xr, slider_max_z],
                  [slider_xr, LR * slider_xr, slider_max_z - 2 * slider_xr],
                  [slider_xr, -LR * (slider_length + slider_xr), slider_max_z - 2 * slider_xr],
                  [slider_xr, -LR * (slider_length + slider_xr),
                   slider_max_z - 2 * slider_xr + slider_kirs_depth],
                  [slider_xr, -LR * (slider_length - slider_xr),
                   slider_max_z - 2 * slider_xr + slider_kirs_depth],
                  [slider_xr, -LR * (slider_length - slider_xr), slider_max_z]]
    slider_pts = [head_cs.mpt(pt) for pt in slider_pts]
    slider_wire = vmi.ccWire(vmi.ccSegments(slider_pts, True))
    slider = vmi.ccPrism(vmi.ccFace(slider_wire), -head_cs.axis(0), 2 * (slider_xr))

    time_stop = time.time() - time_prev
    time_prev = time.time()
    print('slider', time_stop)

    global kirs_radius, slider_kirs_radius
    slider_kirs_radius = kirs_radius + 0.2
    slider_kirs_center = head_cs.mpt([0, -LR * slider_length, 0])
    slider_kirs_hole = vmi.ccPrism(vmi.ccFace(vmi.ccWire(vmi.ccCircle(
        slider_kirs_radius, slider_kirs_center, head_cs.axis(2), head_cs.axis(0)))), body_cs.axis(2), 2 * large_z)

    slider = vmi.ccBoolean_Union([slider, slider_bolt])
    slider = vmi.ccBoolean_Difference([slider, slider_kirs_hole])
    guide_slider_prop.setData(slider)
    # guide_slider_prop.setData(vmi.pdTriangle(vmi.ccPd_Sh(slider), 0, 0))

    time_stop = time.time() - time_prev
    time_prev = time.time()
    print('slider', time_stop)

    global guide_body, guide_body_prop
    guide_body = vmi.ccBoolean_Difference([body, body_hole, head_chute])
    guide_body_prop.setData(guide_body)
    # guide_body_prop.setData(vmi.pdTriangle(vmi.ccPd_Sh(guide_body), 0, 0))

    time_stop = time.time() - time_prev
    time_prev = time.time()
    print('body cut', time_stop)
    print(time.time() - time_start)


def save_docx(file):
    global UDI, UDI_time

    with tempfile.TemporaryDirectory() as p:
        png = str(pathlib.Path(p) / '.png')

        doc = vmi.docx_document('设计确认单')
        vmi.docx_section_landscape_A4(doc.sections[0])
        vmi.docx_section_margin_middle(doc.sections[0])
        vmi.docx_section_header(doc.sections[0])

        s_title = vmi.docx_style(doc, '影为标题', 'Normal', size=26, alignment='CENTER')
        s_header = vmi.docx_style(doc, '影为页眉', 'Header', size=10)
        s_body_left = vmi.docx_style(doc, '影为正文', 'Body Text')
        s_body_left_indent = vmi.docx_style(doc, '影为正文首行缩进', 'Body Text', first_line_indent=2)
        s_body_center = vmi.docx_style(doc, '影为正文居中', 'Body Text', alignment='CENTER')
        s_table = vmi.docx_style(doc, '影为表格', 'Table Grid', alignment='CENTER')

        doc.sections[0].header.paragraphs[0].text = '影为医疗科技（上海）有限公司\t\t\t\t{}'.format('[表单号]')
        doc.sections[0].header.paragraphs[0].style = s_header

        def add_row_text(table, texts, styles, merge=None):
            r = len(table.add_row().table.rows) - 1
            if merge is not None:
                table.cell(r, merge[0]).merge(table.cell(r, merge[1]))
            for c in range(min(len(table.columns), len(texts))):
                table.cell(r, c).paragraphs[0].text = texts[c]
                table.cell(r, c).paragraphs[0].style = styles[c]

        def add_row_picture(table, text, styles, pic_file):
            r = len(table.add_row().table.rows) - 1
            table.cell(r, 1).merge(table.cell(r, 3))
            table.cell(r, 0).paragraphs[0].text = text
            table.cell(r, 0).paragraphs[0].style = styles[0]
            table.cell(r, 1).paragraphs[0].style = styles[1]

            with open(png, 'rb') as pic:
                table.cell(r, 1).paragraphs[0].add_run().add_picture(pic, width=table.cell(r, 1).width * 0.7)

        doc_table = doc.add_table(1, 4, s_table)
        doc_table.autofit = True
        doc_table.alignment = vmi.docx.enum.table.WD_TABLE_ALIGNMENT.CENTER

        doc_table.cell(0, 0).merge(doc_table.cell(0, 3))
        doc_table.cell(0, 0).paragraphs[0].text = '设计确认单\nDesign Confirmation'
        doc_table.cell(0, 0).paragraphs[0].style = s_title

        add_row_text(doc_table, ['顾客名称\nCustomer name', '',
                                 '顾客编号\nCustomer number', ''], [s_body_center] * 4)
        add_row_text(doc_table, ['医师\nPhysician', '',
                                 '电邮\nEmail', ''], [s_body_center] * 4)
        add_row_text(doc_table, ['联系人\nContact', '',
                                 '电话\nPhone number', ''], [s_body_center] * 4)
        add_row_text(doc_table, ['发货地址\nShipping address', ''], [s_body_center, s_body_left], [1, 3])

        text = '顾客收货视为已阅读并接受：'
        text += '\n1）所述产品属于个性化医疗器械；'
        text += '\n2）确认设计输入已包含顾客要求；'
        text += '\n3）确认设计输出符合顾客要求，同意进行生产制造；'
        text += '\n4）当顾客要求与产品上市信息冲突时，不作为设计输入。'
        add_row_text(doc_table, ['销售条款\nTerms of sale', text], [s_body_center, s_body_left], [1, 3])

        add_row_text(doc_table, ['销售工程师\nSales engineer', '',
                                 '电话\nPhone number', ''], [s_body_center] * 4)

        add_row_text(doc_table, ['产品名称\nProduct name', '全髋关节置换手术导板',
                                 '序列号\nSerial number', UDI], [s_body_center] * 4)
        add_row_text(doc_table, ['型号\nModel', 'TH',
                                 '规格\nSpecification', '定制式'], [s_body_center] * 4)
        add_row_text(doc_table, [
            '患者\nPatient',
            '{}\n{} {}'.format(dicom_ds['PatientName'], dicom_ds['PatientSex'], dicom_ds['PatientAge']),
            '术侧\nSpecification', '左' if LR > 0 else '右'], [s_body_center] * 4)

        spc, dim = vmi.imSpacing(original_slice.data()), vmi.imDimensions(original_slice.data())
        text = '描述：{}，{}，{}'.format(dicom_ds['StudyDate'], dicom_ds['Modality'], dicom_ds['StudyDescription'])
        text += '\n参数：{}×{}×{}，{}×{}×{} mm'.format(dim[0], dim[1], dim[2], spc[0], spc[1], spc[2])
        text += '\n系列：{}'.format(dicom_ds['SeriesInstanceUID'])
        add_row_text(doc_table, ['影像输入\nRadiological input', text], [s_body_center, s_body_left], [1, 3])

        text = '影像学前倾角：{:.1f}°\n影像学外展角：{:.1f}°'.format(cup_RA, cup_RI)
        add_row_text(doc_table, ['临床输入\nClinical input', text], [s_body_center, s_body_left], [1, 3])

        text = '骨阈值：{:.0f} HU'.format(bone_value)
        text += '\n主体方位：{:.0f}°，主体长径：{:.0f} mm，主体短径：{:.0f} mm'.format(body_angle, body_xr, body_yr)
        text += '\n滑杆长度：{:.0f} mm'.format(slider_length)
        text += '\n导针半径：{:.1f} mm'.format(kirs_radius)
        add_row_text(doc_table, ['造型输入\nModeling input', text], [s_body_center, s_body_left], [1, 3])

        add_row_text(doc_table, ['设计时间\nDesign time', '{}年{}月{}日{}'.format(
            UDI_time.tm_year, UDI_time.tm_mon, UDI_time.tm_mday, time.strftime('%H:%M:%S', UDI_time))],
                     [s_body_center, s_body_left], [1, 3])

        text = '{} {}'.format(UDI, '定位板.stl')
        text += '\n{} {}'.format(UDI, '滑杆.stl')
        text += '\n{} {}'.format(UDI, '配模.stl')
        add_row_text(doc_table, ['设计输出\nDesign output', text], [s_body_center, s_body_left], [1, 3])

        visibles = [aceta_prop.visible(),
                    guide_path_prop.visible(),
                    guide_body_prop.visible(),
                    guide_slider_prop.visible(),
                    guide_mold_prop.visible()]

        aceta_prop.setVisible(True)
        guide_path_prop.setVisible(False)
        guide_body_prop.setVisible(False)
        guide_slider_prop.setVisible(False)
        guide_mold_prop.setVisible(False)
        update_cup_camera_plane()
        guide_view.snapshot_PNG(png)
        add_row_picture(doc_table, '快照（1/6）\nSnapshot', [s_body_center, s_body_center], png)

        aceta_prop.setVisible(True)
        guide_path_prop.setVisible(True)
        guide_body_prop.setVisible(True)
        guide_slider_prop.setVisible(False)
        guide_mold_prop.setVisible(False)
        guide_view.snapshot_PNG(png)
        add_row_picture(doc_table, '快照（2/6）\nSnapshot', [s_body_center, s_body_center], png)

        aceta_prop.setVisible(True)
        guide_path_prop.setVisible(False)
        guide_body_prop.setVisible(True)
        guide_slider_prop.setVisible(True)
        guide_mold_prop.setVisible(False)
        guide_view.camera().Elevation(-30)
        guide_view.camera().OrthogonalizeViewUp()
        guide_view.snapshot_PNG(png)
        add_row_picture(doc_table, '快照（3/6）\nSnapshot', [s_body_center, s_body_center], png)

        aceta_prop.setVisible(True)
        guide_path_prop.setVisible(False)
        guide_body_prop.setVisible(True)
        guide_slider_prop.setVisible(True)
        guide_mold_prop.setVisible(False)
        guide_view.camera().Elevation(-60)
        guide_view.camera().OrthogonalizeViewUp()
        guide_view.camera().Azimuth(LR * 90)
        guide_view.camera().Elevation(30)
        guide_view.camera().OrthogonalizeViewUp()
        guide_view.snapshot_PNG(png)
        add_row_picture(doc_table, '快照（4/6）\nSnapshot', [s_body_center, s_body_center], png)

        aceta_prop.setVisible(False)
        guide_path_prop.setVisible(False)
        guide_body_prop.setVisible(True)
        guide_slider_prop.setVisible(True)
        guide_mold_prop.setVisible(False)
        guide_view.camera().Elevation(-90)
        guide_view.camera().OrthogonalizeViewUp()
        guide_view.setCamera_FitAll()
        guide_view.snapshot_PNG(png)
        add_row_picture(doc_table, '快照（5/6）\nSnapshot', [s_body_center, s_body_center], png)

        aceta_prop.setVisible(False)
        guide_path_prop.setVisible(False)
        guide_body_prop.setVisible(True)
        guide_slider_prop.setVisible(True)
        guide_mold_prop.setVisible(True)
        update_cup_camera_plane()
        guide_view.camera().Elevation(-30)
        guide_view.camera().OrthogonalizeViewUp()
        guide_view.snapshot_PNG(png)
        add_row_picture(doc_table, '快照（6/6）\nSnapshot', [s_body_center, s_body_center], png)

        aceta_prop.setVisible(visibles[0])
        guide_path_prop.setVisible(visibles[1])
        guide_body_prop.setVisible(visibles[2])
        guide_slider_prop.setVisible(visibles[3])
        guide_mold_prop.setVisible(visibles[4])
        doc.save(file)


def LeftButtonPress(**kwargs):
    if kwargs['picked'] is voi_view:
        if plcut_box.text() == '请勾画切割范围':
            pt = voi_view.pickPt_FocalPlane()
            local_roi_pts.clear()
            local_roi_pts.append(pt)
            update_line_cut()


def LeftButtonPressMove(**kwargs):
    global spcut_center, pelvis_cs
    if kwargs['picked'] is voi_view:
        if plcut_box.text() == '请勾画切割范围':
            pt = voi_view.pickPt_Cell()

            for path_pt in local_roi_pts:
                if (path_pt == pt).all():
                    return

            local_roi_pts.append(pt)  # 添加拾取路径点
            update_line_cut()
        else:
            voi_view.mouseRotateFocal(**kwargs)
    elif kwargs['picked'] is pelvis_view:
        pelvis_view.mouseRotateFocal(**kwargs)
        if pelvis_MPP_box.text() == '确定':
            update_pelvis_MPP()
        elif pelvis_APP_box.text() == '确定':
            update_pelvis_APP()
    elif kwargs['picked'] in [spcut_prop, *spcut_y_props, *spcut_z_props]:
        spcut_center += kwargs['picked'].view().pickVt_FocalPlane()
        update_spcut()
        update_spcut_section()
    elif kwargs['picked'] in [cup_prop, cup_section_prop]:
        pt = pelvis_view.pickPt_FocalPlane()
        pt = vmi.ptOnPlane(pt, pelvis_cs.origin(), pelvis_view.cameraVt_Look())

        over = kwargs['picked'].view().pickVt_FocalPlane()
        if np.dot(pt - pelvis_cs.origin(), cup_cs.origin() - pelvis_cs.origin()) < 0:
            over = pelvis_cs.inv().mvt(over)
            over[0] *= -1
            over = pelvis_cs.mvt(over)

        cup_cs.setOrigin(cup_cs.origin() + over)
        update_cup()
        return True
    elif kwargs['picked'] is guide_slider_prop:
        pass  # TODO 是否支持鼠标拖动滑杆自由移动旋转？


def LeftButtonPressMoveRelease(**kwargs):
    if kwargs['picked'] is voi_view:
        if plcut_box.text() == '请勾画切割范围':
            plcut_box.draw_text('请耐心等待')
            plcut_voi_image()
            plcut_box.draw_text('线切割')

            local_roi_pts.clear()
            update_line_cut()


def LeftButtonPressRelease(**kwargs):
    global spcut_radius, pelvis_cs, cup_radius, cup_cs, cup_RA, cup_RI, bone_value
    global body_angle, body_xr, body_yr, kirs_radius
    if kwargs['picked'] is dicom_box:
        original_image = read_dicom()
        if original_image is not None:
            original_slice.setData(original_image)
            original_slice.setSlicePlaneOrigin_Center()
            original_slice.setSlicePlaneNormal_Coronal()
            original_view.setCamera_Coronal()
            original_view.setCamera_FitAll()
    elif kwargs['picked'] is original_slice:
        on_init_voi()
    elif kwargs['picked'] is bone_value_box:
        v = vmi.askInt(-1000, bone_value, 3000)
        if v is not None:
            bone_value = v
            bone_value_box.draw_text('骨阈值：{:.0f} HU'.format(bone_value))
            voi_volume.setOpacityScalar({bone_value - 1: 0, bone_value: 1})
    elif kwargs['picked'] is plcut_box:
        if plcut_box.text() == '线切割':
            plcut_box.draw_text('请勾画切割范围')
        elif plcut_box.text() == '请勾画切割范围':
            plcut_box.draw_text('线切割')
    elif kwargs['picked'] is spcut_box:
        spcut_box.draw_text('请耐心等待')
        spcut_voi_image()
        spcut_box.draw_text('球切割')
        update_spcut_section()
    elif kwargs['picked'] is spcut_visible_box:
        spcut_prop.visibleToggle()
        spcut_visible_box.draw_text(
            back_color=QColor().fromRgbF(0.4, 0.6, 1) if spcut_prop.visible() else QColor('black'))
    elif kwargs['picked'] is spcut_radius_box:
        r = vmi.askInt(5, spcut_radius, 50)
        if r is not None:
            spcut_radius = r
            spcut_radius_box.draw_text('球半径：{:.0f} mm'.format(spcut_radius))
            update_spcut()
            update_spcut_section()
    elif kwargs['picked'] is init_pelvis_box:
        init_pelvis_box.draw_text('请耐心等待')
        init_pelvis()
        update_cup_orientation()
        update_cup()
        init_pelvis_box.draw_text('创建骨盆')
    elif kwargs['picked'] is cup_radius_box:
        r = vmi.askInt(5, cup_radius, 50)
        if r is not None:
            cup_radius = r
            cup_radius_box.draw_text('半径：{:.0f} mm'.format(cup_radius))
            update_cup()
    elif kwargs['picked'] is cup_RA_box:
        r = vmi.askFloat(-15.0, cup_RA, 45.0, 1, 0.1)
        if r is not None:
            cup_RA = r
            cup_RA_box.draw_text('前倾角：{:.1f}°'.format(cup_RA))

            update_cup_orientation()
            update_cup()
    elif kwargs['picked'] is cup_RI_box:
        r = vmi.askFloat(0.0, cup_RI, 60.0, 1, 0.1)
        if r is not None:
            cup_RI = r
            cup_RI_box.draw_text('外展角：{:.1f}°'.format(cup_RI))

            update_cup_orientation()
            update_cup()
    elif kwargs['picked'] is cup_camera_sagittal_box:
        update_cup_camera_sagittal()
    elif kwargs['picked'] is cup_camera_coronal_box:
        update_cup_camera_coronal()
    elif kwargs['picked'] is cup_camera_axial_box:
        update_cup_camera_axial()
    elif kwargs['picked'] is cup_camera_RA_box:
        update_cup_camera_RA()
    elif kwargs['picked'] is cup_camera_RI_box:
        update_cup_camera_RI()
    elif kwargs['picked'] is cup_camera_plane_box:
        update_cup_camera_plane()
    elif kwargs['picked'] is pelvis_visible_box:
        pelvis_prop.visibleToggle()
        pelvis_visible_box.draw_text(
            back_color=QColor().fromRgbF(1, 1, 0.6) if pelvis_prop.visible() else QColor('black'))
    elif kwargs['picked'] is metal_visible_box:
        metal_prop.visibleToggle()
        metal_visible_box.draw_text(
            back_color=QColor().fromRgbF(1, 0.4, 0.4) if metal_prop.visible() else QColor('black'))
    elif kwargs['picked'] is pelvis_slice_box:
        if pelvis_slice_box.text() == '三维':
            pelvis_slice_box.draw_text('断层')
            cup_prop.setVisible(False)
            pelvis_prop.setVisible(False)
            cup_section_prop.setVisible(True)
            pelvis_slice.setVisible(True)

            pelvis_slice.setSlicePlane(cup_cs.origin(), pelvis_view.cameraVt_Look())
            pd = vmi.pdCut_Implicit(cup_prop.data(), pelvis_slice.slicePlane())
            cup_section_prop.setData(pd)
        elif pelvis_slice_box.text() == '断层':
            pelvis_slice_box.draw_text('三维')
            cup_prop.setVisible(True)
            pelvis_prop.setVisible(True)
            cup_section_prop.setVisible(False)
            pelvis_slice.setVisible(False)
    elif kwargs['picked'] is pelvis_MPP_box:
        if pelvis_MPP_box.text() == '配准对称面':
            pelvis_MPP_box.draw_text('确定')
            update_pelvis_MPP()
            pelvis_MPP_prop.setVisible(True)
        elif pelvis_MPP_box.text() == '确定':
            pelvis_MPP_box.draw_text('配准对称面')
            pelvis_MPP_prop.setVisible(False)
    elif kwargs['picked'] is pelvis_APP_box:
        if pelvis_APP_box.text() == '配准前平面':
            pelvis_APP_box.draw_text('确定')
            update_pelvis_APP()
            pelvis_APP_prop.setVisible(True)
        elif pelvis_APP_box.text() == '确定':
            pelvis_APP_box.draw_text('配准前平面')
            pelvis_APP_prop.setVisible(False)
    elif kwargs['picked'] is init_guide_box:
        init_guide_box.draw_text('请耐心等待')
        init_guide()
        init_guide_box.draw_text('创建导板')
    elif kwargs['picked'] is aceta_visible_box:
        aceta_prop.visibleToggle()
        aceta_visible_box.draw_text(
            back_color=QColor().fromRgbF(1, 1, 0.6) if aceta_prop.visible() else QColor('black'))
    elif kwargs['picked'] is guide_body_visible_box:
        guide_body_prop.visibleToggle()
        guide_body_visible_box.draw_text(
            back_color=QColor().fromRgbF(0.4, 0.6, 1) if guide_body_prop.visible() else QColor('black'))
    elif kwargs['picked'] is guide_path_visible_box:
        guide_path_prop.visibleToggle()
        guide_path_visible_box.draw_text(
            back_color=QColor().fromRgbF(0.4, 1, 0.4) if guide_path_prop.visible() else QColor('black'))
    elif kwargs['picked'] is guide_slider_visible_box:
        guide_slider_prop.visibleToggle()
        guide_slider_visible_box.draw_text(
            back_color=QColor().fromRgbF(0.6, 0.8, 1) if guide_slider_prop.visible() else QColor('black'))
    elif kwargs['picked'] is guide_mold_visible_box:
        guide_mold_prop.visibleToggle()
        guide_mold_visible_box.draw_text(
            back_color=QColor().fromRgbF(1, 0.4, 0.4) if guide_mold_prop.visible() else QColor('black'))
    elif kwargs['picked'] is guide_update_box:
        guide_update_box.draw_text('请耐心等待')
        update_guide_path()
        update_guide_plate()
        guide_update_box.draw_text('更新导板')
    elif kwargs['picked'] is body_angle_box:
        r = vmi.askInt(-45, body_angle, 45)
        if r is not None:
            body_angle = r
            body_angle_box.draw_text('主体方位：{}°'.format(body_angle))
            update_guide_path()
    elif kwargs['picked'] is body_xr_box:
        r = vmi.askInt(10, body_xr, 50)
        if r is not None:
            body_xr = r
            body_xr_box.draw_text('主体长径：{:.0f} mm'.format(body_xr))
            update_guide_path()
    elif kwargs['picked'] is body_yr_box:
        r = vmi.askInt(10, body_yr, 50)
        if r is not None:
            body_yr = r
            body_yr_box.draw_text('主体宽径：{:.0f} mm'.format(body_yr))
            update_guide_path()
    elif kwargs['picked'] is slider_length_box:
        global slider_length
        r = vmi.askInt(10, slider_length, 90)
        if r is not None:
            slider_length = r
            slider_length_box.draw_text('滑杆长度：{:.0f} mm'.format(slider_length))
            update_guide_path()
    elif kwargs['picked'] is kirs_radius_box:
        r = vmi.askFloat(0.5, kirs_radius, 2.5, 1, 0.1)
        if r is not None:
            kirs_radius = r
            kirs_radius_box.draw_text('导针半径：{:.1f} mm'.format(kirs_radius))
            update_guide_path()
    elif kwargs['picked'] is output_box:
        p = vmi.askDirectory('vmi')
        if p is not None:
            global UDI, UDI_time

            try:
                vmi.pdSaveFile_STL(aceta_prop.data(), str(pathlib.Path(p) / ('{} {}'.format(UDI, ' 髋臼.stl'))))
                vmi.pdSaveFile_STL(guide_mold_prop.data(), str(pathlib.Path(p) / ('{} {}'.format(UDI, ' 配模.stl'))))
                vmi.pdSaveFile_STL(guide_body_prop.data(), str(pathlib.Path(p) / ('{} {}'.format(UDI, ' 定位板.stl'))))
                vmi.pdSaveFile_STL(guide_slider_prop.data(), str(pathlib.Path(p) / ('{} {}'.format(UDI, ' 滑杆.stl'))))
                save_docx(str(pathlib.Path(p) / ('{} {} {} {} {}.docx'.format(
                    UDI, '设计确认单', patient_name, 'L' if LR > 0 else 'R', time.strftime('%Y-%m-%d %H-%M-%S', UDI_time)))))
            except Exception as e:
                vmi.askInfo(str(e))


def MidButtonPressMove(**kwargs):
    if kwargs['picked'] in [pelvis_view, pelvis_slice]:
        pelvis_view.mousePan()
        if pelvis_MPP_box.text() == '确定':
            update_pelvis_MPP()
        elif pelvis_APP_box.text() == '确定':
            update_pelvis_APP()


def RightButtonPressMove(**kwargs):
    if kwargs['picked'] in [pelvis_view, pelvis_slice]:
        pelvis_view.mouseZoom()
        if pelvis_MPP_box.text() == '确定':
            update_pelvis_MPP()
        elif pelvis_APP_box.text() == '确定':
            update_pelvis_APP()


def NoButtonWheel(**kwargs):
    global bone_value, spcut_radius, cup_radius, cup_RA, cup_RI
    global body_angle, body_xr, body_yr, kirs_radius
    if kwargs['picked'] is bone_value_box:
        bone_value = min(max(bone_value + 10 * kwargs['delta'], -1000), 3000)
        bone_value_box.draw_text('骨阈值：{:.0f} HU'.format(bone_value))
        voi_volume.setOpacityScalar({bone_value - 1: 0, bone_value: 1})
    elif kwargs['picked'] is spcut_radius_box:
        spcut_radius = min(max(spcut_radius + kwargs['delta'], 5), 50)
        spcut_radius_box.draw_text('球半径：{:.0f} mm'.format(spcut_radius))
        update_spcut()
        update_spcut_section()
    elif kwargs['picked'] is pelvis_view:
        pelvis_view.mouseRotateLook(**kwargs)
        if pelvis_MPP_box.text() == '确定':
            update_pelvis_MPP()
        elif pelvis_APP_box.text() == '确定':
            update_pelvis_APP()
    elif kwargs['picked'] is cup_radius_box:
        cup_radius = min(max(cup_radius + kwargs['delta'], 5), 50)
        cup_radius_box.draw_text('半径：{:.0f} mm'.format(cup_radius))
        update_cup()
    elif kwargs['picked'] is cup_RA_box:
        cup_RA = min(max(cup_RA + 0.1 * kwargs['delta'], -15), 45)
        cup_RA_box.draw_text('前倾角：{:.1f}°'.format(cup_RA))
        update_cup_orientation()
        update_cup()
    elif kwargs['picked'] is cup_RI_box:
        cup_RI = min(max(cup_RI + 0.1 * kwargs['delta'], 0), 60)
        cup_RI_box.draw_text('外展角：{:.1f}°'.format(cup_RI))
        update_cup_orientation()
        update_cup()
    elif kwargs['picked'] is pelvis_slice:
        update_cup()
    elif kwargs['picked'] is body_angle_box:
        body_angle = min(max(body_angle + kwargs['delta'], -45), 45)
        body_angle_box.draw_text('主体方位：{}°'.format(body_angle))
        update_guide_path()
    elif kwargs['picked'] is body_xr_box:
        body_xr = min(max(body_xr + kwargs['delta'], 10), 50)
        body_xr_box.draw_text('主体长径：{:.0f} mm'.format(body_xr))
        update_guide_path()
    elif kwargs['picked'] is body_yr_box:
        body_yr = min(max(body_yr + kwargs['delta'], 10), 50)
        body_yr_box.draw_text('主体宽径：{:.0f} mm'.format(body_yr))
        update_guide_path()
    elif kwargs['picked'] is slider_length_box:
        global slider_length
        slider_length = min(max(slider_length + kwargs['delta'], 10), 90)
        slider_length_box.draw_text('滑杆长度：{:.0f} mm'.format(slider_length))
        update_guide_path()
    elif kwargs['picked'] is kirs_radius_box:
        kirs_radius = min(max(kirs_radius + 0.1 * kwargs['delta'], 0.5), 2.5)
        kirs_radius_box.draw_text('导针半径：{:.1f} mm'.format(kirs_radius))
        update_guide_path()


def return_globals():
    return globals()


if __name__ == '__main__':
    global original_view, voi_view, spcut_y_views, spcut_z_views, pelvis_view, guide_view
    main = vmi.Main(return_globals)
    main.setAppName('全髋关节置换(THA)规划')
    main.setAppVersion(vmi.version)
    main.excludeKeys += ['main', 'i', 'box', 'prop', 'voi_image']

    select = vmi.askButtons(['新建', '打开'], title=main.appName())
    if select is None:
        vmi.appexit()

    if select == '打开':
        open_file = vmi.askOpenFile(nameFilter='*.vmi', title='打开存档')
        if open_file is not None:
            main.loads(pathlib.Path(open_file).read_bytes())
        else:
            vmi.appexit()
    elif select == '新建':
        patient_name = str()

        # 0 原始图像
        original_target, LR = np.zeros(3), 1
        original_view = vmi.View()

        original_slice = vmi.ImageSlice(original_view)  # 断层显示
        original_slice.setColorWindow_Bone()
        original_slice.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]

        dicom_box = vmi.TextBox(original_view, text='DICOM', pickable=True,
                                size=[0.2, 0.04], pos=[0, 0.04], anchor=[0, 0])
        dicom_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]

        patient_name_box = vmi.TextBox(original_view, text='姓名', visible=False,
                                       size=[0.2, 0.04], pos=[0, 0.1], anchor=[0, 0])
        patient_LR_box = vmi.TextBox(original_view, text='患侧', visible=False,
                                     size=[0.2, 0.04], pos=[0, 0.14], anchor=[0, 0])

        # 1 目标区域
        voi_view = vmi.View()
        voi_view.mouse['LeftButton']['Press'] = [LeftButtonPress]
        voi_view.mouse['LeftButton']['PressMove'] = [LeftButtonPressMove]
        voi_view.mouse['LeftButton']['PressMoveRelease'] = [LeftButtonPressMoveRelease]

        bone_value, target_value = 200, -1100

        bone_value_box = vmi.TextBox(voi_view, text='骨阈值：{:.0f} HU'.format(bone_value),
                                     size=[0.2, 0.04], pos=[0, 0.04], anchor=[0, 0], pickable=True)
        bone_value_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]
        bone_value_box.mouse['NoButton']['Wheel'] = [NoButtonWheel]

        voi_size, voi_center, voi_origin, voi_cs = np.zeros(3), np.zeros(3), np.zeros(3), vmi.CS4x4()
        voi_image = vtk.vtkImageData()

        voi_volume = vmi.ImageVolume(voi_view, pickable=True)
        voi_volume.setOpacityScalar({bone_value - 1: 0, bone_value: 1})
        voi_volume.setColor({bone_value: [1, 1, 0.6]})

        # 线切割
        local_roi_pts = []
        plcut_prop = vmi.PolyActor(voi_view, color=[1, 0.6, 0.6], line_width=3, always_on_top=True)

        # 球切割
        spcut_center, spcut_radius, spcut_length = np.zeros(3), 22, 200
        spcut_prop = vmi.PolyActor(voi_view, color=[0.4, 0.6, 1], pickable=True)
        spcut_prop.mouse['LeftButton']['PressMove'] = [LeftButtonPressMove]

        plcut_box = vmi.TextBox(voi_view, text='线切割', size=[0.2, 0.04], pos=[0, 0.1], anchor=[0, 0], pickable=True)
        plcut_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]

        spcut_box = vmi.TextBox(voi_view, text='球切割', size=[0.2, 0.04], pos=[0, 0.16], anchor=[0, 0], pickable=True)
        spcut_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]

        spcut_visible_box = vmi.TextBox(voi_view, size=[0.01, 0.04], pos=[0.2, 0.16], anchor=[1, 0],
                                        back_color=QColor().fromRgbF(0.4, 0.6, 1), pickable=True)
        spcut_visible_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]

        spcut_radius_box = vmi.TextBox(voi_view, text='球半径：{:.0f} mm'.format(spcut_radius),
                                       size=[0.2, 0.04], pos=[0, 0.20], anchor=[0, 0], pickable=True)
        spcut_radius_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]
        spcut_radius_box.mouse['NoButton']['Wheel'] = [NoButtonWheel]

        # 234 球切割局部
        spcut_y_views = [vmi.View(), vmi.View(), vmi.View()]
        spcut_z_views = [vmi.View(), vmi.View(), vmi.View()]

        for i in spcut_y_views + spcut_z_views:
            i.mouse['LeftButton']['PressMove'] = [i.mouseBlock]

        spcut_y_boxs = [vmi.TextBox(spcut_y_views[i], text=['斜冠状位', '正冠状位', '斜冠状位'][i],
                                    size=[0.2, 0.1], pos=[1, 1], anchor=[1, 1]) for i in range(3)]
        spcut_z_boxs = [vmi.TextBox(spcut_z_views[i], text=['斜横断位', '正横断位', '斜横断位'][i],
                                    size=[0.2, 0.1], pos=[1, 1], anchor=[1, 1]) for i in range(3)]

        spcut_y_slices = [vmi.ImageSlice(v) for v in spcut_y_views]
        spcut_z_slices = [vmi.ImageSlice(v) for v in spcut_z_views]

        for i in spcut_y_slices + spcut_z_slices:
            i.bindData(voi_volume)
            i.mouse['NoButton']['Wheel'] = [i.mouseBlock]

        spcut_y_props = [vmi.PolyActor(v, color=[0.4, 0.6, 1], opacity=0.5, pickable=True) for v in spcut_y_views]
        spcut_z_props = [vmi.PolyActor(v, color=[0.4, 0.6, 1], opacity=0.5, pickable=True) for v in spcut_z_views]

        for i in spcut_y_props + spcut_z_props:
            i.mouse['LeftButton']['PressMove'] = [LeftButtonPressMove]

        init_pelvis_box = vmi.TextBox(voi_view, text='创建骨盆', fore_color=QColor('white'), back_color=QColor('crimson'),
                                      bold=True, size=[0.2, 0.04], pos=[1, 0.04], anchor=[1, 0], pickable=True)
        init_pelvis_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]

        # 5 骨盆规划
        pelvis_view = vmi.View()
        pelvis_view.mouse['LeftButton']['PressMove'] = [LeftButtonPressMove]
        pelvis_view.mouse['MidButton']['PressMove'] = [MidButtonPressMove]
        pelvis_view.mouse['RightButton']['PressMove'] = [RightButtonPressMove]
        pelvis_view.mouse['NoButton']['Wheel'] = [NoButtonWheel]

        pelvis_prop = vmi.PolyActor(pelvis_view, color=[1, 1, 0.6])
        metal_prop = vmi.PolyActor(pelvis_view, color=[1, 0.4, 0.4])

        pelvis_cs, cup_cs = vmi.CS4x4(), vmi.CS4x4()
        cup_radius, cup_RA, cup_RI = 22, 20, 40
        cup_prop = vmi.PolyActor(pelvis_view, color=[0.4, 0.6, 1], line_width=3, pickable=True)
        cup_prop.mouse['LeftButton']['PressMove'] = [LeftButtonPressMove]

        cup_radius_box = vmi.TextBox(pelvis_view, text='半径：{:.0f} mm'.format(cup_radius), pickable=True,
                                     size=[0.2, 0.04], pos=[0, 0.04], anchor=[0, 0])
        cup_radius_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]
        cup_radius_box.mouse['NoButton']['Wheel'] = [NoButtonWheel]

        cup_RA_box = vmi.TextBox(pelvis_view, text='前倾角：{:.1f}°'.format(cup_RA), pickable=True,
                                 size=[0.2, 0.04], pos=[0, 0.1], anchor=[0, 0])
        cup_RA_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]
        cup_RA_box.mouse['NoButton']['Wheel'] = [NoButtonWheel]

        cup_RI_box = vmi.TextBox(pelvis_view, text='外展角：{:.1f}°'.format(cup_RI), pickable=True,
                                 size=[0.2, 0.04], pos=[0, 0.14], anchor=[0, 0])
        cup_RI_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]
        cup_RI_box.mouse['NoButton']['Wheel'] = [NoButtonWheel]

        pelvis_slice = vmi.ImageSlice(pelvis_view, visible=False)
        pelvis_slice.bindData(voi_volume)
        pelvis_slice.mouse['MidButton']['PressMove'] = [MidButtonPressMove]
        pelvis_slice.mouse['RightButton']['PressMove'] = [RightButtonPressMove]
        pelvis_slice.mouse['NoButton']['Wheel'] += [NoButtonWheel]

        original_slice.bindColorWindow(spcut_y_slices + spcut_z_slices + [pelvis_slice])

        cup_section_prop = vmi.PolyActor(pelvis_view, color=[0.4, 0.6, 1], line_width=3, visible=False, pickable=True)
        cup_section_prop.mouse['LeftButton']['PressMove'] = [LeftButtonPressMove]

        pelvis_slice_box = vmi.TextBox(pelvis_view, text='三维', pickable=True,
                                       size=[0.2, 0.04], pos=[0, 0.2], anchor=[0, 0])
        pelvis_slice_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]

        pelvis_MPP_box = vmi.TextBox(pelvis_view, text='配准对称面', pickable=True,
                                     size=[0.2, 0.04], pos=[0, 0.26], anchor=[0, 0])
        pelvis_MPP_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]

        pelvis_APP_box = vmi.TextBox(pelvis_view, text='配准前平面', pickable=True,
                                     size=[0.2, 0.04], pos=[0, 0.3], anchor=[0, 0])
        pelvis_APP_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]

        cup_camera_sagittal_box = vmi.TextBox(pelvis_view, text='矢状', pickable=True,
                                              size=[0.06, 0.04], pos=[0, 0.36], anchor=[0, 0])
        cup_camera_sagittal_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]

        cup_camera_coronal_box = vmi.TextBox(pelvis_view, text='冠状', pickable=True,
                                             size=[0.06, 0.04], pos=[0.06, 0.36], anchor=[0, 0])
        cup_camera_coronal_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]

        cup_camera_axial_box = vmi.TextBox(pelvis_view, text='横断', pickable=True,
                                           size=[0.06, 0.04], pos=[0.12, 0.36], anchor=[0, 0])
        cup_camera_axial_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]

        cup_camera_RA_box = vmi.TextBox(pelvis_view, text='前倾', pickable=True,
                                        size=[0.06, 0.04], pos=[0, 0.4], anchor=[0, 0])
        cup_camera_RA_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]

        cup_camera_RI_box = vmi.TextBox(pelvis_view, text='外展', pickable=True,
                                        size=[0.06, 0.04], pos=[0.06, 0.4], anchor=[0, 0])
        cup_camera_RI_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]

        cup_camera_plane_box = vmi.TextBox(pelvis_view, text='正视', pickable=True,
                                           size=[0.06, 0.04], pos=[0.12, 0.4], anchor=[0, 0])
        cup_camera_plane_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]

        pelvis_visible_box = vmi.TextBox(pelvis_view, size=[0.02, 0.04], pos=[0.18, 0.36], anchor=[0, 0],
                                         back_color=QColor().fromRgbF(1, 1, 0.6), pickable=True)
        pelvis_visible_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]

        metal_visible_box = vmi.TextBox(pelvis_view, size=[0.02, 0.04], pos=[0.18, 0.4], anchor=[0, 0],
                                        back_color=QColor().fromRgbF(1, 0.4, 0.4), pickable=True)
        metal_visible_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]

        pelvis_MPP_prop = vmi.PolyActor(pelvis_view, visible=False, color=[1, 0.4, 0.4], repres='points')
        pelvis_APP_prop = vmi.PolyActor(pelvis_view, visible=False, color=[1, 0.4, 0.4], line_width=3,
                                        always_on_top=True)

        init_guide_box = vmi.TextBox(pelvis_view, text='创建导板', fore_color=QColor('white'), back_color=QColor('crimson'),
                                     bold=True, size=[0.2, 0.04], pos=[1, 0.04], anchor=[1, 0], pickable=True)
        init_guide_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]

        # 8 导板
        guide_view = vmi.View()
        guide_view.bindCamera([pelvis_view])

        aceta_prop = vmi.PolyActor(guide_view, color=[1, 1, 0.6])

        guide_path = vmi.TopoDS_Shape()  # 引导线
        guide_path_prop = vmi.PolyActor(guide_view, color=[0.4, 1, 0.4], line_width=3)

        guide_body = vmi.TopoDS_Shape()  # 主板
        guide_body_prop = vmi.PolyActor(guide_view, color=[0.4, 0.6, 1])

        guide_slider = vmi.TopoDS_Shape()  # 滑杆
        guide_slider_prop = vmi.PolyActor(guide_view, color=[0.6, 0.8, 1])
        guide_slider_prop.mouse['LeftButton']['PressMove'] = [LeftButtonPressMove]

        guide_mold = vmi.TopoDS_Shape()  # 配模
        guide_mold_prop = vmi.PolyActor(guide_view, color=[1, 0.4, 0.4])

        body_angle = 0  # 主体方位
        body_xr, body_yr = 20, 15  # 主体长径宽径，臼窝匹配块
        head_xr = 9  # 头部长径，臼缘匹配块
        slider_length = 50  # 滑杆长度
        kirs_radius = 1  # 导向孔半径

        body_angle_box = vmi.TextBox(guide_view, text='主体方位：{}°'.format(body_angle), pickable=True,
                                     size=[0.2, 0.04], pos=[0, 0.04], anchor=[0, 0])
        body_angle_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]
        body_angle_box.mouse['NoButton']['Wheel'] = [NoButtonWheel]

        body_xr_box = vmi.TextBox(guide_view, text='主体长径：{:.0f} mm'.format(body_xr), pickable=True,
                                  size=[0.2, 0.04], pos=[0, 0.08], anchor=[0, 0])
        body_xr_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]
        body_xr_box.mouse['NoButton']['Wheel'] = [NoButtonWheel]

        body_yr_box = vmi.TextBox(guide_view, text='主体宽径：{:.0f} mm'.format(body_yr), pickable=True,
                                  size=[0.2, 0.04], pos=[0, 0.12], anchor=[0, 0])
        body_yr_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]
        body_yr_box.mouse['NoButton']['Wheel'] = [NoButtonWheel]

        slider_length_box = vmi.TextBox(guide_view, text='滑杆长度：{:.0f} mm'.format(slider_length), pickable=True,
                                        size=[0.2, 0.04], pos=[0, 0.16], anchor=[0, 0])
        slider_length_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]
        slider_length_box.mouse['NoButton']['Wheel'] = [NoButtonWheel]

        kirs_radius_box = vmi.TextBox(guide_view, text='导针半径：{:.1f} mm'.format(kirs_radius), pickable=True,
                                      size=[0.2, 0.04], pos=[0, 0.20], anchor=[0, 0])
        kirs_radius_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]
        kirs_radius_box.mouse['NoButton']['Wheel'] = [NoButtonWheel]

        guide_update_box = vmi.TextBox(guide_view, text='更新导板', pickable=True,
                                       size=[0.10, 0.04], pos=[0, 0.26], anchor=[0, 0])
        guide_update_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]

        aceta_visible_box = vmi.TextBox(guide_view, pickable=True, back_color=QColor().fromRgbF(1, 1, 0.6),
                                        size=[0.02, 0.04], pos=[0.10, 0.26], anchor=[0, 0])
        aceta_visible_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]

        guide_path_visible_box = vmi.TextBox(guide_view, pickable=True, back_color=QColor().fromRgbF(0.4, 1, 0.4),
                                             size=[0.02, 0.04], pos=[0.12, 0.26], anchor=[0, 0])
        guide_path_visible_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]

        guide_body_visible_box = vmi.TextBox(guide_view, pickable=True, back_color=QColor().fromRgbF(0.4, 0.6, 1),
                                             size=[0.02, 0.04], pos=[0.14, 0.26], anchor=[0, 0])
        guide_body_visible_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]

        guide_slider_visible_box = vmi.TextBox(guide_view, pickable=True, back_color=QColor().fromRgbF(0.6, 0.8, 1),
                                               size=[0.02, 0.04], pos=[0.16, 0.26], anchor=[0, 0])
        guide_slider_visible_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]

        guide_mold_visible_box = vmi.TextBox(guide_view, pickable=True, back_color=QColor().fromRgbF(1, 0.4, 0.4),
                                             size=[0.02, 0.04], pos=[0.18, 0.26], anchor=[0, 0])
        guide_mold_visible_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]

        output_box = vmi.TextBox(guide_view, text='导出方案', fore_color=QColor('white'), back_color=QColor('crimson'),
                                 bold=True, size=[0.2, 0.04], pos=[1, 0.04], anchor=[1, 0], pickable=True)
        output_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]

        for v in [original_view, voi_view, *spcut_y_views, *spcut_z_views, pelvis_view, guide_view]:
            v.setEnabled(False)
        original_view.setEnabled(True)
        guide_view.setEnabled(True)

    # 视图布局
    for v in [original_view, voi_view, *spcut_y_views, *spcut_z_views, pelvis_view, guide_view]:
        v.setMinimumWidth(round(0.5 * main.screenWidth()))

    for v in spcut_y_views + spcut_z_views:
        v.setMinimumWidth(round(0.25 * main.screenWidth()))

    original_view.setParent(main.scrollArea())
    main.layout().addWidget(original_view, 0, 0, 3, 1)
    main.layout().addWidget(voi_view, 0, 1, 3, 1)
    main.layout().addWidget(spcut_y_views[0], 0, 2, 1, 1)
    main.layout().addWidget(spcut_y_views[1], 1, 2, 1, 1)
    main.layout().addWidget(spcut_y_views[2], 2, 2, 1, 1)
    main.layout().addWidget(spcut_z_views[0], 0, 3, 1, 1)
    main.layout().addWidget(spcut_z_views[1], 1, 3, 1, 1)
    main.layout().addWidget(spcut_z_views[2], 2, 3, 1, 1)
    main.layout().addWidget(pelvis_view, 0, 4, 3, 1)
    main.layout().addWidget(guide_view, 0, 5, 3, 1)

    vmi.appexec(main)  # 执行主窗口程序
    vmi.appexit()  # 清理并退出程序
