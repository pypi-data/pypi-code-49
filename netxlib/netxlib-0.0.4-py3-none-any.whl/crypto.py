import hashlib
import base64
import binascii
import git
import json
import os
import subprocess
import sys
import time

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

from pathlib import Path

# create MD5 checksum for file
def md5Checksum(filePath):
    with open(filePath, 'rb') as fh:
        m = hashlib.md5()
        while True:
            data = fh.read(8192)
            if not data:
                break
            m.update(data)
        return m.hexdigest()

# retrieve credentials from vault file
def unlock(encrypted_credential, calling_user):
    secretkey = "if you're seeing this, something went wrong!"
    plaintext_credential = "if you're seeing this, something went wrong!"
    credvault = "/home/%s/.vault/%s.vault" % (calling_user, calling_user)
    saltfile = "/app/netops/vault/admin/salt"
    keygencmd = ['/app/netops/bin/keygen']

    try:
        if Path(saltfile).is_file():
            with open(saltfile, 'r') as saltstr:
                salt = bytes(saltstr.read().rstrip(), 'utf-8')

        keygenproc = subprocess.Popen(keygencmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
        keygenoutput, keygenerror = keygenproc.communicate()

        if keygenerror:
            raise
        else:
            secretkey, keygenversion, keygenuser, keygenlocaluser = keygenoutput.decode('ascii').rstrip().split(",")

        kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),length=32,salt=salt,iterations=100000,backend=default_backend())
        key = base64.urlsafe_b64encode(kdf.derive(bytes(secretkey, 'UTF-8')))
        f = Fernet(key)

        if Path(credvault).is_file():
            with open(credvault, 'rb') as cipherfile:
                ciphertext = cipherfile.read()
                plaintext = f.decrypt(ciphertext).decode('utf-8')
                creds = json.loads(plaintext)
                if encrypted_credential in creds:
                    plaintext_credential = creds[encrypted_credential]
                else:
                    raise KeyError

    except KeyError:
        print ("KeyError > this credential could not be located!")

    except OSError as e:
        print ("OSError > ",e.errno)
        print ("OSError > ",e.strerror)
        print ("OSError > ",e.filename)

    except:
        print ("Error > ",sys.exc_info()[0])

    finally:
        return plaintext_credential

def hash_password(password):
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')

def verify_password(stored_password, provided_password):
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512', provided_password.encode('utf-8'), salt.encode('ascii'), 100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password

