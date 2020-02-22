import sys
import os
from tempfile import NamedTemporaryFile

from xaws.kms import EncryptedMessage

def encrypt():
    keyid = sys.argv[1]
    with open(sys.argv[2], 'rb') as f:
        msg = EncryptedMessage.new(keyid, f)
    with NamedTemporaryFile(delete=False, dir='.') as tmpfile:
        msg.to_file(tmpfile)
    os.rename(tmpfile.name, sys.argv[2])

def decrypt():
    with open(sys.argv[1], 'rb') as f:
        msg = EncryptedMessage.from_file(f)
    with NamedTemporaryFile(delete=False, dir='.') as tmpfile:
        msg.decrypt(tmpfile)
    os.rename(tmpfile.name, sys.argv[1])
