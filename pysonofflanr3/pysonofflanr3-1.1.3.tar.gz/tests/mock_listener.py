import sys
from datetime import datetime
from zeroconf import ServiceBrowser, Zeroconf


class MyListener:
    def remove_service(self, zeroconf, type, name):

        global name_filter

        if name_filter in name:
            print("%s - Service %s removed" % (datetime.now(), name))
            print(zeroconf.get_service_info(type, name))

    def add_service(self, zeroconf, type, name):

        global name_filter

        if name_filter in name:
            print("%s - Service %s added" % (datetime.now(), name))
            print(zeroconf.get_service_info(type, name))

            # For zeroconf 0.23.0, this is needed as updates only
            # come to the child entry
            # self.browser = ServiceBrowser(zeroconf, name, listener)

    def update_service(self, zeroconf, type, name):

        global name_filter

        if name_filter in name:
            print("%s - Service %s updated" % (datetime.now(), name))
            print(zeroconf.get_service_info(type, name))


if __name__ == "__main__":

    global name_filter
    name_filter = ""

    try:
        name_filter = sys.argv[1]

    except IndexError:
        pass

    zeroconf = Zeroconf()
    listener = MyListener()

    listener.browser = ServiceBrowser(
        zeroconf, "_ewelink._tcp.local.", listener
    )

    try:
        input("Press enter to exit...\n\n")

    finally:
        zeroconf.close()
