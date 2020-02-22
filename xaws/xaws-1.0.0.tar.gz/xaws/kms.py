import logging
from os import urandom
from io import BytesIO

import boto3
import M2Crypto
from pyasn1.type import univ, namedtype, tag
from pyasn1.codec.ber import encoder as ber_encoder
from pyasn1.codec.ber import decoder as ber_decoder

logger = logging.getLogger(__name__)

def new_data_key(keyid, key_length, encryption_context=None):
    kms = boto3.client('kms')
    #docs suggest using encryption_context={key: value}
    request = {
        'KeyId': keyid,
        'NumberOfBytes': key_length / 8
    }
    if encryption_context:
        request['EncryptionContext'] = encryption_context
    result = kms.generate_data_key(**request)
    return result['Plaintext'], result['CiphertextBlob']

def decrypt_data_key(blob, encryption_context=None):
    kms = boto3.client('kms')
    request = {'CiphertextBlob': blob}
    if encryption_context:
        request['EncryptionContext'] = encryption_context
    result = kms.decrypt(**request)
    return result['Plaintext']

def parse_algorithm_spec(spec):
    name, key_length, mode = spec.split('_')
    key_length = int(key_length)
    return name, key_length, mode

def _transform(cipher, buf, blocksize=4068):
    logger.debug('enter')
    while True:
        block = buf.read(blocksize)
        logging.debug('read %d bytes', len(block))
        if block:
            yield cipher.update(block)
        else:
            yield cipher.final()
            break
    logger.debug('leave')

class ASN1EncryptedMessageHeaders(univ.Set):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('algorithm', univ.OctetString().subtype(
            implicitTag=tag.Tag(
                tag.tagClassContext,
                tag.tagFormatSimple,
                1
            )
        )),
        namedtype.NamedType('blob', univ.OctetString().subtype(
            implicitTag=tag.Tag(
                tag.tagClassContext,
                tag.tagFormatSimple,
                2
            )
        )),
        namedtype.NamedType('iv', univ.OctetString().subtype(
            implicitTag=tag.Tag(
                tag.tagClassContext,
                tag.tagFormatSimple,
                3
            )
        )),
    )

class EncryptedMessage(object):
    block_length = 128

    @classmethod
    def block_length_bytes(cls):
        return cls.block_length / 8

    @classmethod
    def new(cls, keyid, plaintext_fileobj, algorithm='aes_128_cbc', encryption_context=None):
        iv = urandom(cls.block_length_bytes())
        _, key_length, _ = parse_algorithm_spec(algorithm)
        datakey, blob = new_data_key(keyid, key_length, encryption_context)
        cipher = M2Crypto.EVP.Cipher(alg=algorithm, key=datakey, iv=iv, op=M2Crypto.encrypt)

        plaintext_fileobj.seek(0)
        buf = StringIO()
        for block in _transform(cipher, plaintext_fileobj):
            buf.write(block)
        ciphertext = buf.getvalue()
        buf.close()

        return cls(algorithm, blob, iv, ciphertext)

    @classmethod
    def from_file(cls, fileobj):
        headers, ciphertext = ber_decoder.decode(fileobj.read(),
                                    asn1Spec=ASN1EncryptedMessageHeaders())
        arg_names = ('algorithm', 'blob', 'iv')
        args = [headers.getComponentByName(name).asOctets()
                for name in arg_names]
        args.append(ciphertext)
        return cls(*args)

    def __init__(self, algorithm, blob, iv, ciphertext):
        try:
            self.algorithm = algorithm.decode('ascii')
        except AttributeError:
            self.algorithm = algorithm
        self.blob = blob
        self.iv = iv
        self.ciphertext = ciphertext

    def new_decryptor(self, encryption_context):
        key = decrypt_data_key(self.blob, encryption_context=encryption_context)
        return M2Crypto.EVP.Cipher(alg=self.algorithm, op=M2Crypto.decrypt,
                                   key=key, iv=self.iv)

    def decrypt(self, fileobj, encryption_context=None):
        cipher = self.new_decryptor(encryption_context=encryption_context)
        fileobj.seek(0)
        buf = BytesIO(self.ciphertext)
        for block in _transform(cipher, buf):
            fileobj.write(block)
        buf.close()

    def to_file(self, fileobj):
        headers = ASN1EncryptedMessageHeaders()
        for name in ('algorithm', 'blob', 'iv'):
            if name == 'algorithm':
                value = getattr(self, name).encode('ascii')
            else:
                value = getattr(self, name)
            headers.setComponentByName(name, value)
        substrate = ber_encoder.encode(headers)
        fileobj.seek(0)
        fileobj.write(substrate)
        fileobj.write(self.ciphertext)

__all__ = ['EncryptedMessage']

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    import sys
    try:
       aws_kms_key_id = sys.argv[1]
    except IndexError:
       aws_kms_key_id='5067017c-73c0-4a6f-8476-94a5a606f924' #iset-devel-jmacdone

    try:
       plaintext = BytesIO(sys.argv[2])
    except IndexError:
       plaintext = BytesIO(b'foo bar baz')

    msg = EncryptedMessage.new(aws_kms_key_id, plaintext)
    ciphertext = BytesIO()
    msg.decrypt(ciphertext)
    assert plaintext.getvalue() == ciphertext.getvalue()
