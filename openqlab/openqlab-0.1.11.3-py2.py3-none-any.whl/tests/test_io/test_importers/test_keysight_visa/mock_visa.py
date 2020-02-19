from re import match
from typing import List


class MockVisa:
    def __init__(self):
        self.log = []
        self.read_termination = ""
        self.waveform_channel: str = None
        self.waveform_points: int = None
        self.waveform_format: str = None
        self.channels_enabled: List[str] = ["0"] * 4
        self.channel_data = {
            "channel1": "#800000139 1.35683e-002,-1.19603e-002,-3.11608e-003, 6.33216e-003, 9.14623e-003, 7.13618e-003, 1.03523e-002, 3.11608e-003, 5.93015e-003, 1.19603e-002",
            "channel2": "#800000139 2.35683e-002,-2.19603e-002,-4.11608e-003, 7.33216e-003, 9.14623e-003, 7.13618e-003, 1.03523e-002, 3.11608e-003, 5.93015e-003, 2.19603e-002",
            "channel3": "#800000139 3.35683e-002,-3.19603e-002,-5.11608e-003, 6.33216e-003, 9.14623e-003, 7.13618e-003, 1.03523e-002, 3.11608e-003, 5.93015e-003, 3.19603e-002",
            "channel4": "#800000139 4.35683e-002,-4.19603e-002,-7.11608e-003, 6.33216e-003, 9.14623e-003, 7.13618e-003, 1.03523e-002, 3.11608e-003, 5.93015e-003, 4.19603e-002",
        }
        self.idn = "KEYSIGHT TECHNOLOGIES,DSO-X 3024T,MY57452230,07.30.2019051434"

    def open_resource(self, _: str):
        return self

    def write(self, command: str):
        known_commands = [":run", ":stop", ":waveform:points:mode"]

        self.log.append(f"write: {command}")
        print(self.log)

        commands: list = command.lower().strip().split(" ")
        if commands[0] == ":waveform:source":
            self.waveform_channel = commands[1]
        elif commands[0] == ":waveform:points":
            self.waveform_points = int(commands[1])
        elif commands[0] == ":waveform:format":
            self.waveform_points = commands[1]
        elif commands[0] in known_commands:
            pass
        else:
            raise ValueError(f"Unknown command: {command}")

    def query(self, query: str):
        self.log.append(f"query: {query}")
        print(self.log)

        query = query.lower().strip()

        if query == "wav:preamble?":
            return "+4,+0,+10,+1,+8.00000000E-005,-4.00000000E-004,+0,+1.57035200E-006,-1.00000000E-004,+32768"
        if query == "wav:data?":
            return self.channel_data[self.waveform_channel]
        if query == "*idn?":
            return self.idn
        m = match(r":channel(.):display\?", query)
        if m is not None:
            chan = int(m.group(1))
            return self.channels_enabled[chan - 1]

        raise ValueError(f"Unknown query: {query}")
