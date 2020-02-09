class EncryptedCredentials:
    """This class contains data required for decrypting and authenticating :ref:`object_encrypted_passport_element`\
    See https://core.telegram.org/passport#receiving-information for further information

    :param data: Base64 encoded encrypted JSON-serialized data with unique user's payload,d ata hashed and secrets\
    required for :ref:`object_encrypted_passport_element` decryption and authentication
    :type data: str
    :param hash_data: Base64 encoded data hash for data authentication
    :type hash_data: str
    :param secret: Base64 encoded secret, encrypted with the bot's public RSA key, required for data decryption
    :type secret: str
    """
    def __init__(self, *, data, hash_data, secret):
        self.data = data
        self.hash_data = hash_data
        self.secret = secret
