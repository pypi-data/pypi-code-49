import sys
sys.path.insert(0, "..")
from geistt_lab_rti_client import RTI, proto
import time

rti = RTI(application_id="python_test", suppress_own_messages=True)

def on_connect():
    print("Connected")

    def on_control(message: proto.RuntimeControl):
        print("control message", message)
    rti.subscribe("control", proto.RuntimeControl, on_control)

    message = proto.RuntimeControl()
    message.load_scenario.name = "python_test"
    rti.publish("control", message)


def on_disconnect():
    print("Disconnected")


def on_error(type, message, exception):
    print(f"Error: {type}: {message}")


rti.on("error", on_error)
rti.on("connect", on_connect)
rti.on("disconnect", on_disconnect)

time.sleep(3)
rti.socket.disconnect()
print("kthxbye")
time.sleep(0.5)
