#Globals.py
#Imports
import time
import os
import math
import threading
from threading import Thread

import os.path as PATH
import glob

#import cv2
import random
import numpy as np
import scipy
import PIL
import pickle

from GlobalData import *
import GlobalData as GD

switchB = False
if switchB:
    print("Running SwitchBee")
    from pyswitchbee import SwitchBee

spotiUser = "o34ukro2jj9v71uaqv3cub4eb"


from socket import *

# sb_ip = "192.168.1.16"
sb_ip = "10.42.1.22"
# sb_ip = "10.203.203.115"

FineVol = True

class dyn(object):
    def __init__(self):
        self.name = 'Chuck Norris'
        self.phone = '+6661'
        self.dict = self.__dict__

def getDict(obj):
    return obj.__dict__

def getAllAtr(obj):
    d = {}
    cc = "_Copy"
    c = 1
    for att in dir(obj):
        at = att
        if at in d:
            while(att+cc+str(c)) in d:
                c+=1
            at = att+cc+str(c)
            c=1
        d[at] =  getattr(obj,att)
    return d


#except Exception as e: print(e)
def perpendicular_vector(v):
    if v[1] == 0 and v[2] == 0:
        if v[0] == 0:
            raise ValueError('zero vector')
        else:
            return np.cross(v, [0, 1, 0])
    return np.cross(v, [1, 0, 0])

os.environ['SPOTIPY_CLIENT_ID'] = 'd419f4fe1de143c0ab7561734322fbe2'
os.environ['SPOTIPY_CLIENT_SECRET'] = 'a5738d2f12a44336b74153cc96a1946e'
os.environ['SPOTIPY_REDIRECT_URI'] = 'http://google.com/'

gd = GlobalData()

WithSwitchBee = False
polyB = []

Debug = False
ReloadSpotify = False

ApexMap = {}

defaultFlickThresh = 40

defaultFlickThresh = 15 # easy
# defaultFlickThresh = 10 # easy
magThresh = [defaultFlickThresh]
maxMag = [-333]

CloserBigger = False
FlashApex = [True]
Gateway = gd.bind("gateway")
triggerHold = [1.5]
GatewayInfo = {"pass":Gateway,"lastTime":time.time(), "apex":None}

incoming_data = []

def isDict(obj):
	if obj is not None:
		return "dict" in str(type(obj))
	return False





showMag = [True]



PosXYZ = [1,1,10]
#gnome-terminal -e 'sh -c "echo opening Atom; sudo atom; exec bash"'
#gnome-terminal -e 'sh -c " echo EXIT_ALL; cd ~/AlphaPose; p Exit.py; sleep 0.3; killall gnome-terminal-server;"'
#gnome-terminal -e 'sh -c " cd ~/; ./start;"'

ChangeAfterCapture = [False]
ChangeOnCapture = [True]

from itertools import combinations


Devices = ["Zed1", "Zed2", "RPi2", "RPi1", "Wyze"]
Device = ["Zed1"]
#Device = ["Wyze"]
WyzeCamURL = "rtsp://magicho:magicho@192.168.1.24/live"


ShowCam = [True]
NewSP = [ReloadSpotify]

apexpath = ""
esplink = "http://10.42.0."
espIP = "21/"
ApexName = "LightA"
gesture = "Touch"
ApexDir = ""

CrashDebug = [True]
ShowRawZed = [ShowCam[0] ,400,0]
ZedRectify = True


title = ["..."]
title_status = [""]


#init.camera_resolution = sl.RESOLUTION.RESOLUTION_HD2K
#in F.py

MQTT = {}
#ZED RES F 636

MinAlphaThresh = 0.44
HeadCenter = False

MaxControllerTimer = False
MaxControllerTime = 15
ControllerTimeFrame = 0.55*2
Pass1Time = 1.3
# Pass1Time = 2


Pointers3DHistory = {"apexes":{},"done":False,"Max":10,"track":False}
xyData = [False, None, False] # keyboard flag, message, mqtt flag

SingleApex = True

AlphaDataTransfer = False
DataTransfer = list()
LoadD3D = True
imgWrappers = list()
Log = list()
PointersSet = (("LEye","LWrist"), ("REye","RWrist"))
Xserver = True

ShowBoxVis = False

TriFix2D   = False #org is True but maybe should be disabled
#TutimSteps = [False,1] #[True, 10] #org [False,1]

MaxAngleFromApex = [17] # load per apex ############# 7 also works - more accurate
#MaxTouchDistance = 15*70
MaxTouchScale = 1

DoCenterVol = True
ZedSensor = True
UseZed = False
ZedScales = [True, [-100,-100,100]]
#ZedScales = [True, [-0.1,-0.1,0.1]]

ClickServer = True
nAlpha = 2
AlphaPause = [False,0.5,0.4]
AlphaOpt = False
AlphaConf = 0.8     # 0.2
AlphaThresh = 0.15  # 0.6
AlphaFastInf = False

RunFrameG = True

MT = [None, time.time(), None]

KeyboardCommand = [False]



#size = 1480
size = 2000

#MaxArmSize = [50,10] #Tutim
MaxArmSize = [500,10] #Tutim
SetMaxArm = False
HumanThresh = 2
MaxHipDistance = 50
RemoveCloseHip = False

MusicVoiceCommands = False



#BMFactor = 1.7
BMFactor = 1

#FirstImgFunc = "JustReturn"

alignImshow = True
liveShowFeed = True
MakeSmaller = True

MaxDA, Max, trios, finalOne = 10,True,True,True # 4.321,True,True,True

collectLap = 10

gcFrameCollect = False
showGCfCount = True
fpsGCLoop = collectLap/(4*(nAlpha+1))
heavyFPS = 2
gcFCount = 0


play_recording_failed = False

printX = True
setsOfA = 3 # Size of Consistant set of AutoApexSetup
limitersA = {"dist":[True,5], "angle":[True,10], "size":[False,1.2]} # Bubble Size for Consistancy of AutoApexSetup
queue = 6 # how many of the last pointers to consider for Consistancy
delay = [True, 0.1]
stopA = [False] # To Stop AutoApexSetup


RotateFeed = [[False, 1],[False,3], None]
#Magic_Alpha
contStream = [True]
globalInput = [False, ["msg","title"], None]
SP = None
rainbowList = [(1, 0, 0, 1),(.8, 0.25, 0, 1),(1, 1, 0, 1),(0, 1, 0, 1),(0, 0, 1, 1),(1, 0, 0.3, 1),(0.3, 0, 1, 1)]
#globalInput = [False, ["msg","title"], None]
EnableTouchControllers = ["music"]


imagePath = "/home/magic/DEMO/IL/"
imagePath = "/home/magic/Training/IL/"
imagePath = "/media/magic/Cruzer/Sessions/"
imagePath = "/media/magic/EV/Sessions/"
imagePath = "/media/magic/EV1/Sessions/"
imagePath = "X/Sessions/"

Take = "NoTake"
#TakePath = "/home/magic/AlphaPose/take.txt"
TakePath = "/home/magic/MagichoRepo/AlphaPose/take.txt"


fixX, fixY, HardRotate = False, False, False
#	fixX, fixY = False,False
zmax, zmin, S = 180,120,30
#			 	(angle,scale) for (x,y,z)
floorDataPath =  imagePath + Take+"/floorData"
finalRotation = [False, floorDataPath, None]
RotateAndScale = (HardRotate,((38,1),(3,1),(0,1)))
scaleXYZ = (1,1,1)
fixData = [fixX, -60, -15, 0.65, fixY, zmax, zmin, S, RotateAndScale, finalRotation, scaleXYZ]

VectorCheckUnits = 7

#fixData = None

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
CalibPath = "/home/magic/calibration/IL/Herz2/LastDayHertz/" ; CalibNum = 70
#CalibPath = "/home/magic/calibration/ILTrue/Villa/First/" ; calibNum = 66
#CalibPath = "/home/magic/calibration/ILTrue/Villa/wall/" ; calibNum = 66
#CalibPath = "/home/magic/calibration/ILTrue/Villa/CloseUpTable/" ; calibNum = 66
#CalibPath = "/home/magic/calibration/ILTrue/Villa/improving/" ; calibNum = 103
#CalibPath = "/home/magic/calibration/ILTrue/Villa/improving/" ; calibNum = 52
#CalibPath = "/home/magic/calibration/ILTrue/Villa/Monitor1/" ; calibNum = 10
#CalibPath = "/home/magic/calibration/ILTrue/Villa/pov/" ; CalibNum = 4
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

AlreadyHavePics = False
LoadSession = False
SSHwakeSensor = True

FrameNewThread = False




def Test(obj):
	for x in range(10):
		print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")

def JustPass(obj):
	pass

def Mono3D(obj):
	pass
'''
	"&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&"
					ImagePrepFunc
	"&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&"
'''

ImagePrepFunc = Test
ImagePrepFunc = Mono3D
ImagePrepFunc = JustPass



def LoadCalibration(path):
	path = "/home/magic/calibration/IL/Herz2/LastDayHertz/"
	dbexist = PATH.exists(path)
	if dbexist:
		P1 = np.load(path+"P1.npy")
		P2 = np.load(path+"P2.npy")
		mtxL = np.load(path+"mtxL.npy")
		mtxR = np.load(path+"mtxR.npy")
		distL = np.load(path+"distL.npy")
		distR = np.load(path+"distR.npy")
		newcameramtxL = np.load(path+"newcameramtxL.npy")
		newcameramtxR = np.load(path+"newcameramtxR.npy")
		Q = np.load(path+"Q.npy")
		error = np.load(path+"error.npy")
		print(path)
		#printTitle(path, "O",3)
		#printTitle("   P1   ", "\"",3)
		print(P1)
		#printTitle("   P2   ", "\"",3)
		print(P2)
		return P1, P2, mtxL, mtxR, distL, distR, newcameramtxL, newcameramtxR, Q, error
	return None,None,None,None,None,None,None,None,None,None




'''
magic@magic-MS-7917:~$ sudo apt install ddd
[sudo] password for magic:
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following packages were automatically installed and are no longer required:
  linux-headers-4.15.0-46 linux-headers-4.15.0-46-generic
  linux-headers-4.15.0-47 linux-headers-4.15.0-47-generic
  linux-image-4.15.0-46-generic linux-image-4.15.0-47-generic
  linux-modules-4.15.0-46-generic linux-modules-4.15.0-47-generic
  linux-modules-extra-4.15.0-46-generic linux-modules-extra-4.15.0-47-generic
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  libmotif-common libxm4
Suggested packages:
  ddd-doc pydb glibc-doc gnuplot
The following NEW packages will be installed:
  ddd libmotif-common libxm4
0 upgraded, 3 newly installed, 0 to remove and 106 not upgraded.
Need to get 2,162 kB of archives.
After this operation, 6,937 kB of additional disk space will be used.
E: You don't have enough free space in /var/cache/apt/archives/.
magic@magic-MS-7917:~$ sudo apt autoclean
Reading package lists... Done
Building dependency tree
Reading state information... Done
magic@magic-MS-7917:~$ sudo apt-get autoclean
Reading package lists... Done
Building dependency tree
Reading state information... Done
magic@magic-MS-7917:~$ sudo apt autoremove
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following packages will be REMOVED:
  linux-headers-4.15.0-46 linux-headers-4.15.0-46-generic
  linux-headers-4.15.0-47 linux-headers-4.15.0-47-generic
  linux-image-4.15.0-46-generic linux-image-4.15.0-47-generic
  linux-modules-4.15.0-46-generic linux-modules-4.15.0-47-generic
  linux-modules-extra-4.15.0-46-generic linux-modules-extra-4.15.0-47-generic
0 upgraded, 0 newly installed, 10 to remove and 106 not upgraded.
After this operation, 670 MB disk space will be freed.
Do you want to continue? [Y/n] y
(Reading database ... 320153 files and directories currently installed.)
Removing linux-headers-4.15.0-46-generic (4.15.0-46.49~16.04.1) ...
Removing linux-headers-4.15.0-46 (4.15.0-46.49~16.04.1) ...
Removing linux-headers-4.15.0-47-generic (4.15.0-47.50~16.04.1) ...
Removing linux-headers-4.15.0-47 (4.15.0-47.50~16.04.1) ...
Removing linux-modules-extra-4.15.0-46-generic (4.15.0-46.49~16.04.1) ...
Removing linux-image-4.15.0-46-generic (4.15.0-46.49~16.04.1) ...
/etc/kernel/prerm.d/dkms:
dkms: removing: bbswitch 0.8 (4.15.0-46-generic) (x86_64)

-------- Uninstall Beginning --------
Module:  bbswitch
Version: 0.8
Kernel:  4.15.0-46-generic (x86_64)
-------------------------------------

Status: Before uninstall, this module version was ACTIVE on this kernel.

bbswitch.ko:
 - Uninstallation
   - Deleting from: /lib/modules/4.15.0-46-generic/updates/dkms/
 - Original module
   - No original module was found for this module on this kernel.
   - Use the dkms install command to reinstall any previous module version.

depmod....

DKMS: uninstall completed.
dkms: removing: nvidia-410 410.78 (4.15.0-46-generic) (x86_64)

-------- Uninstall Beginning --------
Module:  nvidia-410
Version: 410.78
Kernel:  4.15.0-46-generic (x86_64)
-------------------------------------

Status: Before uninstall, this module version was ACTIVE on this kernel.

nvidia_410.ko:
 - Uninstallation
   - Deleting from: /lib/modules/4.15.0-46-generic/updates/dkms/
 - Original module
   - No original module was found for this module on this kernel.
   - Use the dkms install command to reinstall any previous module version.


nvidia_410_modeset.ko:
 - Uninstallation
   - Deleting from: /lib/modules/4.15.0-46-generic/updates/dkms/
 - Original module
   - No original module was found for this module on this kernel.
   - Use the dkms install command to reinstall any previous module version.


nvidia_410_drm.ko:
 - Uninstallation
   - Deleting from: /lib/modules/4.15.0-46-generic/updates/dkms/
 - Original module
   - No original module was found for this module on this kernel.
   - Use the dkms install command to reinstall any previous module version.


nvidia_410_uvm.ko:
 - Uninstallation
   - Deleting from: /lib/modules/4.15.0-46-generic/updates/dkms/
 - Original module
   - No original module was found for this module on this kernel.
   - Use the dkms install command to reinstall any previous module version.

depmod....

DKMS: uninstall completed.
/etc/kernel/postrm.d/initramfs-tools:
update-initramfs: Deleting /boot/initrd.img-4.15.0-46-generic
/etc/kernel/postrm.d/zz-update-grub:
Generating grub configuration file ...
Warning: Setting GRUB_TIMEOUT to a non-zero value when GRUB_HIDDEN_TIMEOUT is set is no longer supported.
Found linux image: /boot/vmlinuz-4.15.0-54-generic
Found initrd image: /boot/initrd.img-4.15.0-54-generic
Found linux image: /boot/vmlinuz-4.15.0-51-generic
Found initrd image: /boot/initrd.img-4.15.0-51-generic
Found linux image: /boot/vmlinuz-4.15.0-47-generic
Found initrd image: /boot/initrd.img-4.15.0-47-generic
Found memtest86+ image: /boot/memtest86+.elf
Found memtest86+ image: /boot/memtest86+.bin
done
Removing linux-modules-extra-4.15.0-47-generic (4.15.0-47.50~16.04.1) ...
Removing linux-image-4.15.0-47-generic (4.15.0-47.50~16.04.1) ...
/etc/kernel/prerm.d/dkms:
dkms: removing: bbswitch 0.8 (4.15.0-47-generic) (x86_64)

-------- Uninstall Beginning --------
Module:  bbswitch
Version: 0.8
Kernel:  4.15.0-47-generic (x86_64)
-------------------------------------

Status: Before uninstall, this module version was ACTIVE on this kernel.

bbswitch.ko:
 - Uninstallation
   - Deleting from: /lib/modules/4.15.0-47-generic/updates/dkms/
 - Original module
   - No original module was found for this module on this kernel.
   - Use the dkms install command to reinstall any previous module version.

depmod....

DKMS: uninstall completed.
dkms: removing: nvidia-410 410.78 (4.15.0-47-generic) (x86_64)

-------- Uninstall Beginning --------
Module:  nvidia-410
Version: 410.78
Kernel:  4.15.0-47-generic (x86_64)
-------------------------------------

Status: Before uninstall, this module version was ACTIVE on this kernel.

nvidia_410.ko:
 - Uninstallation
   - Deleting from: /lib/modules/4.15.0-47-generic/updates/dkms/
 - Original module
   - No original module was found for this module on this kernel.
   - Use the dkms install command to reinstall any previous module version.


nvidia_410_modeset.ko:
 - Uninstallation
   - Deleting from: /lib/modules/4.15.0-47-generic/updates/dkms/
   - No original module was found for this module on this kernel.
   - Original module
   - Use the dkms install command to reinstall any previous module version.


nvidia_410_drm.ko:
 - Uninstallation
   - Deleting from: /lib/modules/4.15.0-47-generic/updates/dkms/
 - Original module
   - No original module was found for this module on this kernel.
   - Use the dkms install command to reinstall any previous module version.


nvidia_410_uvm.ko:
 - Uninstallation
   - Deleting from: /lib/modules/4.15.0-47-generic/updates/dkms/
 - Original module
   - No original module was found for this module on this kernel.
   - Use the dkms install command to reinstall any previous module version.

depmod....

DKMS: uninstall completed.
/etc/kernel/postrm.d/initramfs-tools:
update-initramfs: Deleting /boot/initrd.img-4.15.0-47-generic
/etc/kernel/postrm.d/zz-update-grub:
Generating grub configuration file ...
Warning: Setting GRUB_TIMEOUT to a non-zero value when GRUB_HIDDEN_TIMEOUT is set is no longer supported.
Found linux image: /boot/vmlinuz-4.15.0-54-generic
Found initrd image: /boot/initrd.img-4.15.0-54-generic
Found linux image: /boot/vmlinuz-4.15.0-51-generic
Found initrd image: /boot/initrd.img-4.15.0-51-generic
Found memtest86+ image: /boot/memtest86+.elf
Found memtest86+ image: /boot/memtest86+.bin
done
Removing linux-modules-4.15.0-46-generic (4.15.0-46.49~16.04.1) ...
Removing linux-modules-4.15.0-47-generic (4.15.0-47.50~16.04.1) ...



_________________________ cuda error
The solution can be found here 222. Basically, run the following commands in the terminal:

#sudo rmmod nvidia_uvm
#sudo rmmod nvidia
#sudo modprobe nvidia
sudo modprobe nvidia_uvm


zed serial
24061



def GetCalibConf(serial_number):
	hidden_path = '/usr/local/zed/settings/'
	calibration_file = hidden_path + 'SN' + str(serial_number) + '.conf'
	return calibration_file

import configparser
def init_calibration(calibration_file, image_size) :

	cameraMarix_left = cameraMatrix_right = map_left_y = map_left_x = map_right_y = map_right_x = np.array([])

	config = configparser.ConfigParser()
	config.read(calibration_file)

	check_data = True
	resolution_str = ''
	if image_size.width == 2208 :
		resolution_str = '2K'
	elif image_size.width == 1920 :
		resolution_str = 'FHD'
	elif image_size.width == 1280 :
		resolution_str = 'HD'
	elif image_size.width == 672 :
		resolution_str = 'VGA'
	else:
		resolution_str = 'HD'
		check_data = False

	T_ = np.array([-float(config['STEREO']['Baseline'] if 'Baseline' in config['STEREO'] else 0),
				   float(config['STEREO']['TY_'+resolution_str] if 'TY_'+resolution_str in config['STEREO'] else 0),
				   float(config['STEREO']['TZ_'+resolution_str] if 'TZ_'+resolution_str in config['STEREO'] else 0)])


	left_cam_cx = float(config['LEFT_CAM_'+resolution_str]['cx'] if 'cx' in config['LEFT_CAM_'+resolution_str] else 0)
	left_cam_cy = float(config['LEFT_CAM_'+resolution_str]['cy'] if 'cy' in config['LEFT_CAM_'+resolution_str] else 0)
	left_cam_fx = float(config['LEFT_CAM_'+resolution_str]['fx'] if 'fx' in config['LEFT_CAM_'+resolution_str] else 0)
	left_cam_fy = float(config['LEFT_CAM_'+resolution_str]['fy'] if 'fy' in config['LEFT_CAM_'+resolution_str] else 0)
	left_cam_k1 = float(config['LEFT_CAM_'+resolution_str]['k1'] if 'k1' in config['LEFT_CAM_'+resolution_str] else 0)
	left_cam_k2 = float(config['LEFT_CAM_'+resolution_str]['k2'] if 'k2' in config['LEFT_CAM_'+resolution_str] else 0)
	left_cam_p1 = float(config['LEFT_CAM_'+resolution_str]['p1'] if 'p1' in config['LEFT_CAM_'+resolution_str] else 0)
	left_cam_p2 = float(config['LEFT_CAM_'+resolution_str]['p2'] if 'p2' in config['LEFT_CAM_'+resolution_str] else 0)
	left_cam_p3 = float(config['LEFT_CAM_'+resolution_str]['p3'] if 'p3' in config['LEFT_CAM_'+resolution_str] else 0)
	left_cam_k3 = float(config['LEFT_CAM_'+resolution_str]['k3'] if 'k3' in config['LEFT_CAM_'+resolution_str] else 0)


	right_cam_cx = float(config['RIGHT_CAM_'+resolution_str]['cx'] if 'cx' in config['RIGHT_CAM_'+resolution_str] else 0)
	right_cam_cy = float(config['RIGHT_CAM_'+resolution_str]['cy'] if 'cy' in config['RIGHT_CAM_'+resolution_str] else 0)
	right_cam_fx = float(config['RIGHT_CAM_'+resolution_str]['fx'] if 'fx' in config['RIGHT_CAM_'+resolution_str] else 0)
	right_cam_fy = float(config['RIGHT_CAM_'+resolution_str]['fy'] if 'fy' in config['RIGHT_CAM_'+resolution_str] else 0)
	right_cam_k1 = float(config['RIGHT_CAM_'+resolution_str]['k1'] if 'k1' in config['RIGHT_CAM_'+resolution_str] else 0)
	right_cam_k2 = float(config['RIGHT_CAM_'+resolution_str]['k2'] if 'k2' in config['RIGHT_CAM_'+resolution_str] else 0)
	right_cam_p1 = float(config['RIGHT_CAM_'+resolution_str]['p1'] if 'p1' in config['RIGHT_CAM_'+resolution_str] else 0)
	right_cam_p2 = float(config['RIGHT_CAM_'+resolution_str]['p2'] if 'p2' in config['RIGHT_CAM_'+resolution_str] else 0)
	right_cam_p3 = float(config['RIGHT_CAM_'+resolution_str]['p3'] if 'p3' in config['RIGHT_CAM_'+resolution_str] else 0)
	right_cam_k3 = float(config['RIGHT_CAM_'+resolution_str]['k3'] if 'k3' in config['RIGHT_CAM_'+resolution_str] else 0)

	R_zed = np.array([float(config['STEREO']['RX_'+resolution_str] if 'RX_' + resolution_str in config['STEREO'] else 0),
					  float(config['STEREO']['CV_'+resolution_str] if 'CV_' + resolution_str in config['STEREO'] else 0),
					  float(config['STEREO']['RZ_'+resolution_str] if 'RZ_' + resolution_str in config['STEREO'] else 0)])

	R, _ = cv2.Rodrigues(R_zed)
	cameraMatrix_left = np.array([[left_cam_fx, 0, left_cam_cx],
						 [0, left_cam_fy, left_cam_cy],
						 [0, 0, 1]])

	cameraMatrix_right = np.array([[right_cam_fx, 0, right_cam_cx],
						  [0, right_cam_fy, right_cam_cy],
						  [0, 0, 1]])

	distCoeffs_left = np.array([[left_cam_k1], [left_cam_k2], [left_cam_p1], [left_cam_p2], [left_cam_k3]])

	distCoeffs_right = np.array([[right_cam_k1], [right_cam_k2], [right_cam_p1], [right_cam_p2], [right_cam_k3]])

	T = np.array([[T_[0]], [T_[1]], [T_[2]]])
	R1 = R2 = P1 = P2 = np.array([])

	R1, R2, P1, P2 = cv2.stereoRectify(cameraMatrix1=cameraMatrix_left,
									   cameraMatrix2=cameraMatrix_right,
									   distCoeffs1=distCoeffs_left,
									   distCoeffs2=distCoeffs_right,
									   R=R, T=T,
									   flags=cv2.CALIB_ZERO_DISPARITY,
									   alpha=0,
									   imageSize=(image_size.width, image_size.height),
									   newImageSize=(image_size.width, image_size.height))[0:4]

	map_left_x, map_left_y = cv2.initUndistortRectifyMap(cameraMatrix_left, distCoeffs_left, R1, P1, (image_size.width, image_size.height), cv2.CV_32FC1)
	map_right_x, map_right_y = cv2.initUndistortRectifyMap(cameraMatrix_right, distCoeffs_right, R2, P2, (image_size.width, image_size.height), cv2.CV_32FC1)

	cameraMatrix_left = P1
	cameraMatrix_right = P2

#	printTitle("CALIB LOADED", " ZED ")

	return cameraMatrix_left, cameraMatrix_right, map_left_x, map_left_y, map_right_x, map_right_y

class Resolution :
	width = 2208
	height = 1242



serial_number = 24061
image_size = Resolution()
calibration_file = GetCalibConf(serial_number)
ZedP1, ZedP2, map_left_x, map_left_y, map_right_x, map_right_y = init_calibration(calibration_file, image_size)
'''






gclient = "125433551197-09juo7v381ct22c732rub5l895gp94be.apps.googleusercontent.com"
gsecret = "KzoYfr_TlFE-PAMHQxSl7f73"

# Disable Enable usb (of netstick)
#echo '1-3' |sudo tee /sys/bus/usb/drivers/usb/unbind
#echo '1-3' |sudo tee /sys/bus/usb/drivers/usb/bind

# Create new sudo startup SERVICES
'''
2

This creates and runs /root/boot.sh on boot (as root) using a minimal service file:

sudo su
bootscript=/root/boot.sh
servicename=customboot

cat > $bootscript <<EOF
#!/usr/bin/env bash
echo "$bootscript ran at $(date)!" > /tmp/it-works
EOF

chmod +x $bootscript

cat > /etc/systemd/system/$servicename.service <<EOF
[Service]
ExecStart=$bootscript
[Install]
WantedBy=default.target
EOF

systemctl enable $servicename

To modify the parameters, for example to use a different $bootscript, set that variable manually and just skip that line when copying the commands.

After running the commands, you can edit the boot script using your favorite editor, and it will run on next boot. You can also immediately run it by using:

systemctl start $servicename

'''


'''

Instructions to run the inference code using PyTorch 0.4.0:

$ git clone https://github.com/atapour/monocularDepth-Inference.git
$ cd monocularDepth-Inference
$ chmod +x ./download_pretrained_models.sh
$ ./download_pretrained_models.sh
$ python3 remove_running_stats.py
$
python3 run_test.py --data_directory=./Examples --checkpoints_dir=./checkpoints --results_dir=./results

The output results are written in a directory taken as an argument to the test harness ('./results' by default):

    the script entitled "download_pretrained_models.sh" will download the required pre-trained models and checks the downloaded file integrity using MD5 checksum.
    the checkpoints that are available for direct download were created using pyTorch 0.3.1 and will not work if you are using pyTorch 0.4.0. The provided python script named ' remove_running_stats.py' will remedy the situation.
    the file with the suffix "_original" is the original input image.
    the file with the suffix "_restyled" is the style transferred image.
    the file with the suffix "_depth" is the output depth image.

'''

def printF(data=None, a=None, b=None, c=None, d=None,e=None,f=None,g=None,h=None,i=None,j=None):
	global printX
	s = ""
	ls = [data,a,b,c,d,e,f,g,h,i,j]
	for x in ls:
		if x is not None:
			s = s + str(x)

	if printX:
		print(s)

def printTitle(text, char, thick = 5, length = 70, newline=False, minimal = True):
	#x = list()
	#x.append(text)
	#return x
	TextList = list()
	text = str(text)
	head = char
	for l in range(0,int(length/(len(char)))):
		head += char
	if minimal:
		char = " "
	if newline:
		printF()
		TextList.append("")
	extra = length - len(text)
	ntext= ""
	for l in range(0, int(extra/2)+1):
		ntext += char
	ntext+=text
	for l in range(0, int(extra/2)):
		ntext += char
	while (len(ntext)<length+1):
		ntext+=char


	for r in range(0, int(thick)):
		printF(head)
		TextList.append(head)
	printF(ntext)
	TextList.append(ntext)
	for r in range(0, int(thick)):
		printF(head)
		TextList.append(head)
	if newline:
		printF()
		TextList.append("")
	return TextList

def GetMyIP():
    try:
    # if True:
    	s = socket(AF_INET, SOCK_DGRAM)
    	s.connect(("8.8.8.8", 80))
    	ip = s.getsockname()[0]
    	print("My Local IP Address is:",ip)
    	s.close()
    	return str(ip)
    except:
        printTitle("XXXXXXXx", "Offline | ")
    return None


# MyIP = GetMyIP("10.203.203.183")
# MyIP = GetMyIP("10.0.0.62")
MyIP = GetMyIP()



def SetTitle(nt = None):
	global title, title_status
	if nt is None:
		nt = title[0]+title_status[0]
		#printT(nt)
	t = '\33]0;'+nt+'\a'
	print(t, end='', flush=True)


def printT(txt,n=10):
	print("......")
	Again = True
	while Again:
		try:
			while n>0:
				Again = False
				n-=1
				print(txt)
		except:
			txt = txt+str(n)
			n = 10


def now():
	return time.time()
