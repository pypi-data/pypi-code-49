class Master:

    def __init__(self, uniq_group_name, uniq_master_name):
        self.uniq_group_name = uniq_group_name
        self.uniq_master_name = uniq_master_name
        # [zabbix_index] to [Slave] object
        self.slaves = dict()

    def set_slaves(self, slaves):
        self.slaves = slaves

    def get_slaves(self):
        return self.slaves

    def is_configured(self) -> bool:
        return self.uniq_group_name and self.uniq_master_name

    def has_slaves(self) -> bool:
        return self.slaves and len(self.slaves) > 0
