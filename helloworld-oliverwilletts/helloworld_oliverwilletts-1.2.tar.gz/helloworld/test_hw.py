import hw

def test_one():  # These must be named "test_" then a number for the test all in lowercase
    t1 = hw.Hello()  # Instantiate a new "Hello" class from the "hw" script and store its output into t1
    assert str(t1) == "Hello World!"  # Test if the output is "Hello World!"

def test_two():
    t2 = hw.Hello()
    assert str(t2) == "Goodbye World!"

def test_three():
    t3 = hw.Hello("Goodbye World!")
    assert str(t3) == "Goodbye World!"
