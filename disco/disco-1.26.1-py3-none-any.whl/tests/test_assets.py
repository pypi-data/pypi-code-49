#  Copyright (c) 2019 Samsung, Inc. and its affiliates.
#
#  This source code is licensed under the RESTRICTED license found in the
#  LICENSE file in the root directory of this source tree.

import io
import os
import pathlib
import uuid

import mock
import pytest
import requests

import disco
from disco.core.constants import ClusterType
from disco.models import ClusterDetails
from .base_test import BaseTest
from disco import Asset
from contextlib import contextmanager

test_file_dir = os.path.dirname(os.path.realpath(__file__))
txt_file = os.path.join(test_file_dir, 'test_files', 'text_file.txt')
img_file = os.path.join(test_file_dir, 'test_files', 'disco-logo.png')

file_content = {}


class FTypes(object):
    text = 'Text'
    image = 'Image'


def setup_module():
    global file_content
    with io.FileIO(txt_file) as txt_f:
        file_content[FTypes.text] = txt_f.read()

    with io.FileIO(img_file) as img_f:
        file_content[FTypes.image] = img_f.read()


class TestAsset(BaseTest):

    def test__request_url_for_upload_with_cluster(self):
        file_name = self.random_str('filename')
        cluster_id = self.random_str('cluster_id')
        request_params = {
            'key': file_name,
            'clusterId': cluster_id
        }
        with mock.patch('disco.asset.Asset.rest') as fake_rest:
            Asset()._request_url_for_upload(file_name, cluster_id)
            fake_rest.assert_called_once_with(url='/files/uploadparams',
                                              data=request_params,
                                              method='post')

    def test__request_url_for_upload_without_cluster(self):
        file_name = self.random_str('filename')
        request_params = {
            'key': file_name,
        }
        with mock.patch('disco.asset.Asset.rest') as fake_rest:
            Asset()._request_url_for_upload(file_name, None)
            fake_rest.assert_called_once_with(url='/files/uploadparams',
                                              data=request_params,
                                              method='post')

    def test__register_file(self):
        token = self.random_str('token')
        send_result = self.random_str('id')

        with mock.patch('disco.asset.Asset.rest') as fake_rest:

            fake_rest.return_value = {'id': send_result}
            result = Asset()._register(token)
            fake_rest.assert_called_once_with(url='/files',
                                              data={'token': token},
                                              method='post')
            assert result == send_result

    file_argument_parameters = [
        (b'Lol I have text \n and newlines here.', FTypes.text),
        ('Lol I have text \n and newlines here.', FTypes.text),
        (io.StringIO('Lol I have text \n and newlines here.'), FTypes.text),
        (io.BytesIO(b'Lol I have text \n and newlines here.'), FTypes.text),
        (open(os.path.abspath(txt_file), 'r'), FTypes.text),
        (open(os.path.abspath(txt_file), 'rb'), FTypes.text),
        (pathlib.Path(txt_file), FTypes.text),
        (pathlib.Path(img_file), FTypes.image),
        (open(os.path.abspath(img_file), 'rb'), FTypes.image)
    ]
    @pytest.mark.parametrize('file_argument', file_argument_parameters)
    def test_upload_file_mocked_with_default_cluster(self, file_argument):
        generated_id = str(uuid.uuid4())
        generated_url = '/some-storage/%s' % generated_id
        generated_name = 'file_%s.bin' % generated_id
        generated_token = 'token>%s' % generated_id
        generated_fields = {'x': generated_id, 'y': generated_name}

        with mock.patch('disco.asset.Asset._request_url_for_upload') \
                as request_url_mock, \
                mock.patch('disco.asset.Asset._upload_to_aws_with_callback') as _upload_to_aws_with_callback, \
                mock.patch('disco.asset.Asset._register') as register_file_mock:

            request_url_mock.return_value = {
                'url': generated_url,
                'fields': generated_fields,
                'token': generated_token
            }

            register_file_mock.return_value = generated_id

            file_id = disco.asset.upload_file(generated_name, file_argument[0], show_progress_bar=False)

            request_url_mock.assert_called_once_with(generated_name, None)
            expected_body = file_content[file_argument[1]]

            _upload_to_aws_with_callback.assert_called_once_with(
                generated_url, generated_name, form_fields=generated_fields,
                file_content_bytes=expected_body, callback=self.is_function())
            register_file_mock.assert_called_once_with(generated_token)

            assert file_id == generated_id

    def test_upload_file_mocked_with_GCP_cluster(self):
        cluster_id = self.random_str('cluster_id')
        cluster = ClusterDetails(dict(id=cluster_id, type=ClusterType.GCP.value))

        file_argument = (pathlib.Path(txt_file), FTypes.text)

        file_id = str(uuid.uuid4())
        generated_url = '/some-storage/%s' % file_id
        generated_name = 'file_%s.bin' % file_id
        generated_token = 'token>%s' % file_id

        with mock.patch('disco.asset.Asset._request_url_for_upload') \
                as request_url_mock, \
                mock.patch('disco.asset.Asset._upload_to_gcp_with_callback') as _upload_to_gcp_with_callback, \
                mock.patch('disco.asset.Asset._register') as register_file_mock:

            request_url_mock.return_value = {
                'url': generated_url,
                'token': generated_token
            }

            register_file_mock.return_value = file_id

            file_id = disco.asset.upload_file(generated_name, file_argument[0], cluster, show_progress_bar=False)

            request_url_mock.assert_called_once_with(generated_name, cluster_id)
            expected_body = file_content[file_argument[1]]

            _upload_to_gcp_with_callback.assert_called_once_with(
                generated_url,
                file_content_bytes=expected_body,
                callback=self.is_function()
            )
            register_file_mock.assert_called_once_with(generated_token)

            assert file_id == file_id

    def test_upload_file_mocked_with_azure_cluster(self):
        cluster_id = self.random_str('cluster_id')
        cluster = ClusterDetails(dict(id=cluster_id, type=ClusterType.Azure.value))

        file_argument = (pathlib.Path(txt_file), FTypes.text)

        file_id = str(uuid.uuid4())
        generated_url = '/some-storage/%s' % file_id
        generated_name = 'file_%s.bin' % file_id
        generated_token = 'token>%s' % file_id

        with mock.patch('disco.asset.Asset._request_url_for_upload') \
                as request_url_mock, \
                mock.patch('disco.asset.Asset._upload_to_azure') as _upload_to_azure, \
                mock.patch('disco.asset.Asset._register') as register_file_mock:

            request_url_mock.return_value = {
                'url': generated_url,
                'token': generated_token
            }

            register_file_mock.return_value = file_id

            file_id = disco.asset.upload_file(generated_name, file_argument[0], cluster, show_progress_bar=False)

            request_url_mock.assert_called_once_with(generated_name, cluster_id)
            expected_body = file_content[file_argument[1]]

            _upload_to_azure.assert_called_once_with(
                generated_url,
                file_content_bytes=expected_body,
            )
            register_file_mock.assert_called_once_with(generated_token)

            assert file_id == file_id

    def test_input_files_from_bucket(self):
        bucket_paths = self.random_list('bucket_path', length=3)
        cluster_id = self.random_str('clusterId')
        request_params = {'bucketPaths': bucket_paths, 'clusterId': cluster_id}
        fake_input_files = [dict(id=self.random_str('file_id')) for _ in range(3)]
        expected_input_file_ids = [fake_input_file['id'] for fake_input_file in fake_input_files]

        with mock.patch('disco.asset.Asset.rest') as fake_rest:
            fake_rest.return_value = fake_input_files

            result = Asset().input_files_from_bucket(bucket_paths, cluster_id)

            fake_rest.assert_called_once_with(url='/files/bucket', data=request_params, method='post')
            assert result == expected_input_file_ids

    def test_input_files_from_bucket_no_files_found(self):
        bucket_paths = self.random_list('bucket_path', length=3)
        cluster_id = self.random_str('clusterId')
        request_params = {'bucketPaths': bucket_paths, 'clusterId': cluster_id}
        empty_response = None

        with mock.patch('disco.asset.Asset.rest') as fake_rest:
            fake_rest.return_value = empty_response

            result = Asset().input_files_from_bucket(bucket_paths, cluster_id)

            fake_rest.assert_called_once_with(url='/files/bucket', data=request_params, method='post')
            assert result == []
