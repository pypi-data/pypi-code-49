from . import api, device_status, obd, location
import asyncio
import logging

def main():
    la = api.API("http://www.aika168.com/")
    la.registerUpdater(location.Location(la))
    la.registerUpdater(device_status.DeviceStatus(la))

    loop = asyncio.get_event_loop()

    loop.run_until_complete( la.doLogin('7018095531', '770608') )
    loop.run_until_complete(la.doUpdate())

    attrs = vars(la)
    
    print(', '.join("%s: %s" % item for item in attrs.items()))

if __name__ == "__main__":
    main()