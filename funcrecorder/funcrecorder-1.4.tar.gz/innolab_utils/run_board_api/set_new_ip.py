
from innopy.api import *
from src.json_config import get_config


def main():
    ip = "10.1.1.101"
    di = DeviceInterface()

    di.set_dp("networkIPAddr", ip, True)


if __name__ == "__main__":
    main()
