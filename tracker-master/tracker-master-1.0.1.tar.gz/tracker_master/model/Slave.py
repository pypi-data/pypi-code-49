from enum import Enum


class Slave:

    def __init__(self, hw_id, zbx_slave_number):
        self.hw_id = hw_id
        self.zbx_slave_number = zbx_slave_number
        self.monitorings = list()

    def __eq__(self, o: object) -> bool:
        return isinstance(o, Slave) and self.hw_id == o.hw_id

    def __hash__(self) -> int:
        return hash(self.hw_id)


class MonitoringName(Enum):
    ALARM = 'alarm'
    CHARGE = 'charge'
    TEST = 'test'


class Monitoring:

    zbx_id = None

    name = None

    active = None

    def __init__(self, zbx_id, name, active):
        assert isinstance(name, MonitoringName)
        self.zbx_id = zbx_id
        self.name = name
        self.active = active