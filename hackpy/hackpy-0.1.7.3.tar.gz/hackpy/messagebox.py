from ctypes import windll

# Table
MB_OK                = 0x0
MB_OK_CANCEL         = 0x01
MB_ABORTRETRYIGNORE  = 0x2
MB_YES_NO_CANCEL     = 0x03
MB_YES_NO            = 0x04
MB_RETRYCANCEL       = 0x5
MB_CANCELTRYCONTINUE = 0x6
MB_HELP              = 0x4000

ICON_ERROR           = 0x10
ICON_QUESTION        = 0x20
ICON_WARNING         = 0x30
ICON_INFORMATION     = 0x40

MB_TOPMOST = 0x40000


# MessageBox
def messagebox(text, title, settings = []):
    ##|
    ##| messagebox('Hello, this is text!', 'It\'s title!')
    ##| messagebox('text', 'title', settings=['ICON_WARNING', 'MB_RETRYCANCEL', 'MB_TOPMOST'])
    ##|
    if len(settings) >= 1:
        settings = eval(' | '.join(settings))
    else:
        settings = None
    result = windll.user32.MessageBoxW(0, text, title, settings)
    return result

