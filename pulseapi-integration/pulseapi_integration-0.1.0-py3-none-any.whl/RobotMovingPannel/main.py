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
            (self.button_xUp,       self.jogXup,    self.move_step_Xup),
            (self.button_xDown,     self.jogXdown,  self.move_step_Xdown),
            (self.button_yUp,       self.jogYup,    self.move_step_Yup),
            (self.button_yDown,     self.jogYdown,  self.move_step_Ydown),
            (self.button_zDown,     self.jogZdown,  self.move_step_Zdown),
            (self.button_zUp,       self.jogZup,    self.move_step_Zup),
            (self.button_rollUp,    self.jogRXup,   self.move_step_RXup),
            (self.button_rollDown,  self.jogRXdown, self.move_step_RXdown),
            (self.button_pitchUp,   self.jogRYup,   self.move_step_RYup),
            (self.button_pitchDown, self.jogRYdown, self.move_step_RYdown),
            (self.button_yawUp,     self.jogRZup,   self.move_step_RZup),
            (self.button_yawDown,   self.jogRZdown, self.move_step_RZdown)
        ]

        self.lineEdit_mapping = [
            self.lineEdit_x,
            self.lineEdit_y,
            self.lineEdit_z,
            self.lineEdit_roll,
            self.lineEdit_pitch,
            self.lineEdit_yaw
        ]

        # self.checkBox_moving.toggled.connect(self.spinBox_move_step.setEnabled)
        # self.checkBox_moving.toggled.connect(self.spinBox_rotation_step.setEnabled)
        # self.checkBox_moving.toggled.connect(self.change)
        # self.change()

        # Disable some functions
        self.label_move_step.setVisible(False)
        self.checkBox_moving.setVisible(False)
        self.spinBox_move_step.setVisible(False)
        self.label_rotation_step.setVisible(False)
        self.spinBox_rotation_step.setVisible(False)
        self.pushButton_rememberPoint.setVisible(False)

        self.button_get_pose.clicked.connect(self.getPose_handler)
        self.button_get_position.clicked.connect(self.getButton_handler)
        self.positionalChenger_instance = PositionChenger(mainwindow=self)
        self.launchPositionChanger()
        self.jogMove()

    def launchPositionChanger(self):
        self.positionalChenger_instance.start()

    def change(self):
        if self.checkBox_moving.isChecked():
            self.stepMove()

        if self.checkBox_moving.isChecked():
            self.jogMove()

    def getSpeed(self):
        return self.horizontalSlider_speed.value()/100

    def getMoveStep(self):
        return self.spinBox_move_step.value()/1000

    def getRotationStep(self):
        return self.spinBox_rotation_step.value()

    def jogMove(self):
        for button, jog_func, _ in self.buttons_maping:
            button.pressed.connect(jog_func)
            button.released.connect(self.stopJog)

    def stepMove(self):
        for button, _, step_move_func in self.buttons_maping:
            button.pressed.connect(step_move_func)

    def jogXup(self):
        self.robot.jogging(jog(x=self.getSpeed()))
        # print("Up")
    def jogXdown(self):
        self.robot.jogging(jog(x=-self.getSpeed()))
        # print("Down")

    def jogYup(self):
        self.robot.jogging(jog(y=self.getSpeed()))
    def jogYdown(self):
        self.robot.jogging(jog(y=-self.getSpeed()))

    def jogZup(self):
        self.robot.jogging(jog(z=self.getSpeed()))
    def jogZdown(self):
        self.robot.jogging(jog(z=-self.getSpeed()))

    def jogRXup(self):
        self.robot.jogging(jog(rx=self.getSpeed()))
    def jogRXdown(self):
        self.robot.jogging(jog(rx=-self.getSpeed()))

    def jogRYup(self):
        self.robot.jogging(jog(ry=self.getSpeed()))
    def jogRYdown(self):
        self.robot.jogging(jog(ry=-self.getSpeed()))

    def jogRZup(self):
        self.robot.jogging(jog(rz=self.getSpeed()))
    def jogRZdown(self):
        self.robot.jogging(jog(rz=-self.getSpeed()))

    def stopJog(self):
        # print('Stop')
        self.robot.freeze()
        # self.robot.jogging(jog())

    def move_step_Xup(self):
        # self.robot.move_along_axis('x', self.getMoveStep(), self.getSpeed())
        print("stepX")
    def move_step_Xdown(self):
        # self.robot.move_along_axis('x', -self.getMoveStep(), self.getSpeed())
        print('stepXD')

    def move_step_Yup(self):
        self.robot.move_along_axis('y', self.getMoveStep(), self.getSpeed())
    def move_step_Ydown(self):
        self.robot.move_along_axis('y', -self.getMoveStep(), self.getSpeed())

    def move_step_Zup(self):
        self.robot.move_along_axis('z', self.getMoveStep(), self.getSpeed())
    def move_step_Zdown(self):
        self.robot.move_along_axis('z', -self.getMoveStep(), self.getSpeed())

    def move_step_RXup(self):
        self.robot.move_along_axis('roll', self.getRotationStep(), self.getSpeed())
    def move_step_RXdown(self):
        self.robot.move_along_axis('roll', -self.getRotationStep(), self.getSpeed())

    def move_step_RYup(self):
        self.robot.move_along_axis('pitch', self.getRotationStep(), self.getSpeed())
    def move_step_RYdown(self):
        self.robot.move_along_axis('pitch', -self.getRotationStep(), self.getSpeed())

    def move_step_RZup(self):
        self.robot.move_along_axis('yaw', self.getRotationStep(), self.getSpeed())
    def move_step_RZdown(self):
        self.robot.move_along_axis('yaw', -self.getRotationStep(), self.getSpeed())

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