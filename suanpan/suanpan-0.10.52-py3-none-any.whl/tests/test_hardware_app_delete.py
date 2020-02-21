from suanpan import api

h = api.Hardware("192.168.199.108")
h.apps.delete("24870")
