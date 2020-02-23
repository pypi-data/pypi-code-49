#!/usr/bin/python3
# -*- coding: utf-8 -*-
# import _4quila

from tornado.ioloop import IOLoop

def start():
    return IOLoop.current().start()

def run(func):
    return IOLoop.current().run_sync(func)
