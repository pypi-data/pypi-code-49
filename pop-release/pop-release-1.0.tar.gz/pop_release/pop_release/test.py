# Import python libs
import subprocess


def pytest(hub):
    """
    Run pytest and fail the sequence if pytest fails
    """
    retcode = subprocess.run("pytest").returncode
    if retcode == 5:
        # No tests, skip
        print("This project has no tests")
        return
    fail = bool(retcode)
    if fail:
        raise Exception("Pytest failed")
