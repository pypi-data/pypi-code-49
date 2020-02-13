"""
Tools for working with zip files in memory
"""
import zipfile as zip_module
import io


def zip_in_memory(files):
    """Zip files in memory and return zip archive as a string.
    Files should be given as tuples of `(file_path, file_contents)`.

    Args:
        files:

    Returns:
        str:
    """
    zip_stream = io.BytesIO()
    with zip_module.ZipFile(
            zip_stream,
            mode='w',
            compression=zip_module.ZIP_DEFLATED
    ) as zip_file:
        assert isinstance(zip_file, zip_module.ZipFile)
        for file_name, file_data in files:
            zip_file.writestr(file_name, file_data)

    return zip_stream.getvalue()


def unzip_in_memory(zip_archive):
    """Unzip a zip archive given as string, returning files
    Files are returned as tuples of `(file_path, file_contents)` .

    Args:
        zip_archive (str):

    Returns:
    """
    zip_stream = io.BytesIO(zip_archive)
    with zip_module.ZipFile(
            zip_stream,
            mode='r',
            compression=zip_module.ZIP_DEFLATED
    ) as zip_file:
        assert isinstance(zip_file, zip_module.ZipFile)
        return tuple((file_name, zip_file.read(file_name)) for file_name in
                     zip_file.namelist())
