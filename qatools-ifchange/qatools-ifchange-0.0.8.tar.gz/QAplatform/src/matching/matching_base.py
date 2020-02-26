class MatchingBase:
    def __init__(self, dict_map, config):
        self.dict_map = dict_map
        self.config = config

    def compute_simlarity(self, query_info, retrived_indices):
        raise NotImplementedError("Matching plugin must have computer_similartiy function")

