from ConfigEnv import Config
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
import boto3
import re
from urllib.request import urlopen


class Splitter():
    """docstring for Splitter."""

    def __init__(self, configFile = None):
        self._config = Config(configFile)
        self._cachePage = {}
        self._cachePdf = {}
        self._s3 = boto3.resource(
            's3',
            'eu-west-1',
            aws_access_key_id=self._config.get("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=self._config.get("AWS_SECRET_ACCESS_KEY"),
            aws_session_token= self._config.get("AWS_SESSION_TOKEN")
        )
        self._bucket = self._s3.Bucket(self._config.get("S3_BUCKET"))


    def split(self,splitInput):
        for output in splitInput["output"]:
            self._splitOnePdf(splitInput["input"], output)

    def _downloadAndCache(self,fileKey):

        if re.search("^https?://", fileKey) :
            filedata = urlopen(fileKey)
            dataStream = filedata.read()

        else:
            s3Object = self._s3.Object(self._config.get("S3_BUCKET"),fileKey)
            dataStream = s3Object.get()["Body"].read()

        self._cachePdf[fileKey] = io.BytesIO(dataStream)


    def _cachePdfOneFile(self,fileKey):
        self._downloadAndCache(fileKey)

        pdfBuffer = self._cachePdf[fileKey]
        self._cachePage[fileKey] = []
        cachePage = self._cachePage[fileKey]

        infileReader = PdfFileReader(pdfBuffer)

        for i in range(infileReader.getNumPages()):
            page = infileReader.getPage(i)
            cachePage.append(page)

    def _getOnePage(self,fileKey,page):
        if fileKey not in self._cachePage:
            self._cachePdfOneFile(fileKey)
        return self._cachePage[fileKey][page]

    def _uploadToS3(self,writer,key):
        outputWriteStream = io.BytesIO()
        writer.write(outputWriteStream)
        outputWriteStream.seek(0)
        self._bucket.upload_fileobj(outputWriteStream, key)

    def _splitOnePdf(self,inputFiles, output):
        writer = PdfFileWriter()
        for page in output["pages"]:
            # récuprération de la clef de la page
            key = inputFiles[page["index"]]
            for pageNumber in page["pages"]:
                #Ajout de la page
                writer.addPage(self._getOnePage(key,pageNumber))
        self._uploadToS3(writer,output["s3Key"])
