import vmi
import vtk
import pydicom
import numpy as np
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from numba import jit
import pathlib
import time
import pickle


def read_dicom():
    dcmdir = vmi.askDirectory('DICOM')  # 用户选择文件夹

    if dcmdir is not None:  # 判断用户选中了有效文件夹并点击了确认
        series_list = vmi.sortSeries(dcmdir)  # 将文件夹及其子目录包含的所有DICOM文件分类到各个系列

        if len(series_list) > 0:  # 判断该文件夹内包含有效的DICOM系列
            series = vmi.askSeries(series_list)  # 用户选择DICOM系列

            if series is not None:  # 判断用户选中了有效系列并点击了确认
                with pydicom.dcmread(series.filenames()[0]) as ds:
                    global patient_name
                    patient_name = ds.PatientName
                    patient_name_box.draw_text('姓名：{}'.format(patient_name))
                    patient_name_box.setVisible(True)
                return series.read()  # 读取DICOM系列为图像数据


def on_init_voi():
    size = vmi.askInt(1, 300, 1000, suffix='mm', title='请输入目标区域尺寸')
    if size is not None:
        global original_LR, original_target, voi_size, voi_center, spcut_center
        original_target = original_view.pickPt_Cell()
        voi_center = np.array([vmi.imCenter(original_image)[0], original_target[1], original_target[2]])
        voi_size = np.array([vmi.imSize(original_image)[0], size, size])
        init_voi()

        original_LR = 1 if original_target[0] > voi_center[0] else -1
        patient_LR_box.draw_text('患侧：{}'.format('左' if original_LR > 0 else '右'))
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
    global voi_size, voi_center, voi_origin, voi_cs
    voi_origin = voi_center - 0.5 * voi_size
    voi_cs = vmi.CS4x4(origin=voi_origin)

    global voi_image
    voi_image = vmi.imReslice(original_image, voi_cs, voi_size, -1024)
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
    if len(plcut_pts) > 1:
        plcut_prop.setData(vmi.ccWire(vmi.ccSegments(plcut_pts, True)))
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
    global voi_image

    cs = voi_view.cameraCS()
    d = vmi.imSize_Vt(voi_image, cs.axis(2))
    pts = [vmi.ptOnPlane(pt, vmi.imCenter(voi_image), cs.axis(2)) for pt in plcut_pts]
    pts = [pt - d * cs.axis(2) for pt in pts]
    sh = vmi.ccFace(vmi.ccWire(vmi.ccSegments(pts, True)))
    sh = vmi.ccPrism(sh, cs.axis(2), 2 * d)

    mask = vmi.imStencil_PolyData(vmi.ccPd_Sh(sh),
                                  vmi.imOrigin(voi_image),
                                  vmi.imSpacing(voi_image),
                                  vmi.imExtent(voi_image))
    mask_ary = vmi.imArray_VTK(mask)
    voi_ary = vmi.imArray_VTK(voi_image)
    ary_mask(voi_ary, mask_ary, bone_value, target_value)
    voi_image = vmi.imVTK_Array(voi_ary, vmi.imOrigin(voi_image), vmi.imSpacing(voi_image))
    voi_volume.setData(voi_image)

    for v in spcut_z_views + spcut_y_views:
        v.updateInTime()


def spcut_voi_image():
    global voi_image
    spcut_image = vmi.imStencil_PolyData(spcut_prop.data(),
                                         vmi.imOrigin(voi_image),
                                         vmi.imSpacing(voi_image),
                                         vmi.imExtent(voi_image))
    spcut_ary = vmi.imArray_VTK(spcut_image)
    voi_ary = vmi.imArray_VTK(voi_image)

    ary_mask(voi_ary, spcut_ary, bone_value, target_value)
    voi_image = vmi.imVTK_Array(voi_ary, vmi.imOrigin(voi_image), vmi.imSpacing(voi_image))
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
        y_cs[i].origin(spcut_center - y_cs[i].mpt([hwidth, hheight, 0]))
        z_cs[i].origin(spcut_center - z_cs[i].mpt([hwidth, hheight, 0]))

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
    pd = vmi.imIsosurface(voi_image, bone_value)
    pelvis_prop.setData(pd)

    pelvis_view.setCamera_Coronal()
    pelvis_view.setCamera_FitAll()
    pelvis_view.setEnabled(True)

    origin = np.array(pelvis_prop.data().GetCenter())
    pelvis_cs.origin(origin)
    cup_cs.origin(original_target)
    xray_view.setEnabled(True)


def update_pelvis_MPP():
    global pelvis_cs
    vr = pelvis_view.cameraVt_Right()
    vr = vr if np.dot(vr, np.array([1, 0, 0])) >= 0 else -vr
    if vmi.vtAngle(vr, pelvis_cs.axis(1)) < 1 or vmi.vtAngle(vr, pelvis_cs.axis(1)) > 179:
        return

    pelvis_cs.axis(0, vr)
    pelvis_cs.orthogonalize([2, 0])
    update_cup_orientation()
    update_cup()

    origin = pelvis_view.pickFPlane([0.5 * pelvis_view.width(), 0.5 * pelvis_view.height()])
    pelvis_cs.origin(origin)
    cs = vmi.CS4x4().reflect(pelvis_cs.axis(0), pelvis_cs.origin())
    pd = vmi.pdMatrix(pelvis_prop.data(), cs.matrix4x4())
    pelvis_MPP_prop.setData(pd)


def update_pelvis_APP():
    global pelvis_cs
    vr = pelvis_view.cameraVt_Right()
    vr = vr if np.dot(vr, np.array([0, 1, 0])) >= 0 else -vr
    if vmi.vtAngle(vr, pelvis_cs.axis(0)) < 1 or vmi.vtAngle(vr, pelvis_cs.axis(0)) > 179:
        return

    pelvis_cs.axis(1, vr)
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
    cup_axis = -cs.axis(2) * np.array([original_LR, 1, 1])

    cup_cs.axis(1, pelvis_cs.axis(1))
    cup_cs.axis(2, cup_axis)
    cup_cs.orthogonalize([0, 1])
    cup_cs.axis(0, -original_LR * cup_cs.axis(0))

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


def update_xray_pelvis():
    cs = pelvis_view.cameraCS()
    pelvis_left_top = pelvis_view.pickFPlane([0, 0])
    pelvis_right_top = pelvis_view.pickFPlane([pelvis_view.width(), 0])
    pelvis_left_bottom = pelvis_view.pickFPlane([0, pelvis_view.height()])

    xray_left_top = xray_view.pickFPlane([0, 0])
    xray_right_top = xray_view.pickFPlane([xray_view.width(), 0])
    xray_left_bottom = xray_view.pickFPlane([0, xray_view.height()])

    global xray_cs
    xray_cs = xray_view.cameraCS()
    xray_cs.axis(0, xray_cs.axis(0) * np.linalg.norm(xray_left_top - xray_right_top) /
                 np.linalg.norm(pelvis_left_top - pelvis_right_top))
    xray_cs.axis(1, xray_cs.axis(1) * np.linalg.norm(xray_left_top - xray_left_bottom) /
                 np.linalg.norm(pelvis_left_top - pelvis_left_bottom))
    xray_cs = xray_cs.mcs(vmi.CS4x4(axis2=[0, 0, 0]).mcs(cs.inv()))

    pd = vmi.pdMatrix(pelvis_prop.data(), xray_cs.matrix4x4())
    xray_pelvis_prop.setData(pd)

    global pelvis_cs
    vr = pelvis_view.cameraVt_Right()
    vr = vr if np.dot(vr, np.array([0, 1, 0])) >= 0 else -vr
    if vmi.vtAngle(vr, pelvis_cs.axis(0)) < 1 or vmi.vtAngle(vr, pelvis_cs.axis(0)) > 179:
        return

    pelvis_cs.axis(1, vr)
    pelvis_cs.orthogonalize([2, 0])
    update_cup_orientation()
    update_cup()

    global ctray_cs, ctray_size
    ctray_cs = pelvis_view.cameraCS()
    ctray_size[2] = vmi.imSize_Vt(voi_image, cs.axis(2))

    pt = vmi.imCenter(voi_image) - 0.5 * ctray_size[2] * cs.axis(2)
    ctray_cs.origin(vmi.ptOnPlane(cs.origin(), pt, cs.axis(2)))

    ctray_size[0] = np.linalg.norm(pelvis_left_top - pelvis_right_top)
    ctray_size[1] = np.linalg.norm(pelvis_left_top - pelvis_left_bottom)


def update_ctray():
    image_blend = vmi.imReslice_Blend(voi_image, cs=ctray_cs, size=ctray_size,
                                      back_scalar=-1024, scalar_min=bone_value - 300)
    ctray_slice.setData(image_blend)
    ctray_slice.window(width=350, level=bone_value - 150)


def init_guide():
    global voi_image
    size = np.array([5 * cup_radius, 5 * cup_radius, 5 * cup_radius])
    cs = vmi.CS4x4(origin=cup_cs.origin() - 0.5 * size)
    image = vmi.imReslice(voi_image, cs, size, -1024)
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
    cs = vmi.CS4x4(axis1=-pelvis_cs.axis(2), axis2=-original_LR * pelvis_cs.axis(0))
    cs.orthogonalize([0])
    cs.origin(cup_cs.origin() - 2.5 * cup_radius * cs.axis(0) - 2.5 * cup_radius * cs.axis(1))
    pelvis_view.setCamera_FPlane(cs, 5 * cup_radius)
    pelvis_view.updateInTime()


def update_cup_camera_coronal():
    cs = vmi.CS4x4(axis1=-pelvis_cs.axis(2), axis2=pelvis_cs.axis(1))
    cs.orthogonalize([0])
    cs.origin(cup_cs.origin() - 2.5 * cup_radius * cs.axis(0) - 2.5 * cup_radius * cs.axis(1))
    pelvis_view.setCamera_FPlane(cs, 5 * cup_radius)
    pelvis_view.updateInTime()


def update_cup_camera_axial():
    cs = vmi.CS4x4(axis1=pelvis_cs.axis(1), axis2=pelvis_cs.axis(2))
    cs.orthogonalize([0])
    cs.origin(cup_cs.origin() - 2.5 * cup_radius * cs.axis(0) - 2.5 * cup_radius * cs.axis(1))
    pelvis_view.setCamera_FPlane(cs, 5 * cup_radius)
    pelvis_view.updateInTime()


def update_cup_camera_RA():
    cs = vmi.CS4x4(axis1=-cup_cs.axis(1), axis2=-cup_cs.axis(0))
    cs.orthogonalize([0])
    cs.origin(cup_cs.origin() - 2.5 * cup_radius * cs.axis(0) - 2.5 * cup_radius * cs.axis(1))
    pelvis_view.setCamera_FPlane(cs, 5 * cup_radius)
    pelvis_view.updateInTime()


def update_cup_camera_RI():
    cs = vmi.CS4x4(axis1=-cup_cs.axis(0), axis2=cup_cs.axis(1))
    cs.orthogonalize([0])
    cs.origin(cup_cs.origin() - 2.5 * cup_radius * cs.axis(0) - 2.5 * cup_radius * cs.axis(1))
    pelvis_view.setCamera_FPlane(cs, 5 * cup_radius)
    pelvis_view.updateInTime()


def update_cup_camera_plane():
    cs = vmi.CS4x4(axis1=-cup_cs.axis(0), axis2=-cup_cs.axis(2))
    cs.orthogonalize([0])
    cs.origin(cup_cs.origin() - 2.5 * cup_radius * cs.axis(0) - 2.5 * cup_radius * cs.axis(1))
    pelvis_view.setCamera_FPlane(cs, 5 * cup_radius)
    pelvis_view.updateInTime()


def update_guide_path():
    global guide_path, guide_angles, hole_radius
    css = [cup_cs.rotate(-original_LR * guide_angles[i], cup_cs.axis(2)) for i in range(4)] + [cup_cs.copy()]
    for cs in css:
        cs.origin(cs.mpt([0, 0, cup_radius]))
    centers = [css[i].mpt([guide_radiuss[i], 0, 0]) for i in range(4)] + [css[4].mpt([0, 0, 0])]
    r = hole_radius + 0.2
    outer_radius = r + min_thick

    for i in [0]:
        pts = [centers[i] - 100 * cup_cs.axis(2), centers[i] + 50 * cup_cs.axis(2)]
        line = vmi.ccPd_Sh(vmi.ccEdge(vmi.ccSegment(pts[0], pts[1])))
        circle = vmi.ccPd_Sh(vmi.ccEdge(vmi.ccCircle(outer_radius, centers[i], css[i].axis(2), css[i].axis(0))))
        hole = vmi.ccPd_Sh(vmi.ccEdge(vmi.ccCircle(r, centers[i], css[i].axis(2), css[i].axis(0))))
        guide_axes_prop[i].setData(vmi.pdAppend([line, circle, hole]))

    for i in [4]:
        pts = [centers[i] - 100 * cup_cs.axis(2), centers[i] + 50 * cup_cs.axis(2)]
        line = vmi.ccPd_Sh(vmi.ccEdge(vmi.ccSegment(pts[0], pts[1])))
        hole = vmi.ccPd_Sh(vmi.ccEdge(vmi.ccCircle(outer_radius, centers[i], css[i].axis(2), css[i].axis(0))))
        guide_axes_prop[i].setData(vmi.pdAppend([line, hole]))

    guide_path = vmi.ccEdge(vmi.ccBSpline_Kochanek(centers[:4], True))
    guide_path_prop.setData(guide_path)


def update_hole_depth():
    global hole_depth
    cs = cup_cs.rotate(-original_LR * guide_angles[0], cup_cs.axis(2))
    cs.origin(cs.mpt([0, 0, cup_radius]))
    center = cs.mpt([guide_radiuss[0], 0, 0])
    pts = [center - 1000 * cup_cs.axis(2), center + 1000 * cup_cs.axis(2)]
    d = [vmi.pdRayDistance_Pt(pts[0], cup_cs.axis(2), aceta_prop.data()),
         vmi.pdRayDistance_Pt(pts[1], -cup_cs.axis(2), aceta_prop.data())]

    d = 2000 - d[0] - d[1] if d[0] and d[1] else 0
    hole_depth = max(d, 0)
    guide_hole_depth_box.draw_text('深 {:.1f} mm'.format(hole_depth))


def update_guide_plate():
    global guide_plate, guide_path, hole_radius

    # 匹配板
    n = round(vmi.ccLength(guide_path))
    pts = vmi.ccUniformPts_Edge(guide_path, n)
    guide_shape = vmi.ccMatchSolid_Thick(pts, -cup_cs.axis(2), 4 * cup_radius, aceta_prop.data(), min_thick)

    # 边缘坐标系
    css = [cup_cs.rotate(-original_LR * guide_angles[i], cup_cs.axis(2)) for i in range(4)] + [cup_cs.copy()]
    for cs in css:
        cs.origin(cs.mpt([0, 0, cup_radius]))
    centers = [css[i].mpt([guide_radiuss[i], 0, 0]) for i in range(4)] + [css[4].mpt([0, 0, 0])]
    r = hole_radius + 0.2
    outer_radius = r + min_thick

    # 外圆柱
    pts = [centers[0], (centers[0] + centers[1] + centers[4]) / 3]

    dists = [vmi.pdRayDistance_Pt(pt, -cup_cs.axis(2), aceta_prop.data()) for pt in pts]
    tops = [pts[i] + (hole_length - dists[i]) * cup_cs.axis(2) for i in range(2)]
    tops = [vmi.ptOnPlane(tops[i], tops[0], cup_cs.axis(2)) for i in range(2)]

    top_edges = [vmi.ccEdge(vmi.ccCircle(outer_radius, pt, cup_cs.axis(2), cup_cs.axis(0))) for pt in tops]
    top_ptss = [vmi.ccUniformPts_Edge(edge, round(vmi.ccLength(edge))) for edge in top_edges]

    solids = [vmi.ccMatchSolid_Face(top_ptss[i], -cup_cs.axis(2), [1.2, 5][i] * hole_length, aceta_prop.data(),
                                    [0.1, 0.5 * min_thick][i]) for i in range(2)]
    guide_shape = vmi.ccBoolean_Union([guide_shape, *solids])

    # 内通孔
    pts = [centers[0], centers[4]]

    dists = [vmi.pdRayDistance_Pt(pt, -cup_cs.axis(2), aceta_prop.data()) for pt in pts]
    tops = [pts[i] + (hole_length - dists[i]) * cup_cs.axis(2) for i in range(2)]

    top_edges = [vmi.ccEdge(vmi.ccCircle([r, outer_radius][i], tops[i], cup_cs.axis(2), cup_cs.axis(0))) for i in
                 range(2)]
    top_faces = [vmi.ccFace(vmi.ccWire(edge)) for edge in top_edges]

    solids = [vmi.ccPrism(face, -cup_cs.axis(2), vmi.ccDiagonal(guide_shape)) for face in top_faces]
    guide_shape = vmi.ccBoolean_Difference([guide_shape, *solids])

    guide_plate_prop.setData(guide_shape)


def LeftButtonPress(**kwargs):
    if kwargs['picked'] is voi_view:
        if plcut_box.text() == '请勾画切割范围':
            pt = voi_view.pickPt_FocalPlane()
            plcut_pts.clear()
            plcut_pts.append(pt)
            update_line_cut()


def LeftButtonPressMove(**kwargs):
    global spcut_center, pelvis_cs
    if kwargs['picked'] is voi_view:
        if plcut_box.text() == '请勾画切割范围':
            pt = voi_view.pickPt_Cell()

            for path_pt in plcut_pts:
                if (path_pt == pt).all():
                    return

            plcut_pts.append(pt)  # 添加拾取路径点
            update_line_cut()
        else:
            voi_view.mouseRotateFocal(**kwargs)
    elif kwargs['picked'] is pelvis_view:
        pelvis_view.mouseRotateFocal(**kwargs)
        if pelvis_MPP_box.text() == '确定':
            update_pelvis_MPP()
        elif pelvis_APP_box.text() == '确定':
            update_pelvis_APP()
        elif xray_align_box.text() == '确定':
            update_xray_pelvis()
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

        cup_cs.origin(cup_cs.origin() + over)
        update_cup()


def LeftButtonPressMoveRelease(**kwargs):
    if kwargs['picked'] is voi_view:
        if plcut_box.text() == '请勾画切割范围':
            plcut_box.draw_text('请耐心等待')
            plcut_voi_image()
            plcut_box.draw_text('线切割')

            plcut_pts.clear()
            update_line_cut()


def LeftButtonPressRelease(**kwargs):
    global original_image, spcut_radius, pelvis_cs, cup_radius, cup_cs, cup_RA, cup_RI, hole_radius
    global xray_image
    if kwargs['picked'] is dicom_box:
        patient_image = read_dicom()
        if patient_image is not None:
            original_slice.setData(patient_image)
            original_slice.setSlicePlaneOrigin_Center()
            original_slice.setSlicePlaneNormal_Coronal()
            original_view.setCamera_Coronal()
            original_view.setCamera_FitAll()
    elif kwargs['picked'] is bone_value_box:
        global bone_value
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
            back_color=QColor.fromRgbF(0.4, 0.6, 1) if spcut_prop.visible() else QColor('black'))
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
            cup_radius_box.draw_text('半径 = {:.0f} mm'.format(cup_radius))
            update_cup()
    elif kwargs['picked'] is cup_RA_box:
        r = vmi.askInt(-15, cup_RA, 45)
        if r is not None:
            cup_RA = r
            cup_RA_box.draw_text('前倾角 = {:.0f}°'.format(cup_RA))

            update_cup_orientation()
            update_cup()
    elif kwargs['picked'] is cup_RI_box:
        r = vmi.askInt(0, cup_RI, 60)
        if r is not None:
            cup_RI = r
            cup_RI_box.draw_text('外展角 = {:.0f}°'.format(cup_RI))

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
            back_color=QColor.fromRgbF(1, 1, 0.6) if pelvis_prop.visible() else QColor('black'))
    elif kwargs['picked'] is metal_visible_box:
        metal_prop.visibleToggle()
        metal_visible_box.draw_text(
            back_color=QColor.fromRgbF(1, 0.4, 0.4) if metal_prop.visible() else QColor('black'))
    elif kwargs['picked'] is cup_radius_box:
        r = vmi.askInt(5, cup_radius, 50)
        if r is not None:
            cup_radius = r
            cup_radius_box.draw_text('半径 = {:.0f} mm'.format(cup_radius))
            update_cup()
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
    elif kwargs['picked'] is xray_align_box:
        if xray_align_box.text() == '配准骨盆正位':
            xray_align_box.draw_text('确定')
            update_xray_pelvis()
        elif xray_align_box.text() == '确定':
            xray_align_box.draw_text('配准骨盆正位')
    elif kwargs['picked'] is init_ctray_box:
        init_ctray_box.draw_text('请耐心等待')
        update_ctray()
        ctray_view.setCamera_Axial()
        ctray_view.setCamera_FitAll()
        ctray_view.setEnabled(True)
        init_ctray_box.draw_text('创建投影')
    elif kwargs['picked'] is xray_open_box:
        xray_image = read_dicom()  # 读取DICOM路径
        if xray_image is not None:
            xray_slice.setData(xray_image)
            xray_view.setCamera_Axial()
            xray_view.setCamera_FitAll()
            xray_slice.setColorWindow_Auto()
    elif kwargs['picked'] is init_guide_box:
        init_guide_box.draw_text('请耐心等待')
        init_guide()
        init_guide_box.draw_text('创建导板')
    elif kwargs['picked'] is aceta_visible_box:
        aceta_prop.visibleToggle()
        aceta_visible_box.draw_text(back_color=QColor.fromRgbF(1, 1, 0.6) if aceta_prop.visible() else QColor('black'))
    elif kwargs['picked'] is guide_plate_visible_box:
        guide_plate_prop.visibleToggle()
        guide_plate_visible_box.draw_text(
            back_color=QColor.fromRgbF(0.4, 0.6, 1) if guide_plate_prop.visible() else QColor('black'))
    elif kwargs['picked'] is guide_plate_box:
        guide_plate_box.draw_text('请耐心等待')
        update_hole_depth()
        update_guide_plate()
        guide_plate_box.draw_text('更新导板')
    elif kwargs['picked'] in guide_radius_boxs:
        i = guide_radius_boxs.index(kwargs['picked'])
        r = vmi.askInt(5, guide_radiuss[i], 80)
        if r is not None:
            guide_radiuss[i] = r
            guide_radius_boxs[i].draw_text('{} mm'.format(guide_radiuss[i]))
            update_guide_path()
    elif kwargs['picked'] in guide_angle_boxs:
        i = guide_angle_boxs.index(kwargs['picked'])
        r = vmi.askInt(-179, guide_angles[i], 180)
        if r is not None:
            guide_angles[i] = r
            if guide_angles[i] + kwargs['delta'] > 180.5:
                guide_angles[i] = -179
            elif guide_angles[i] + kwargs['delta'] < -178.5:
                guide_angles[i] = 180
            guide_angle_boxs[i].draw_text('{}°'.format(guide_angles[i]))
            update_guide_path()
    elif kwargs['picked'] is guide_hole_radius_box:
        r = vmi.askFloat(0.5, hole_radius, 2.5, 1, 0.1)
        if r is not None:
            hole_radius = r
            guide_hole_radius_box.draw_text('针 {:.1f} mm'.format(2 * hole_radius))
            update_guide_path()
    elif kwargs['picked'] is guide_hole_depth_box:
        update_hole_depth()
    elif kwargs['picked'] is output_box:
        p = vmi.askDirectory('vmi')
        if p is not None:
            filename = '{} {} {}'.format(patient_name,
                                         '左' if original_LR > 0 else '右',
                                         time.strftime("%Y-%m-%d %H-%M-%S", time.localtime()))

            vmi.pdSaveFile_STL(aceta_prop.data(), str(pathlib.Path(p) / (filename + ' 髋臼.stl')))
            vmi.pdSaveFile_STL(guide_plate_prop.data(), str(pathlib.Path(p) / (filename + ' 导板.stl')))
            vmi.app.clipboard().setText(str(gdata))

            # data = pickle.dumps(gdata)
            # (pathlib.Path(p) / (filename + ' 存档.vmi')).write_bytes(data)


def MidButtonPressMove(**kwargs):
    if kwargs['picked'] in [pelvis_view, pelvis_slice]:
        pelvis_view.mousePan()
        if pelvis_MPP_box.text() == '确定':
            update_pelvis_MPP()
        elif pelvis_APP_box.text() == '确定':
            update_pelvis_APP()
        elif xray_align_box.text() == '确定':
            update_xray_pelvis()
    elif kwargs['picked'] in [xray_view, xray_slice]:
        xray_view.mousePan()
        if xray_align_box.text() == '确定':
            update_xray_pelvis()


def RightButtonPressMove(**kwargs):
    if kwargs['picked'] in [pelvis_view, pelvis_slice]:
        pelvis_view.mouseZoom()
        if pelvis_MPP_box.text() == '确定':
            update_pelvis_MPP()
        elif pelvis_APP_box.text() == '确定':
            update_pelvis_APP()
        elif xray_align_box.text() == '确定':
            update_xray_pelvis()
    elif kwargs['picked'] in [xray_view, xray_slice]:
        xray_view.mouseZoom()
        if xray_align_box.text() == '确定':
            update_xray_pelvis()


def NoButtonWheel(**kwargs):
    global bone_value, spcut_radius, cup_radius, cup_RA, cup_RI, hole_radius
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
        elif xray_align_box.text() == '确定':
            update_xray_pelvis()
    elif kwargs['picked'] is cup_radius_box:
        cup_radius = min(max(cup_radius + kwargs['delta'], 5), 50)
        cup_radius_box.draw_text('半径：{:.0f} mm'.format(cup_radius))
        update_cup()
    elif kwargs['picked'] is cup_RA_box:
        cup_RA = min(max(cup_RA + kwargs['delta'], -15), 45)
        cup_RA_box.draw_text('前倾角：{:.0f}°'.format(cup_RA))

        update_cup_orientation()
        update_cup()
    elif kwargs['picked'] is cup_RI_box:
        cup_RI = min(max(cup_RI + kwargs['delta'], 0), 60)
        cup_RI_box.draw_text('外展角：{:.0f}°'.format(cup_RI))

        update_cup_orientation()
        update_cup()
    elif kwargs['picked'] is pelvis_slice:
        pelvis_slice.slice(**kwargs)
        update_cup()
    elif kwargs['picked'] in guide_radius_boxs:
        i = guide_radius_boxs.index(kwargs['picked'])
        guide_radiuss[i] = min(max(guide_radiuss[i] + kwargs['delta'], 5), 80)
        guide_radius_boxs[i].draw_text('{} mm'.format(guide_radiuss[i]))
        update_guide_path()
    elif kwargs['picked'] in guide_angle_boxs:
        i = guide_angle_boxs.index(kwargs['picked'])
        guide_angles[i] = guide_angles[i] + kwargs['delta']
        if guide_angles[i] + kwargs['delta'] > 180.5:
            guide_angles[i] = -179
        elif guide_angles[i] + kwargs['delta'] < -178.5:
            guide_angles[i] = 180
        guide_angle_boxs[i].draw_text('{}°'.format(guide_angles[i]))
        update_guide_path()
    elif kwargs['picked'] is guide_hole_radius_box:
        hole_radius = min(max(hole_radius + 0.1 * kwargs['delta'], 0.5), 2.5)
        guide_hole_radius_box.draw_text('针 {:.1f} mm'.format(2 * hole_radius))
        update_guide_path()


class Main(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        brush = QBrush(QColor(255, 255, 255, 255))
        palette = QPalette()
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.setPalette(palette)

        self._AppTitle = '髋关节置换导板设计'
        self._Version = vmi.vers

        self._ScrollArea = QScrollArea()
        self._ScrollArea.setWidgetResizable(True)
        self.setCentralWidget(self._ScrollArea)

        menubar = QMenuBar(self)
        self.setMenuBar(menubar)

        menuFile = QMenu('文件', menubar)
        menubar.addAction(menuFile.menuAction())

        actionSave = QAction('保存', self)
        actionSave.setShortcut(QKeySequence('Ctrl+S'))
        actionSave.triggered.connect(self.save)
        menuFile.addAction(actionSave)

        statusbar = QStatusBar(self)
        self.setStatusBar(statusbar)

    def area(self):
        return self._ScrollArea

    def closeEvent(self, ev: QCloseEvent):
        ev.accept() if vmi.askYesNo('退出？') else ev.ignore()

    def save(self):
        print(len(pickle.dumps(gdata)))


if __name__ == '__main__':
    gdata_start = list(globals().keys())

    patient_name = str()
    original_image = vtk.vtkImageData()

    # 0 原始图像
    original_target, original_LR = np.zeros(3), 1
    original_view = vmi.View()

    original_slice = vmi.ImageSlice(original_view)  # 断层显示
    original_slice.setColorWindow_Bone()

    original_slice_menu = vmi.Menu()
    original_slice_menu.menu.addAction('定位髋关节中心').triggered.connect(on_init_voi)
    original_slice_menu.menu.addSeparator()
    original_slice_menu.menu.addMenu(original_slice.menu)
    original_slice.mouse['RightButton']['PressRelease'] = [original_slice_menu.menuexec]

    dicom_box = vmi.TextBox(original_view, text='DICOM', pickable=True,
                            size=[0.24, 0.04], pos=[0, 0.04], anchor=[0, 0])
    dicom_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]

    patient_name_box = vmi.TextBox(original_view, text='姓名', visible=False,
                                   size=[0.24, 0.04], pos=[0, 0.1], anchor=[0, 0])
    patient_LR_box = vmi.TextBox(original_view, text='患侧', visible=False,
                                 size=[0.24, 0.04], pos=[0, 0.14], anchor=[0, 0])

    # 1 目标区域
    voi_view = vmi.View()
    voi_view.mouse['LeftButton']['Press'] = [LeftButtonPress]
    voi_view.mouse['LeftButton']['PressMove'] = [LeftButtonPressMove]
    voi_view.mouse['LeftButton']['PressMoveRelease'] = [LeftButtonPressMoveRelease]

    bone_value, target_value = 200, -1100

    bone_value_box = vmi.TextBox(voi_view, text='骨阈值：{:.0f} HU'.format(bone_value),
                                 size=[0.24, 0.04], pos=[0, 0.04], anchor=[0, 0], pickable=True)
    bone_value_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]
    bone_value_box.mouse['NoButton']['Wheel'] = [NoButtonWheel]

    voi_size, voi_center, voi_origin, voi_cs = np.zeros(3), np.zeros(3), np.zeros(3), vmi.CS4x4()

    voi_image = vtk.vtkImageData()
    voi_volume = vmi.ImageVolume(voi_view)
    voi_volume.setOpacityScalar({bone_value - 1: 0, bone_value: 1})
    voi_volume.setColor({bone_value: [1, 1, 0.6]})

    # 线切割
    plcut_pts = []
    plcut_prop = vmi.PolyActor(voi_view, color=[1, 0.6, 0.6], line_width=3, always_on_top=True)

    # 球切割
    spcut_center, spcut_radius, spcut_length = np.zeros(3), 22, 200
    spcut_prop = vmi.PolyActor(voi_view, color=[0.4, 0.6, 1], pickable=True)
    spcut_prop.mouse['LeftButton']['PressMove'] = [LeftButtonPressMove]

    plcut_box = vmi.TextBox(voi_view, text='线切割', size=[0.24, 0.04], pos=[0, 0.1], anchor=[0, 0], pickable=True)
    plcut_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]

    spcut_box = vmi.TextBox(voi_view, text='球切割', size=[0.24, 0.04], pos=[0, 0.16], anchor=[0, 0], pickable=True)
    spcut_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]

    spcut_visible_box = vmi.TextBox(voi_view, size=[0.01, 0.04], pos=[0.24, 0.16], anchor=[1, 0],
                                    back_color=QColor.fromRgbF(0.4, 0.6, 1), pickable=True)
    spcut_visible_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]

    spcut_radius_box = vmi.TextBox(voi_view, text='球半径：{:.0f} mm'.format(spcut_radius),
                                   size=[0.24, 0.04], pos=[0, 0.20], anchor=[0, 0], pickable=True)
    spcut_radius_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]
    spcut_radius_box.mouse['NoButton']['Wheel'] = NoButtonWheel

    # 234 球切割局部
    spcut_y_views = [vmi.View(), vmi.View(), vmi.View()]
    spcut_z_views = [vmi.View(), vmi.View(), vmi.View()]

    spcut_y_boxs = [vmi.TextBox(spcut_y_views[i], text=['斜冠状位', '正冠状位', '斜冠状位'][i],
                                size=[0.2, 0.1], pos=[1, 1], anchor=[1, 1]) for i in range(3)]
    spcut_z_boxs = [vmi.TextBox(spcut_z_views[i], text=['斜横断位', '正横断位', '斜横断位'][i],
                                size=[0.2, 0.1], pos=[1, 1], anchor=[1, 1]) for i in range(3)]

    spcut_y_slices = [vmi.ImageSlice(v) for v in spcut_y_views]
    spcut_z_slices = [vmi.ImageSlice(v) for v in spcut_z_views]

    for i in spcut_y_slices + spcut_z_slices:
        i.bindData(voi_volume)
        i.bindLookupTable(original_slice)
        i.mouse['NoButton']['Wheel'] = [i.mouseBlock]

    spcut_y_props = [vmi.PolyActor(v, color=[0.4, 0.6, 1], opacity=0.5, pickable=True) for v in spcut_y_views]
    spcut_z_props = [vmi.PolyActor(v, color=[0.4, 0.6, 1], opacity=0.5, pickable=True) for v in spcut_z_views]

    for i in spcut_y_props + spcut_z_props:
        i.mouse['LeftButton']['PressMove'] = [LeftButtonPressMove]

    init_pelvis_box = vmi.TextBox(voi_view, text='创建骨盆', fore_color=QColor('white'), back_color=QColor('crimson'),
                                  bold=True, size=[0.24, 0.04], pos=[1, 0.04], anchor=[1, 0], pickable=True)
    init_pelvis_box.mouse['LeftButton']['PressRelease'] = LeftButtonPressRelease

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

    cup_radius_box = vmi.TextBox(pelvis_view, text='半径: {:.0f} mm'.format(cup_radius), pickable=True,
                                 size=[0.24, 0.04], pos=[0, 0.04], anchor=[0, 0])
    cup_radius_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]
    cup_radius_box.mouse['NoButton']['Wheel'] = [NoButtonWheel]

    cup_RA_box = vmi.TextBox(pelvis_view, text='前倾角: {:.0f}°'.format(cup_RA), pickable=True,
                             size=[0.24, 0.04], pos=[0, 0.1], anchor=[0, 0])
    cup_RA_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]
    cup_RA_box.mouse['NoButton']['Wheel'] = [NoButtonWheel]

    cup_RI_box = vmi.TextBox(pelvis_view, text='外展角: {:.0f}°'.format(cup_RI), pickable=True,
                             size=[0.24, 0.04], pos=[0, 0.14], anchor=[0, 0])
    cup_RI_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]
    cup_RI_box.mouse['NoButton']['Wheel'] = [NoButtonWheel]

    pelvis_slice = vmi.ImageSlice(pelvis_view, visible=False)
    pelvis_slice.bindData(voi_volume)
    pelvis_slice.bindLookupTable(original_slice)
    pelvis_slice.mouse['MidButton']['PressMove'] = [MidButtonPressMove]
    pelvis_slice.mouse['RightButton']['PressMove'] = [RightButtonPressMove]
    pelvis_slice.mouse['NoButton']['Wheel'] = [NoButtonWheel]

    cup_section_prop = vmi.PolyActor(pelvis_view, color=[0.4, 0.6, 1], line_width=3, visible=False, pickable=True)
    cup_section_prop.mouse['LeftButton']['PressMove'] = [LeftButtonPressMove]

    pelvis_slice_box = vmi.TextBox(pelvis_view, text='三维', pickable=True,
                                   size=[0.24, 0.04], pos=[0, 0.2], anchor=[0, 0])
    pelvis_slice_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]

    pelvis_MPP_box = vmi.TextBox(pelvis_view, text='配准对称面', pickable=True,
                                 size=[0.24, 0.04], pos=[0, 0.26], anchor=[0, 0])
    pelvis_MPP_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]

    pelvis_APP_box = vmi.TextBox(pelvis_view, text='配准前平面', pickable=True,
                                 size=[0.24, 0.04], pos=[0, 0.3], anchor=[0, 0])
    pelvis_APP_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]

    cup_camera_sagittal_box = vmi.TextBox(pelvis_view, text='矢状', pickable=True,
                                          size=[0.07, 0.04], pos=[0, 0.36], anchor=[0, 0])
    cup_camera_sagittal_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]

    cup_camera_coronal_box = vmi.TextBox(pelvis_view, text='冠状', pickable=True,
                                         size=[0.07, 0.04], pos=[0.07, 0.36], anchor=[0, 0])
    cup_camera_coronal_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]

    cup_camera_axial_box = vmi.TextBox(pelvis_view, text='横断', pickable=True,
                                       size=[0.07, 0.04], pos=[0.14, 0.36], anchor=[0, 0])
    cup_camera_axial_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]

    cup_camera_RA_box = vmi.TextBox(pelvis_view, text='前倾', pickable=True,
                                    size=[0.07, 0.04], pos=[0, 0.4], anchor=[0, 0])
    cup_camera_RA_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]

    cup_camera_RI_box = vmi.TextBox(pelvis_view, text='外展', pickable=True,
                                    size=[0.07, 0.04], pos=[0.07, 0.4], anchor=[0, 0])
    cup_camera_RI_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]

    cup_camera_plane_box = vmi.TextBox(pelvis_view, text='正视', pickable=True,
                                       size=[0.07, 0.04], pos=[0.14, 0.4], anchor=[0, 0])
    cup_camera_plane_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]

    pelvis_visible_box = vmi.TextBox(pelvis_view, size=[0.03, 0.04], pos=[0.21, 0.36], anchor=[0, 0],
                                     back_color=QColor.fromRgbF(1, 1, 0.6), pickable=True)
    pelvis_visible_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]

    metal_visible_box = vmi.TextBox(pelvis_view, size=[0.03, 0.04], pos=[0.21, 0.4], anchor=[0, 0],
                                    back_color=QColor.fromRgbF(1, 0.4, 0.4), pickable=True)
    metal_visible_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]

    pelvis_MPP_prop = vmi.PolyActor(pelvis_view, visible=False, color=[1, 0.4, 0.4], repres='points')
    pelvis_APP_prop = vmi.PolyActor(pelvis_view, visible=False, color=[1, 0.4, 0.4], line_width=3, always_on_top=True)

    init_guide_box = vmi.TextBox(pelvis_view, text='创建导板', fore_color=QColor('white'), back_color=QColor('crimson'),
                                 bold=True, size=[0.24, 0.04], pos=[1, 0.04], anchor=[1, 0], pickable=True)
    init_guide_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]

    # 6 投影对照
    xray_cs = vmi.CS4x4()
    xray_view = vmi.View()
    xray_view.mouse['LeftButton']['PressMove'] = [xray_view.mousePass]
    xray_view.mouse['MidButton']['PressMove'] = [MidButtonPressMove]
    xray_view.mouse['RightButton']['PressMove'] = [RightButtonPressMove]
    xray_view.mouse['NoButton']['Wheel'] = [xray_view.mousePass]

    xray_slice = vmi.ImageSlice(xray_view)
    xray_slice.mouse['MidButton']['PressMove'] = [MidButtonPressMove]
    xray_slice.mouse['RightButton']['PressMove'] = [RightButtonPressMove]

    xray_pelvis_prop = vmi.PolyActor(xray_view, color=[1, 1, 0.6], opacity=0.1, repres='points', shade=False)

    xray_open_box = vmi.TextBox(xray_view, text='打开X-ray图像', pickable=True,
                                size=[0.24, 0.04], pos=[0, 0.04], anchor=[0, 0])
    xray_open_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]

    xray_align_box = vmi.TextBox(xray_view, text='配准骨盆正位', pickable=True,
                                 size=[0.24, 0.04], pos=[0, 0.1], anchor=[0, 0])
    xray_align_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]

    init_ctray_box = vmi.TextBox(xray_view, text='创建投影', pickable=True,
                                 fore_color=QColor('white'), back_color=QColor('crimson'), bold=True,
                                 size=[0.24, 0.04], pos=[1, 0.04], anchor=[1, 0])
    init_ctray_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]

    # 7 站立位投影
    ctray_cs = vmi.CS4x4()
    ctray_size = np.zeros(3)
    ctray_view = vmi.View()
    ctray_slice = vmi.ImageSlice(ctray_view)

    # 8 导板
    guide_view = vmi.View()
    guide_view.renderer().SetActiveCamera(pelvis_view.camera())

    aceta_prop = vmi.PolyActor(guide_view, color=[1, 1, 0.6])

    min_thick = 4
    guide_radiuss, guide_angles, hole_radius, hole_length = [22, 22, 10, 10], [-45, 15, 100, -100], 1, 20
    hole_depth = 0

    guide_prefix_boxs = [vmi.TextBox(guide_view, text=['前上', '后上', '后下', '前下'][i],
                                     size=[0.06, 0.04], pos=[0, 0.12 + i * 0.04], anchor=[0, 0]) for i in range(4)]
    guide_radius_boxs = [vmi.TextBox(guide_view, text='{} mm'.format(guide_radiuss[i]), pickable=True,
                                     size=[0.06, 0.04], pos=[0.06, 0.12 + i * 0.04], anchor=[0, 0]) for i in range(4)]
    guide_angle_boxs = [vmi.TextBox(guide_view, text='{}°'.format(guide_angles[i]), pickable=True,
                                    size=[0.06, 0.04], pos=[0.12, 0.12 + i * 0.04], anchor=[0, 0]) for i in range(4)]

    guide_hole_radius_box = vmi.TextBox(guide_view, text='针 {:.1f} mm'.format(2 * hole_radius), pickable=True,
                                        size=[0.09, 0.04], pos=[0, 0.08], anchor=[0, 0])

    for box in guide_radius_boxs + guide_angle_boxs + [guide_hole_radius_box]:
        box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]
        box.mouse['NoButton']['Wheel'] = [NoButtonWheel]

    guide_hole_depth_box = vmi.TextBox(guide_view, text='深 {:.1f} mm'.format(hole_depth), pickable=True,
                                       size=[0.09, 0.04], pos=[0.09, 0.08], anchor=[0, 0])
    guide_hole_depth_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]

    guide_path = vmi.TopoDS_Shape()
    guide_path_prop = vmi.PolyActor(guide_view, color=[0.4, 1, 0.4], line_width=3)
    guide_axes_prop = [vmi.PolyActor(guide_view, color=[0.4, 1, 0.4], line_width=3) for i in range(5)]
    for prop in guide_axes_prop:
        prop.mouse['LeftButton']['PressMove'] = [LeftButtonPressMove]

    guide_plate = vmi.TopoDS_Shape()
    guide_plate_prop = vmi.PolyActor(guide_view, color=[0.4, 0.6, 1])
    guide_plate_prop.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]

    guide_plate_box = vmi.TextBox(guide_view, text='更新导板', pickable=True,
                                  size=[0.14, 0.04], pos=[0, 0.04], anchor=[0, 0])
    guide_plate_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]

    aceta_visible_box = vmi.TextBox(guide_view, size=[0.02, 0.04], pos=[0.14, 0.04], anchor=[0, 0],
                                    back_color=QColor.fromRgbF(1, 1, 0.6), pickable=True)
    aceta_visible_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]

    guide_plate_visible_box = vmi.TextBox(guide_view, size=[0.02, 0.04], pos=[0.16, 0.04], anchor=[0, 0],
                                          back_color=QColor.fromRgbF(0.4, 0.6, 1), pickable=True)
    guide_plate_visible_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]

    output_box = vmi.TextBox(guide_view, text='导出', pickable=True,
                             size=[0.09, 0.04], pos=[0.09, 0.28], anchor=[0, 0])
    output_box.mouse['LeftButton']['PressRelease'] = [LeftButtonPressRelease]

    gdata = {kw: globals()[kw] for kw in globals() if kw not in gdata_start}
    for kw in ['gdata_start', 'i', 'box', 'prop', 'original_slice_menu']:
        if kw in gdata:
            del gdata[kw]

    screen_width = QGuiApplication.screens()[0].geometry().width()
    views = [original_view, voi_view, *spcut_y_views, *spcut_z_views, pelvis_view, xray_view, ctray_view, guide_view]

    for v in views:
        v.setMinimumWidth(0.5 * screen_width)
    for v in spcut_y_views + spcut_z_views:
        v.setMinimumWidth(0.25 * screen_width)

    for v in views[1:]:
        v.setEnabled(False)

    # 视图布局
    widget = QWidget()
    layout = QGridLayout(widget)
    layout.addWidget(original_view, 0, 0, 3, 1)
    layout.addWidget(voi_view, 0, 1, 3, 1)
    layout.addWidget(spcut_y_views[0], 0, 2, 1, 1)
    layout.addWidget(spcut_y_views[1], 1, 2, 1, 1)
    layout.addWidget(spcut_y_views[2], 2, 2, 1, 1)
    layout.addWidget(spcut_z_views[0], 0, 3, 1, 1)
    layout.addWidget(spcut_z_views[1], 1, 3, 1, 1)
    layout.addWidget(spcut_z_views[2], 2, 3, 1, 1)
    layout.addWidget(pelvis_view, 0, 4, 3, 1)
    layout.addWidget(guide_view, 0, 5, 3, 1)
    # layout.addWidget(xray_view, 0, 5, 3, 1)
    # layout.addWidget(ctray_view, 0, 6, 3, 1)

    main = Main()
    main.area().setWidget(widget)

    # pickle.dumps(gdata)
    vmi.appexec(main)  # 执行主窗口程序
    vmi.appexit()  # 清理并退出程序
