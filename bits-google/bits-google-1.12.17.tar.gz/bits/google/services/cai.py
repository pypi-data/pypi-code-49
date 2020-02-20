# -*- coding: utf-8 -*-
"""Google Cloud Asset Inventory API."""

from bits.google.services.base import Base
from google.cloud import asset_v1
from googleapiclient.discovery import build
from google.auth.transport.requests import AuthorizedSession


class CloudAssetInventory(Base):
    """CloudAssetInventory class."""

    def __init__(self, credentials):
        """Initialize a class instance."""
        self.asset = build('cloudasset', 'v1', credentials=credentials, cache_discovery=False)
        # self.asset_v1p5alpha1 = build('cloudasset', 'v1p5alpha1', credentials=credentials, cache_discovery=False)

        self.asset_v1 = asset_v1
        self.credentials = credentials
        self.requests = AuthorizedSession(self.credentials)

    def export_assets(self, parent, body):
        """Export new asset inventory."""
        v1 = self.asset.v1()
        return v1.exportAssets(parent=parent, body=body).execute()

    def export_assets_to_bigquery(
        self,
        parent,
        asset_types=None,
        content_type=None,
        read_time=None,
        dataset=None,
        table=None,
        force=False,
    ):
        """Export Assets to BigQuery."""
        body = {
            'assetTypes': asset_types,
            'contentType': content_type,
            'outputConfig': {
                'bigqueryDestination': {
                    'dataset': dataset,
                    'table': table,
                    'force': force,
                },
            },
            'readTime': read_time,
        }
        return self.export_assets(parent, body)

    def export_assets_to_gcs(
        self,
        parent,
        asset_types=None,
        content_type=None,
        read_time=None,
        uri=None,
        uri_prefix=None,
    ):
        """Export Assets to GCS."""
        if uri:
            output_config = {'gcsDestination': {'uri': uri}}
        else:
            output_config = {'gcsDestination': {'uriPrefix': uri_prefix}}
        body = {
            'assetTypes': asset_types,
            'contentType': content_type,
            'outputConfig': output_config,
            'readTime': read_time,
        }
        return self.export_assets(parent, body)

    def get_operation(self, name):
        """Get the status of an asset inventory export operation."""
        operations = self.asset.operations()
        return operations.get(name=name).execute()

    def list_assets(
        self,
        parent,
        asset_types=None,
        content_type=None,
        snapshot_time=None,
        page_size=1000,
    ):
        """List assets."""
        body = {
            'assetTypes': asset_types,
            'contentType': content_type,
            'snapshot_time': snapshot_time

        }
        # assets = self.asset_v1p5alpha1.projects().assets()
        # request = assets.list(**params)
        # return self.get_list_items(assets, request, 'assets')
        base_url = 'https://cloudasset.googleapis.com/v1p5alpha1'
        url = '{}/{}/assets'.format(base_url, parent)
        print('URL: {}'.format(url))
        response = self.requests.post(url, data=body)
        response.raise_for_status()
        print(response.text)

        # client = asset_v1p5alpha1.AssetServiceClient()
        # response = client.list_assets(
        #     parent=parent,
        #     read_time=read_time,
        #     asset_types=asset_types,
        #     content_type=content_type,
        #     page_size=page_size,
        # )
        # for page in response.pages:
        #     for asset in page:
        #         print(asset)
