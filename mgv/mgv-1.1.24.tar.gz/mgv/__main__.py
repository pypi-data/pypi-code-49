#! /usr/bin/env python
# -- coding: utf-8 --


def set_procname(newname):
    """Change a process name"""
    from ctypes import cdll, byref, create_string_buffer
    libc = cdll.LoadLibrary('libc.so.6')
    buff = create_string_buffer(len(newname) + 1)
    buff.value = newname
    libc.prctl(15, byref(buff), 0, 0, 0)


if __name__ == "__main__":
    # execute only if run as a script
    #import mgv.mgvUI as mgvUI
    import mgvUI
    mgvUI.main()
    try:
        set_procname('mangrove')
    except:
        pass