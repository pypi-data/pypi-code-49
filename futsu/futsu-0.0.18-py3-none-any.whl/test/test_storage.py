from unittest import TestCase
import futsu.storage as storage
import tempfile
import os
import futsu.fs as fs
import time
import futsu.json
import json

class TestStorge(TestCase):

    def test_local(self):
        with tempfile.TemporaryDirectory() as tempdir:
            tmp_filename = os.path.join(tempdir,'QKDQXVOOME')
            src_file = os.path.join('futsu','test','test_storage_0.txt')
            
            self.assertFalse(storage.is_blob_exist(tmp_filename))
            
            storage.local_to_path(tmp_filename,src_file)
            self.assertTrue(storage.is_blob_exist(tmp_filename))
            self.assertFalse(fs.diff(tmp_filename,src_file))

            storage.rm(tmp_filename)
            self.assertFalse(storage.is_blob_exist(tmp_filename))
            
            tmp_filename = os.path.join(tempdir,'NKNVMMYPUI')
            bytes0=b'YENLUMVECW'
            storage.bytes_to_path(tmp_filename,bytes0)
            bytes1=storage.path_to_bytes(tmp_filename)
            self.assertEqual(bytes0,bytes1)

    def test_gcp(self):
        with tempfile.TemporaryDirectory() as tempdir:
            tmp_filename = os.path.join(tempdir,'GPVRUHXTTC')
            src_file = os.path.join('futsu','test','test_storage_0.txt')
            timestamp = int(time.time())
            tmp_gs_blob = 'gs://futsu-test/test-NXMUHBDEMR-{0}'.format(timestamp)

            self.assertFalse(storage.is_blob_exist(tmp_gs_blob))
            
            storage.local_to_path(tmp_gs_blob,src_file)
            self.assertTrue(storage.is_blob_exist(tmp_gs_blob))

            storage.path_to_local(tmp_filename,tmp_gs_blob)
            self.assertFalse(fs.diff(tmp_filename,src_file))

            storage.rm(tmp_gs_blob)
            self.assertFalse(storage.is_blob_exist(tmp_gs_blob))

            tmp_gs_blob = 'gs://futsu-test/test-DQZFYPFNUV-{0}'.format(timestamp)
            bytes0=b'RZCPRGZZBC'
            storage.bytes_to_path(tmp_gs_blob,bytes0)
            bytes1=storage.path_to_bytes(tmp_gs_blob)
            self.assertEqual(bytes0,bytes1)

    def test_s3(self):
        with tempfile.TemporaryDirectory() as tempdir:
            tmp_filename = os.path.join(tempdir,'TMWGHOKDRE')
            src_file = os.path.join('futsu','test','test_storage_0.txt')
            timestamp = int(time.time())
            tmp_path = 's3://futsu-test/test-KWPIYZVIYK-{0}'.format(timestamp)

            self.assertFalse(storage.is_blob_exist(tmp_path))
            
            storage.local_to_path(tmp_path,src_file)
            self.assertTrue(storage.is_blob_exist(tmp_path))

            storage.path_to_local(tmp_filename,tmp_path)
            self.assertFalse(fs.diff(tmp_filename,src_file))

            storage.rm(tmp_path)
            self.assertFalse(storage.is_blob_exist(tmp_path))

            tmp_gs_blob = 's3://futsu-test/test-LKUDEBPHEF-{0}'.format(timestamp)
            bytes0=b'SUZODZKFXW'
            storage.bytes_to_path(tmp_gs_blob,bytes0)
            bytes1=storage.path_to_bytes(tmp_gs_blob)
            self.assertEqual(bytes0,bytes1)

    def test_http(self):
        with tempfile.TemporaryDirectory() as tempdir:
            tmp_filename = os.path.join(tempdir,'RICFYWBCVI')
            tmp_path = 'https://httpbin.org/get'
            storage.path_to_local(tmp_filename,tmp_path)
            data = futsu.json.file_to_data(tmp_filename)
            self.assertEqual(data['url'],tmp_path)

            data = storage.path_to_bytes(tmp_path)
            data = json.loads(data)
            self.assertEqual(data['url'],tmp_path)
