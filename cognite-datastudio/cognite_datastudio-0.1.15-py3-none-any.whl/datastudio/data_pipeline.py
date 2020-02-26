from typing import List

from cognite.client import CogniteClient
from cognite.datastudio.data_kit import DataKit


class DataPipeline:
    data_kits: List[DataKit] = []

    def load_data_kits(self):
        c = CogniteClient(client_name="datastudio")

        self.data_kits = []

        # Data kit 1
        data_kit = DataKit("Skarv assets and timeseries")
        data_kit.assets = c.assets.list(root_ids=[8129784932439587], limit=5000)
        data_kit.time_series = c.time_series.list(root_asset_ids=[8129784932439587], limit=5000)
        self.data_kits.append(data_kit)

    def create_relations(self, type1, type2, matches):
        print("Done")
        pass


current_data_pipeline = DataPipeline()
