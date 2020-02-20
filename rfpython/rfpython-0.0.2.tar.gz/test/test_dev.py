import rfpython


def test_same_folder():
    rfpython.run("dummy.py", "hello2")
    pass


def test_other_folder():
    rfpython.run("crap/dummy.py", "hello2")
    pass


def test_dir_logic():
    rfpython.dir_logic("crap/dummy.py")
    return


if __name__ == "__main__":
    test_other_folder()
