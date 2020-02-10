""" Proxy for ctrl-v main
ctrl-v cannot be directly used in setup.py entry_points
"""
import importlib

ctrl_v = importlib.import_module("ctrl-v")

main = ctrl_v.main
