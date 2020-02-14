from google.cloud import storage
from google.oauth2 import service_account
from abc import ABC as AbstractClass


class GeneralGSCBuilder(AbstractClass):
    def __init__(self):
        self.credentials_path = None

    def with_service_account(self, creds_path: str):
        """Recibe un string con el path donde se encuentras las credenciales deseadas y se las setea al builder"""
        self.credentials_path = creds_path
        return self

    def _validate_credentials(self):
        """ Verifica que las credenciales del builder no sean nulas"""
        if self.credentials_path is None:
            raise NoCredentialsEspecifiedException('No credentials was especificated.')

    def _validations(self):
        """Se realizan una a una las validaciones necesarias para crear un cliente"""
        self._validate_credentials()


class Error(Exception):
    pass


class NoCredentialsEspecifiedException(Error):
    pass


class NoClientEspecifiedException(Error):
    pass


class NoBucketNameEspecifiedException(Error):
    pass


class GCSClientBuilder(GeneralGSCBuilder):

    def build(self):
        """crea un nuevo cliente si las validaciones son correctas"""
        self._validations()
        credentials = service_account.Credentials.from_service_account_file(self.credentials_path)
        return storage.Client(project=credentials.project_id, credentials=credentials)


class GCSBucketBuilder(GeneralGSCBuilder):
    bucket_name = None

    def build(self):
        """Crea un bucket si las validaciones son correctas"""
        self._validations()
        client = GCSClientBuilder().with_service_account(self.credentials_path).build()
        return client.get_bucket(self.bucket_name)

    def with_bucket_name(self, _bucket_name):
        """Recibe un string con el nombre del bucket deseado y se lo setea al builder"""
        self.bucket_name = _bucket_name
        return self

    def _validate_bucket_name(self):
        """Verifica que el nombre del bucket del builder no sea nulo"""
        if self.bucket_name is None:
            raise NoBucketNameEspecifiedException('No bucket name was especificated.')

    def _validations(self):
        super()
        self._validate_bucket_name()
