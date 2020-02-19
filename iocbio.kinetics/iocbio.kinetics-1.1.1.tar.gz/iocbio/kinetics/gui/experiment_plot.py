# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#  Copyright (C) 2019-2020
#   Laboratory of Systems Biology, Department of Cybernetics,
#   School of Science, Tallinn University of Technology
#  This file is part of project: IOCBIO Kinetics
#
from PyQt5.QtCore import Qt, pyqtSignal, QPointF
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTabBar
from PyQt5.QtGui import QColor, QMenu, QAction, QGraphicsPathItem#, QWidgetAction
from collections import namedtuple
import pyqtgraph as pg
import numpy as np
import copy


class LinearRegion(pg.LinearRegionItem):
    sigHover = pyqtSignal(str)

    def __init__(self, roi_id, values, **kwargs):
        pg.LinearRegionItem.__init__(self, values, **kwargs)
        self.roi_id = roi_id

    def hoverEvent(self, ev):
        if self.movable and (not ev.isExit()) and ev.acceptDrags(Qt.LeftButton):
            self.setMouseHover(True)
        else:
            self.setMouseHover(False)
        self.sigHover.emit(self.roi_id)


class ExperimentViewPlot(QWidget):

    sigRoiRangeChanged = pyqtSignal(str, list)
    sigAdd = pyqtSignal(str, list)
    sigRemove = pyqtSignal(str)
    sigActive = pyqtSignal(str)

    pens = {'left axis': {'color': '#2171b5', 'width': 2},
            'right axis': {'color': '#d7301f', 'width': 2},
            'events line': {'color': '#737373', 'width': 1.5}
            }

    Tab = namedtuple('Tab', ['left', 'right'])

    def __init__(self, data, roi_types):
        QWidget.__init__(self)

        self.data = data

        self.rois_list = set()

        # fill the tabs
        l = list(self.data.keys())
        self.tab_list = []
        for k in range(0,len(l),2):
            if k+1 < len(l):
                t = ExperimentViewPlot.Tab(left=l[k], right=l[k+1])
            else:
                if k > 0: t = ExperimentViewPlot.Tab(left=l[k], right=l[0])
                else: t = ExperimentViewPlot.Tab(left=l[k], right=None)
            self.tab_list.append(t)

        # prepare empty plots

        pw = pg.PlotWidget()
        pw.setTitle(' ')
        self.plot = pw.plotItem
        self.plot.setDownsampling(ds=25, mode='subsample')
        self.plot.setClipToView(True)
        self.plot.showAxis('right')

        self.plot_right = pg.PlotCurveItem([0, 1], [0, 1], pen=self.pens['right axis'],
                                           downsampleMethod='subsample',
                                           downsample=25,
                                           #autoDownsample=True,
                                           clipToView=True)

        self.plot_left = self.plot.plot([0, 1], [0, 1], pen=self.pens['left axis'])

        self.plot.addItem(self.plot_left)

        self.pw2 = pg.ViewBox()
        self.plot.scene().addItem(self.pw2)
        self.pw2.addItem(self.plot_right)

        self.plot.getAxis('right').linkToView(self.pw2)
        self.pw2.setXLink(self.plot)

        self.update_views()

        # { Event bindings
        self.plot.vb.sigResized.connect(self.update_views)
        #self.plot.vb.sigYRangeChanged.connect(self.update_text_positions)
        self.plot.scene().sigMouseMoved.connect(self.get_mouse_postition)
        #self.plot.scene().sigMouseClicked.connect(self.get_mouse_postition_clicked)#print)
        # }

        self.mouse_current_pos = QPointF(-1,-1)
        self.last_hovered_region = None

        # tab switch
        if len(self.tab_list) > 1:
            tabs = QTabBar()
            tabs.setUsesScrollButtons(True)
            for t in self.tab_list:
                tabs.addTab("%s / %s" % (t.left,t.right))
            tabs.currentChanged.connect(self.tab_changed)
        else:
            tabs = None

        # { Creating layout
        layout = QVBoxLayout()
        if tabs is not None: layout.addWidget(tabs)
        layout.addWidget(pw)
        self.setLayout(layout)
        # }

        new_menu = QMenu()
        roi_types.sort()

        for t in roi_types:
            add_action = QAction('Add ROI: %s' % t, new_menu)
            add_action.triggered.connect(lambda toggle, value=t: self.on_add_roi(value))
            new_menu.addAction(add_action)

        self.remove_action = QAction('Remove ROI', new_menu)
        self.remove_action.triggered.connect(self.on_remove_roi)
        view_all = QAction('View All', self)
        view_all.triggered.connect(self.plot.vb.autoRange)

        new_menu.addAction(self.remove_action)
        new_menu.addAction(view_all)
        new_menu.addSeparator()
        new_menu.addMenu(self.plot.vb.menu)
        self.plot.vb.menu = new_menu
        self.plot.vb.menu.aboutToShow.connect(self.validate_add_remove_actions)

        self.tab_changed(0)
        self.show_events()
        self.update_xrange()

    def tab_changed(self, index):
        lkey, rkey = self.tab_list[index]

        x = self.data.x(lkey)
        self.view_x0 = x[0]
        self.view_x1 = x[-1]

        self.plot.setLabel('bottom', self.data.xname, units=self.data.xunit)
        self.plot.setLabel('left', self.data.y(lkey).name, units=self.data.y(lkey).unit,
                           color=self.pens['left axis']['color'])

        self.plot_left.setData(self.data.x(lkey), self.data.y(lkey).data)

        if rkey is not None:
            self.plot.getAxis('right').setLabel(self.data.y(rkey).name, units=self.data.y(rkey).unit,
                                                color=self.pens['right axis']['color'])
            self.plot_right.setData(self.data.x(rkey), self.data.y(rkey).data)
        else:
            self.plot_right.setData(None, None)

        self.update_xrange()

    def validate_add_remove_actions(self):
        # self.plot.vb.grabMouse()
        if self.last_hovered_region is None:
            self.remove_action.setDisabled(True)
        else:
            xm = self.mouse_current_pos.x()
            for item in self.plot.items:
                if hasattr(item, 'roi_id'):
                    if item.roi_id == self.last_hovered_region:
                        x0, x1 = item.getRegion()
                        break

            if x0 < xm < x1:
                self.remove_action.setEnabled(True)
            else:
                self.remove_action.setDisabled(True)
        # self.plot.vb.ungrabMouse()

    def get_mouse_postition_clicked(self, ev):
        self.mouse_current_pos = self.plot.vb.mapSceneToView(ev.pos())

    def get_mouse_postition(self, pos):
        if self.plot.sceneBoundingRect().contains(pos):
            self.mouse_current_pos = self.plot.vb.mapSceneToView(pos)

    def on_add_roi(self, roi_type):
        if self.mouse_current_pos.x() < 0: return
        self.sigAdd.emit(roi_type, self.data.new_range(self.mouse_current_pos.x()))

    def on_remove_roi(self):
        self.remove_roi(self.last_hovered_region)
        self.last_hovered_region = None

    def set_hovered_region(self, roi_id):
        self.last_hovered_region = roi_id
        self.sigActive.emit(self.last_hovered_region)

    def xview_change_request(self, r):
        x0, x1 = r.xlim()
        [vx0, vx1], _ = self.plot.vb.viewRange()

        if not vx0 < x0 < vx1 or not vx0 < x1 < vx1:
            vw = vx1 - vx0 # view width
            rw = x1 - x0 # roi width
            if vw < rw: vw = 1.1 * rw
            half_vw = 0.5 * vw
            ct = 0.5 * (x0 + x1) # center of the roi
            self.plot.setRange(xRange=[ct-half_vw, ct+half_vw], padding=0)

    def update_xrange(self):
        # print('update_xrange', self.view_x0, self.view_x1)
        # TODO remove this method, put it in __init__
        self.plot.vb.setRange(xRange=[self.view_x0, self.view_x1], padding=0)
        self.plot.setRange(xRange=[self.view_x0, self.view_x1], padding=0)

    def update_views(self):
        # Handle view resizing
        self.pw2.setGeometry(self.plot.vb.sceneBoundingRect())
        self.pw2.linkedViewChanged(self.plot.vb, self.pw2.XAxis)

    def show_events(self):
        events = self.data.config['events']
        [_, _], [_, ymax] = self.plot.vb.viewRange()

        for t, label in events.items():
            v_line = pg.InfiniteLine(t, angle=90, pen=self.pens['events line'], movable=False)
            text = pg.TextItem(anchor=(-0.2,-1), color='#000000', fill=None)
            text.setHtml('<h4>'+str(label)+'</h4>')
            text.setPos(t, ymax)

            self.plot.addItem(v_line)
            self.plot.addItem(text)

    def update_text_positions(self, vb, yrange):
        ymin, ymax = yrange
        for item in self.plot.items:
            if isinstance(item, pg.graphicsItems.TextItem.TextItem):
                t = item.pos().x()
                item.setPos(t, ymax)

    def update_rois(self, rois, rois_list):
        for key in rois_list:
            if key not in rois:
                print(key, 'not found among current ROIs')
                continue
            rdata = rois[key]['data']
            roi_type = rois[key]['type']
            if key not in self.rois_list:
                # if rois[key]['analyzer']:
                #     continue # the analysis range is handled separately

                t0, t1 = rdata.xlim()
                color = QColor('#%s' % key[:6])
                color.setAlpha(60)
                region = LinearRegion(key, (t0, t1), brush=color)
                #region = LinearRegion(key, (t0, t1))
                region.setBounds(self.data.xlim())
                region.sigRegionChangeFinished.connect(self.update_region)
                region.sigHover.connect(self.set_hovered_region)
                self.plot.addItem(region)
                self.rois_list.add(key)

            t0, t1 = rdata.xlim()
            self.update_region_if_changed(key, t0, t1)

        keys = list(self.rois_list)
        for key in keys:
            if key not in rois_list:
                self.remove_roi(key)

    def update_region_if_changed(self, roi_id, start, end):
        tol = 1e-6
        for item in self.plot.items:
            if hasattr(item, 'roi_id') and item.roi_id == roi_id:
                t0, t1 = item.getRegion()
                if abs(t0-start) > tol or abs(t1-end)>tol:
                    item.setRegion([start,end])
                return

    def update_region(self, region):
        t0, t1 = region.getRegion()
        self.sigRoiRangeChanged.emit(region.roi_id, [t0, t1])

    def remove_roi(self, roi_id):
        for item in self.plot.items:
            if hasattr(item, 'roi_id'):
                if item.roi_id == roi_id:
                    self.plot.removeItem(item)
                    break
        self.rois_list.remove(roi_id)
        self.sigRemove.emit(roi_id)
