def makeArchive(fileList, archive, root):
    """
    'fileList' is a list of file names - full path each name
    'archive' is the file name for the archive with a full path
    """
    a = zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED)

    for f in fileList:
        print "archiving file %s" % (f)
        a.write(f, os.path.relpath(f, root))
    a.close()
