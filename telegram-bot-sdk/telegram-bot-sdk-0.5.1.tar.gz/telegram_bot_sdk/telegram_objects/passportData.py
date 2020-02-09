from telegram_bot_sdk.telegram_objects.encryptedCredentials import EncryptedCredentials
from telegram_bot_sdk.telegram_objects.encryptedPassportElement import EncryptedPassportElement


class PassportData:
    """This class contains formation about Telegram Passport data shared with the bot by the user

    :param data: List with information about documents and other Telegram Passport elements that was shared with the bot
    :type data: list of :ref:`object_encrypted_passport_element`
    :param credentials: Encrypted credentials required to decrypt the data
    :type credentials: :ref:`object_encrypted_credentials`
    """
    def __init__(self, *, data, credentials):
        self.data = [EncryptedPassportElement(**x) for x in data] if data else None
        self.credentials = EncryptedCredentials(**credentials) if credentials else None
