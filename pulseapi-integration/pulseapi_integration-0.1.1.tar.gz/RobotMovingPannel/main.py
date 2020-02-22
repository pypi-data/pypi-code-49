import sys
import time

from pulseapi import *
from math import radians
from .interface import Ui_Dialog
from PyQt5 import QtWidgets, QtCore
from pulseapi_integration import NewRobotPulse
from PyQt5.QtWidgets import QApplication, QDialog

class PositionChenger(QtCore.QThread):
    def __init__(self, mainwindow, parent=None):
        super().__init__()
        self.mainwindow = mainwindow

    def run(self):
        while True:
            XYZ = self.mainwindow.robot.get_position()['point'].values()
            RPW = self.mainwindow.robot.get_position()['rotation'].values()

            for lineEdit, value in zip(self.mainwindow.lineEdit_mapping, [*XYZ, *RPW]):
                lineEdit.setText(str(round(value, 4)))
            time.sleep(0.2)

class MovingPannel(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self, host):
        super().__init__()

        self.setupUi(self)
        self.robot = NewRobotPulse(host)

        self.buttons_maping = [
            (self.button_xUp,       self.xUp),
            (self.button_xDown,     self.xDown),
            (self.button_yUp,       self.yUp),
            (self.button_yDown,     self.yDown),
            (self.button_zDown,     self.zUp),
            (self.button_zUp,       self.zDown),
            (self.button_rollUp,    self.rxUp),
            (self.button_rollDown,  self.rxDown),
            (self.button_pitchUp,   self.ryUp),
            (self.button_pitchDown, self.ryDown),
            (self.button_yawUp,     self.rzUp),
            (self.button_yawDown,   self.rzDown)
        ]

        self.lineEdit_mapping = [
            self.lineEdit_x,
            self.lineEdit_y,
            self.lineEdit_z,
            self.lineEdit_roll,
            self.lineEdit_pitch,
            self.lineEdit_yaw
        ]

        self.checkBox_moving.toggled.connect(self.spinBox_move_step.setEnabled)
        self.checkBox_moving.toggled.connect(self.spinBox_rotation_step.setEnabled)

        # Disable some functions
        self.label_move_step.setVisible(True)
        self.checkBox_moving.setVisible(True)
        self.spinBox_move_step.setVisible(True)
        self.label_rotation_step.setVisible(True)
        self.spinBox_rotation_step.setVisible(True)
        self.pushButton_rememberPoint.setVisible(False)

        self.button_get_pose.clicked.connect(self.getPose_handler)
        self.button_get_position.clicked.connect(self.getButton_handler)
        self.positionalChenger_instance = PositionChenger(mainwindow=self)
        self.launchPositionChanger()
        self.move_button_handler()

    def launchPositionChanger(self):
        self.positionalChenger_instance.start()

    def getSpeed(self):
        return self.horizontalSlider_speed.value()/100

    def getMoveStep(self):
        return self.spinBox_move_step.value()/1000

    def getRotationStep(self):
        return self.spinBox_rotation_step.value()

    def move_button_handler(self):
        for button, move_func in self.buttons_maping:
            button.pressed.connect(move_func)
            button.released.connect(self.stopJog)

    def xUp(self):
        if not self.checkBox_moving.isChecked():
            self.robot.jogging(jog(x=self.getSpeed()))
        if self.checkBox_moving.isChecked():
            self.robot.move_along_axis('x', self.getMoveStep(), self.getSpeed())

    def xDown(self):
        if not self.checkBox_moving.isChecked():
            self.robot.jogging(jog(x=-self.getSpeed()))
        if self.checkBox_moving.isChecked():
            self.robot.move_along_axis('x', -self.getMoveStep(), self.getSpeed())

    def yUp(self):
        if not self.checkBox_moving.isChecked():
            self.robot.jogging(jog(y=self.getSpeed()))
        if self.checkBox_moving.isChecked():
            self.robot.move_along_axis('y', self.getMoveStep(), self.getSpeed())

    def yDown(self):
        if not self.checkBox_moving.isChecked():
            self.robot.jogging(jog(x=-self.getSpeed()))
        if self.checkBox_moving.isChecked():
            self.robot.move_along_axis('y', -self.getMoveStep(), self.getSpeed())

    def zUp(self):
        if not self.checkBox_moving.isChecked():
            self.robot.jogging(jog(z=self.getSpeed()))
        if self.checkBox_moving.isChecked():
            self.robot.move_along_axis('z', self.getMoveStep(), self.getSpeed())

    def zDown(self):
        if not self.checkBox_moving.isChecked():
            self.robot.jogging(jog(z=-self.getSpeed()))
        if self.checkBox_moving.isChecked():
            self.robot.move_along_axis('z', -self.getMoveStep(), self.getSpeed())

    def rxUp(self):
        if not self.checkBox_moving.isChecked():
            self.robot.jogging(jog(rx=self.getSpeed()))
        if self.checkBox_moving.isChecked():
            self.robot.move_along_axis('roll', self.getMoveStep(), self.getSpeed())

    def rxDown(self):
        if not self.checkBox_moving.isChecked():
            self.robot.jogging(jog(rx=-self.getSpeed()))
        if self.checkBox_moving.isChecked():
            self.robot.move_along_axis('roll', -self.getMoveStep(), self.getSpeed())

    def ryUp(self):
        if not self.checkBox_moving.isChecked():
            self.robot.jogging(jog(ry=self.getSpeed()))
        if self.checkBox_moving.isChecked():
            self.robot.move_along_axis('pitch', self.getMoveStep(), self.getSpeed())

    def ryDown(self):
        if not self.checkBox_moving.isChecked():
            self.robot.jogging(jog(ry=-self.getSpeed()))
        if self.checkBox_moving.isChecked():
            self.robot.move_along_axis('pitch', -self.getMoveStep(), self.getSpeed())

    def rzUp(self):
        if not self.checkBox_moving.isChecked():
            self.robot.jogging(jog(rz=self.getSpeed()))
        if self.checkBox_moving.isChecked():
            self.robot.move_along_axis('rz', self.getMoveStep(), self.getSpeed())

    def rzDown(self):
        if not self.checkBox_moving.isChecked():
            self.robot.jogging(jog(rz=-self.getSpeed()))
        if self.checkBox_moving.isChecked():
            self.robot.move_along_axis('rz', -self.getMoveStep(), self.getSpeed())

    def stopJog(self):
        if not self.checkBox_moving.isChecked():
            # self.robot.jogging(jog())
            self.robot.freeze()
        if self.checkBox_moving.isChecked():
            pass

    def getButton_handler(self):
        print(self.robot.get_position())

    def getPose_handler(self):
        print(self.robot.get_pose())

def main(host):
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    window = MovingPannel(host)
    window.show()
    app.exec_()