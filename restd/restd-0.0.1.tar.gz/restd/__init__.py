"""
restd is a REST service that routes incoming data to plugins.
The goal is to provide a lightweight, flexible, and extensible
REST framework manged by service configs
"""
import os
from . import restd

name = "restd"
