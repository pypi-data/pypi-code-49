import os
import pytest
import six

from girder.models.folder import Folder
from girder.models.upload import Upload
from girder.plugin import loadedPlugins


# It would be nice if this were its own test, but we can't use the dicom
# plugin twice in girder pytests.
# @pytest.mark.plugin('girder_archive_access')
# def test_import(server):
#     assert 'girder_archive_access' in loadedPlugins()


@pytest.mark.plugin('girder_archive_access')
def test_archiveEndpoints(server, admin, fsAssetstore):
    # See comments above
    assert 'girder_archive_access' in loadedPlugins()

    testDir = os.path.dirname(os.path.realpath(__file__))
    filePath = os.path.join(testDir, 'TCIA.image.tar.bz2')
    name = os.path.basename(filePath)
    publicFolder = Folder().find({
        'parentId': admin['_id'],
        'name': 'Public',
    })[0]
    file = Upload().uploadFromFile(
        open(filePath, 'rb'), os.path.getsize(filePath), name,
        parentType='folder', parent=publicFolder,
        user=admin, assetstore=fsAssetstore)

    resp = server.request(
        path='/file/%s/archive' % file['_id'],
        user=admin)
    assert len(resp.json['names']) == 10

    resp = server.request(
        path='/file/%s/archive/download' % file['_id'],
        params={'path': '002.dcm'},
        user=admin, isJson=False)
    datalen = 0
    for chunk in resp.body:
        if not isinstance(chunk, six.binary_type):
            chunk = chunk.encode('utf8')
        datalen += len(chunk)
    assert datalen == 527192
