import pydicom
import pydicom.valuerep
import pydicom.multival
import pydicom.sequence

from girder.api import access
from girder.api.rest import boundHandler
from girder.api.describe import Description, autoDescribeRoute
from girder.constants import AccessType, TokenScope
from girder.exceptions import GirderException
from girder.models.file import File
from girder.models.item import Item
from girder.utility.progress import setResponseTimeLimit

import girder_dicom_viewer
from girder_dicom_viewer import _coerceMetadata, _getDicomFileSortKey, _removeUniqueMetadata


@boundHandler()
@access.user(scope=TokenScope.DATA_READ)
@autoDescribeRoute(
    Description('Get and store common DICOM metadata, if any, for all files in the item.')
    .modelParam('id', 'The item ID',
                model='item', level=AccessType.WRITE, paramType='path')
    .errorResponse('ID was invalid.')
    .errorResponse('Read permission denied on the item.', 403)
)
def makeDicomItem(self, item):
    """
    Try to convert an existing item into a "DICOM item", which contains a
    "dicomMeta" field with DICOM metadata that is common to all DICOM files.
    """
    metadataReference = None
    dicomFiles = []

    lastFile = None
    for file in Item().childFiles(item):
        lastFile = file
        dicomMeta = _parseFile(file)
        if dicomMeta:
            dicomFiles.append(_extractFileData(file, dicomMeta))
            metadataReference = (
                dicomMeta
                if metadataReference is None else
                _removeUniqueMetadata(metadataReference, dicomMeta)
            )
        setResponseTimeLimit()

    if not dicomFiles and lastFile is not None and hasattr(File(), 'archiveList'):
        try:
            for path in File().archiveList(lastFile)['names']:
                dicomMeta = _parseFile(lastFile, path)
                if dicomMeta:
                    dicomFiles.append(_extractFileData(lastFile, dicomMeta, path))
                    metadataReference = (
                        dicomMeta
                        if metadataReference is None else
                        _removeUniqueMetadata(metadataReference, dicomMeta)
                    )
                setResponseTimeLimit()
        except GirderException:
            pass

    if dicomFiles:
        # Sort the dicom files
        dicomFiles.sort(key=_getDicomFileSortKey)
        # Store in the item
        item['dicom'] = {
            'meta': metadataReference,
            'files': dicomFiles
        }
        # Save the item
        Item().save(item)


def _extractFileData(file, dicomMetadata, archivePath=None):
    """
    Extract the useful data to be stored in the `item['dicom']['files']`.
    In this way it become simpler to sort them and store them.
    """
    result = {
        'dicom': {
            'SeriesNumber': dicomMetadata.get('SeriesNumber'),
            'InstanceNumber': dicomMetadata.get('InstanceNumber'),
            'SliceLocation': dicomMetadata.get('SliceLocation')
        },
        'name': file['name'],
        '_id': file['_id']
    }
    if archivePath:
        result['archivePath'] = archivePath
    return result


def _parseFile(f, p=None):
    try:
        # download file and try to parse dicom
        with File().open(f) if p is None else File().archiveOpen(f, p) as fp:
            dataset = pydicom.dcmread(
                fp,
                # don't read huge fields, esp. if this isn't even really dicom
                defer_size=1024,
                # don't read image data, just metadata
                stop_before_pixels=True)
            return _coerceMetadata(dataset)
    except pydicom.errors.InvalidDicomError:
        # if this error occurs, probably not a dicom file
        return None


def add_archive_access(info):
    dicomItem = girder_dicom_viewer.DicomItem()
    girder_dicom_viewer.DicomItem.makeDicomItem = makeDicomItem
    dicomItem.makeDicomItem = makeDicomItem
    info['apiRoot'].item.removeRoute('POST', (':id', 'parseDicom'))
    info['apiRoot'].item.route(
        'POST', (':id', 'parseDicom'), makeDicomItem)
    girder_dicom_viewer._extractFileData = _extractFileData
    girder_dicom_viewer._parseFile = _parseFile
