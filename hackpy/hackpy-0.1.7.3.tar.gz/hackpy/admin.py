from ctypes import windll

# Check if program started as admin
def isAdmin():
    status = windll.shell32.IsUserAnAdmin()
    if (status == 1):
        return True
    else:
        return False

# Set wallpaper
def setWallpaper(image):
    return windll.user32.SystemParametersInfoW(20, 0, image, 0)
