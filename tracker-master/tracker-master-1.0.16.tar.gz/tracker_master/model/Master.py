class Master:

    def __init__(self, uniq_group_name, uniq_master_name):
        self.uniq_group_name = uniq_group_name
        self.uniq_master_name = uniq_master_name

    def is_initialized(self) -> bool:
        return self.uniq_group_name and self.uniq_master_name
