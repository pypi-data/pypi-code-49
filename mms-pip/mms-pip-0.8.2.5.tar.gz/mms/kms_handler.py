from google.cloud import kms_v1

def decrypt_symmetric(project_id, location_id, key_ring_id, crypto_key_id,
                      ciphertext):
    """Decrypts input ciphertext using the provided symmetric CryptoKey."""

    #from google.cloud import kms_v1

    # Creates an API client for the KMS API.
    client = kms_v1.KeyManagementServiceClient()

    # The resource name of the CryptoKey.
    name = client.crypto_key_path_path(project_id, location_id, key_ring_id,
                                       crypto_key_id)
    # Use the KMS API to decrypt the data.
    response = client.decrypt(name, ciphertext)
    return response.plaintext



def encrypt_symmetric(project_id, location_id, key_ring_id, crypto_key_id,
                      plaintext):
    """Encrypts input plaintext data using the provided symmetric CryptoKey."""

    from google.cloud import kms_v1

    # Creates an API client for the KMS API.
    client = kms_v1.KeyManagementServiceClient()

    # The resource name of the CryptoKey.
    name = client.crypto_key_path_path(project_id, location_id, key_ring_id,
                                       crypto_key_id)

    # Use the KMS API to encrypt the data.
    response = client.encrypt(name, plaintext)
    return response.ciphertext


class KmsService:

    def __init__(self):
        self.client = kms_v1.KeyManagementServiceClient()

    def decrypt_response(self, project_id, location_id, key_ring_id, crypto_key_id, ciphertext):

        name = self.client.crypto_key_path_path(project=project_id,
                                                location=location_id,
                                                key_ring=key_ring_id,
                                                crypto_key_path=crypto_key_id)

        return self.client.decrypt(name, ciphertext)

    def encrypt_plaintext(self, project_id, location_id, key_ring_id, crypto_key_id, plaintext):

        name = self.client.crypto_key_path_path(project=project_id,
                                                location=location_id,
                                                key_ring=key_ring_id,
                                                crypto_key_path=crypto_key_id)

        return self.client.encrypt(name, plaintext)

    @classmethod
    def init(cls):
        return KmsService()

    @classmethod
    def decrypt(cls, project_id, location_id, key_ring_id, crypto_key_id, ciphertext):

        kms = KmsService.init()
        response = kms.decrypt_response(project_id=project_id,
                                        location_id=location_id,
                                        key_ring_id=key_ring_id,
                                        crypto_key_id=crypto_key_id,
                                        ciphertext=ciphertext)

        return response.plaintext

    @classmethod
    def encrypt(cls, project_id, location_id, key_ring_id, crypto_key_id, plaintext):

        kms = KmsService.init()
        response = kms.encrypt_plaintext(project_id=project_id,
                               location_id=location_id,
                               key_ring_id=key_ring_id,
                               crypto_key_id=crypto_key_id,
                               plaintext=plaintext)

        return response.ciphertext

