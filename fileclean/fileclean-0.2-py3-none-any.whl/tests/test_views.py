import os
from fileclean import view


def test_initTasks():
    setTargetPath = "tests/data/tasks.csv"
    if os.path.exists(setTargetPath):
        os.remove(setTargetPath)
    try:
        view.initTasks(targetPath=setTargetPath)
        assert os.path.exists(setTargetPath)
    finally:
        os.remove(setTargetPath)
