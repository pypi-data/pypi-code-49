
import sys, os, shutil, requests, essentials
from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Func
from panda3d.core import Spotlight, PerspectiveLens, AmbientLight
import threading, math

def DownloadDatastore(filedir):
    if os.path.exists(os.path.split(filedir)[1]) == False:
        print("Downloading: " + filedir.ljust(50), end="")
        resp = requests.get(url="https://cdn.mknxgn.pro/datastore/GET/" + filedir)
        if resp.status_code == 200:
            print("OK")
            essentials.write_file(os.path.split(filedir)[1], resp.content, byte=True)
        else:
            print("FAILED")
            raise ConnectionError("Downloading Model Failed. Check MkNxGn's CDN State/Internet Connection!")

# pylint: skip-file

class __model__loader__(object):

    def __init__(self):
        super().__init__()

    @property
    def DRONE(self):
        DownloadDatastore("mk_mpu6050_tools/models/Drone.egg")
        return "Drone.egg"

    @property
    def TRUCK(self):
        DownloadDatastore("mk_mpu6050_tools/models/Truck.egg")
        return "Truck.egg"

    @property
    def PLANE(self):
        DownloadDatastore("mk_mpu6050_tools/models/Plane.egg")
        return "Plane.egg"

    @property
    def GRYO_MULTIPLEX(self):
        DownloadDatastore("mk_mpu6050_tools/models/GyroSpin.egg")
        DownloadDatastore("mk_mpu6050_tools/models/GyroBase.egg")
        return "gyro_multiplex"




class __z_Underground__(ShowBase):
    def __init__(self, Gyro, model, use_offset=True):
        self.Gyro = Gyro
        self.offset = use_offset
        self.X = 0
        self.Y = 0
        self.Z = 0
        ShowBase.__init__(self)
        self.setBackgroundColor(0.25, 0.25, 0.5)
        self.disableMouse()

        Updater = Func(self.Update_Orientation)
        Updater.loop()

        self.camLens.setNearFar(1.0, 90.0)
        self.camLens.setFov(45.0)

        camera.setPos(5.0, 15.0, 5.0)  # pylint:disable=invalid-name,used-before-assignment
        camera.lookAt(0,0,0)  # pylint:disable=invalid-name,used-before-assignment

        root = render.attachNewNode("Root")  # pylint:disable=invalid-name,used-before-assignment
        root.setPos(0.0, 0.0, 0.0)

        if model == "gyro_multiplex":
            self.Multiplex = True
            self.base = Actor("GyroBase.egg")
            self.base.reparentTo(render)  # pylint:disable=invalid-name,used-before-assignment
            self.base.setPos(0, 0.0, 0.0)

            self.spin = Actor("GyroSpin.egg")
            self.spin.reparentTo(render)  # pylint:disable=invalid-name,used-before-assignment
            self.spin.setPos(0, 0.0, 0.0)
        else:
            self.Multiplex = False
            self.cube = Actor(model)
            self.cube.reparentTo(render)  # pylint:disable=invalid-name,used-before-assignment
            self.cube.setPos(0, 0.0, 0.0)

        self.accept("escape", sys.exit)

        self.accept("o", self.oobe)

        slight = Spotlight('slight')
        slight.setColor((1, 1, 1, 1))
        lens = PerspectiveLens()
        slight.setLens(lens)

        slnp = render.attachNewNode(slight)  # pylint:disable=invalid-name,used-before-assignment
        slnp.setPos(5.0, 10.0, 5.0) 
        slnp.lookAt(0,0,0)
        render.setLight(slnp)  # pylint:disable=invalid-name,used-before-assignment

        alight = AmbientLight('alight')
        alight.setColor((0.5, 0.5, 0.5, 1))
        alnp = render.attachNewNode(alight)  # pylint:disable=invalid-name,used-before-assignment
        render.setLight(alnp)  # pylint:disable=invalid-name,used-before-assignment
        

    def Update_Orientation(self):
        if self.Multiplex:
            if self.offset:
                X = self.Gyro.x.offset_value
                Y = self.Gyro.y.offset_value
                Z = self.Gyro.z.offset_value
            else:
                X = self.Gyro.x.value
                Y = self.Gyro.y.value
                Z = self.Gyro.z.value
                
            Roll = Y * 0.7
            Pitch = X * 0.7
            
            self.base.setHpr(0, Pitch, 0)
            self.spin.setHpr(0, 0, Roll)
        else:
            if self.offset:
                X = self.Gyro.x.offset_value
                Y = self.Gyro.y.offset_value
                Z = self.Gyro.z.offset_value
            else:
                X = self.Gyro.x.value
                Y = self.Gyro.y.value
                Z = self.Gyro.z.value
                
            Roll = Y * 0.7
            Pitch = X * 0.7
            Yaw = 0 #math.degrees(math.atan2(Z, (abs(X) - abs(Y))))
            
            self.cube.setHpr(Yaw, Pitch, Roll)


MODELS = __model__loader__()

def Run_visiulization_on_Gyro(Gyro, model=MODELS.GRYO_MULTIPLEX, use_offset=True):
    Visulize = __z_Underground__(Gyro, model=model, use_offset=True)
    Visulize.run()