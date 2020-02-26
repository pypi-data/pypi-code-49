import gnupg
try:
    import oqs
except:
    pass
from Crypto.Cipher import AES
from Crypto import Random
from pkcs7 import PKCS7Encoder
import zml


def generate_keypair():

    with oqs.KeyEncapsulation(kemalg) as client:
        with oqs.KeyEncapsulation(kemalg) as server:
            print("\nStarting key encapsulation")
            pprint(client.details)

            # client generates its keypair
            public_key = client.generate_keypair()
            # optionally, the secret key can be obtained by calling export_secret_key()
            # and the client can later be reinstantiated with the key pair:
            # secret_key = client.export_secret_key()
            # store key pair, wait... (session resumption):
            # client = oqs.OQS_KEM(kemalg, secret_key)

            # the server encapsulates its secret using the client's public key
            ciphertext, shared_secret_server = server.encap_secret(public_key)

            # the client decapsulates the the server's ciphertext to obtain the shared secret
        # shared_secret_client = client.decap_secret(ciphertext)


def generate_secret_key_aes():
    rndfile = Random.new()
    key = rndfile.read(32)
    return key


def store_secret_key():
    pass


def load_secret_key(keys_directory, key_file):
    gpg = gnupg.GPG(gnupghome=keys_directory)
    document = zml.import_file(key_file)
    encrypted_key = document.local_context['ciphertext']
    decryption = gpg.decrypt(encrypted_key)
    if decryption.status == 'decryption ok':
        decrypted_key = decryption.data
    else:
        raise Exception('Decryption failure')
    return decrypted_key

# gpg = gnupg.GPG(gnupghome=keys_directory, verbose=True)
# gpg.encoding = 'utf-8'
# input_data = gpg.gen_key_input(
#     name_email='testgpguser@mydomain.com',
#     passphrase=pass_phrase)


def create_secret_key_file(keys_directory, key_file):
    key = generate_secret_key_aes()
    gpg = gnupg.GPG(gnupghome=keys_directory)
    encrypted_key = gpg.encrypt(key, None, symmetric=True)
    code = "&cipher: 'AES-256'\n#ciphertext: '\n{}'".format(encrypted_key)
    with open(key_file, 'w', encoding='utf-8') as f:
        f.write(code)


def encrypt(code, key):
    cipher = encrypt_message(code, key)
    return cipher


def decrypt(cipher, key):
    iv = 'skeurTFGHU384756'
    obj2 = AES.new(key, AES.MODE_CBC, iv)
    decoded_message = obj2.decrypt(cipher).decode('utf-8')
    return decoded_message


def encrypt_message(message, key):
    print(key)
    # key = self.generate_secret_key_aes()
    iv = 'skeurTFGHU384756'
    obj = AES.new(key, AES.MODE_CBC, iv)
    encoder = PKCS7Encoder()
    pad_message = encoder.encode(message)
    cipher = obj.encrypt(pad_message)
    return cipher
