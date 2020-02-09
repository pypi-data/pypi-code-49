from telegram_bot_sdk.telegram_objects.passportFile import PassportFile


class EncryptedPassportElement:
    """This class contains information about documents or other Telegram Passport elements shared with the bot by\
    the user

    :param type_result: Element type. One of “personal_details”, “passport”, “driver_license”, “identity_card”,\
    “internal_passport”, “address”, “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”,\
    “temporary_registration”, “phone_number”, “email”
    :type type_result: str
    :param data: Optional: Base64-encoded encrypted Telegram Passport element data provided by the user, available for\
    “personal_details”, “passport”, “driver_license”, “identity_card”, “internal_passport” and “address” types
    :type data: str
    :param hash_data: Base64-encoded element hash for using in :ref:`object_passport_element_error_unspecified`
    :type hash_data: str
    :param phone_number: Optional: User's verified phone number, available only for “phone_number” type
    :type phone_number: str
    :param email: Optional: User's verified email address, available only for “email” type
    :type email: str
    :param files: Optional: Array of encrypted files with documents provided by the user, available for “utility_bill”,\
    “bank_statement”, “rental_agreement”, “passport_registration” and “temporary_registration” types. Files can be\
    decrypted and verified using the accompanying :ref:`object_encrypted_credentials`
    :type files: list of :ref:`object_passport_file`
    :param front_side: Optional: Encrypted file with the front side of the document, provided by the user. Available\
    for “passport”, “driver_license”, “identity_card” and “internal_passport”. The file can be decrypted and verified\
    using the accompanying :ref:`object_encrypted_credentials`.
    :type front_side: :ref:`object_passport_file`
    :param reverse_side: Optional: Encrypted file with the reverse side of the document, provided by the user. \
    Available or “driver_license” and “identity_card”. The file can be decrypted and verified using the accompanying \
    :ref:`object_encrypted_credentials`
    :type reverse_side: :ref:`object_passport_file`
    :param selfie: Optional: Encrypted file with the selfie of the user holding a document, provided by the user;\
    available for “passport”, “driver_license”, “identity_card” and “internal_passport”. The file can be decrypted and \
    verified using the accompanying :ref:`object_encrypted_credentials`
    :type selfie: :ref:`object_passport_file`
    :param translation: Optional: Array of encrypted files with translated versions of documents provided by the user. \
    Available if requested for “passport”, “driver_license”, “identity_card”, “internal_passport”, “utility_bill”, \
    “bank_statement”, “rental_agreement”, “passport_registration” and “temporary_registration” types. Files can be \
    decrypted and verified using the accompanying :ref:`object_encrypted_credentials`
    :type translation: list of :ref:`object_passport_file`
    """
    def __init__(self, *, type_result, data=None, hash_data, phone_number=None, email=None, files=None, front_side=None,
                 reverse_side=None, selfie=None, translation=None):
        self.type_result = type_result
        self.data = data
        self.hash_data = hash_data
        self.phone_number = phone_number
        self.email = email
        self.files = [PassportFile(**x) for x in files] if files else None
        self.front_side = PassportFile(**front_side) if front_side else None
        self.reverse_side = PassportFile(**reverse_side) if reverse_side else None
        self.selfie = PassportFile(**selfie) if selfie else None
        self.translation = [PassportFile(**x) for x in translation] if translation else None
