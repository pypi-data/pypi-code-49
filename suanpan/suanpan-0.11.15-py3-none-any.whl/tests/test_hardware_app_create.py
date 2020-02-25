from suanpan import api

h = api.Hardware("192.168.199.108")
h.suanpan.init("https://spnext.xuelangyun.com")
h.apps.create("24870")
