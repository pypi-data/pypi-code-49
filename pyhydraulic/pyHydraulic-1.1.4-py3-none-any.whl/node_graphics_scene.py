import math,os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class QDMGraphicsScene(QGraphicsScene):
    def __init__(self, scene, parent=None):
        super().__init__(parent)

        self.scene = scene

        # settings
        self.gridSize = 50 # 每個格子像素
        self.gridSquares = 5  # 每个大格子里面有几个小格子
        # 颜色选择：https://doc.qt.io/qtforpython/PySide2/QtGui/QColor.html
        self._color_background = QColor("##000000")  # QColor("#393939")
        self._color_light =  QColor("#888888")  # QColor("#2f2f2f")
        self._color_dark = QColor("#888888")  # QColor("#292929")
        # 小格子的笔
        self._pen_light = QPen(self._color_light)
        self._pen_light.setWidth(1)
        self._grid_enble = True

        # 大格子的笔
        self._pen_dark = QPen(self._color_dark)
        self._pen_dark.setWidth(2)
        # 用来画原点出的十字线的笔
        self._pen_origin = QPen(Qt.darkRed)
        self._pen_origin.setStyle(Qt.DashLine)
        self._pen_origin.setWidth(5)
        # 刷背景
        self.setBackgroundBrush(self._color_background)

        # 图片信息
        self.waterMarkEnable = True
        currentDir = os.path.dirname(__file__)
        self._picturePath = os.path.join(currentDir,"icons\\南工校徽红底.png")
        self._pixmap = QPixmap(self._picturePath)

        self.updateTime =0

    def setGrScene(self, width, height):
        self.setSceneRect(-width // 2, -height // 2, width, height)

    def drawBackground(self, painter, exposedRectF):
        # exposedRectF 為view在scene中的矩形輪廓
        super().drawBackground(painter, exposedRectF)
        if self._grid_enble:
            # here we create our grid
            left = int(math.floor(exposedRectF.left()))
            right = int(math.ceil(exposedRectF.right()))
            top = int(math.floor(exposedRectF.top()))
            bottom = int(math.ceil(exposedRectF.bottom()))





            first_left = left - (left % self.gridSize)
            first_top = top - (top % self.gridSize)

            # compute all lines to be drawn
            lines_light, lines_dark = [], []
            for x in range(first_left, right, self.gridSize):
                if (x % (self.gridSize*self.gridSquares) != 0): lines_light.append(QLine(x, top, x, bottom))
                else: lines_dark.append(QLine(x, top, x, bottom))

            for y in range(first_top, bottom, self.gridSize):
                if (y % (self.gridSize*self.gridSquares) != 0): lines_light.append(QLine(left, y, right, y))
                else: lines_dark.append(QLine(left, y, right, y))


            # draw the lines
            painter.setPen(self._pen_light)
            painter.drawLines(*lines_light)

            painter.setPen(self._pen_dark)
            painter.drawLines(*lines_dark)

        # 5.draw the orgins
        # zoom =self.views()[0].zoom # 獲取view的當前放大因子
        # zoomRangeList = self.views()[0].zoomRange
        # length = (zoomRangeList[1] -(zoom)) * self.gridSize *1.25 +1 * self.gridSize   #* self.gridSquares

        # exposedRectF = self.views()[0].geometry() # view整個輪廓
        # rectView = self.views()[0].mapToScene(exposedRectF).boundingRect() # view在scene中的輪廓
        radius = exposedRectF.width() / 10 # 原點十字長度
        pictureWidth = exposedRectF.height() /2

        self._pen_origin.setWidth(radius/50) # 十字線的長度也是變化的
        painter.setPen(self._pen_origin)
        painter.setOpacity(0.5)

        painter.drawLine(- radius, 0, radius, 0)
        painter.drawLine(0, - radius, 0, radius)
        painter.setOpacity(1)
        painter.drawEllipse(QPoint(0,0), radius/10, radius/10)

        # self.updateTime = self.updateTime +1
        # print("update screen %d " % self.updateTime)

        if self.waterMarkEnable == True:

            painter.setOpacity(0.12)
            painter.drawPixmap(QRect(- pictureWidth,-pictureWidth,2*pictureWidth, 2*pictureWidth), self._pixmap)


