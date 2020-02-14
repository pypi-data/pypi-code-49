import base64
import hashlib
import time

from Crypto import Random
from Crypto.Cipher import AES
# More about pysine https://pypi.org/project/pysine/
# More about it's installation https://github.com/lneuhaus/pysine
from pysine import sine


class Note(object):
    C = 'C'
    Db = 'Db'
    D = 'D'
    Eb = 'Eb'
    E = 'E'
    F = 'F'
    Gb = 'F#'
    G = 'G'
    Ab = 'Ab'
    A = 'A'
    Bb = 'Bb'
    B = 'B'


class Notes(object):

    __notes = [Note.C, Note.Db, Note.D, Note.Eb, Note.E, Note.F, Note.Gb, Note.G,
               Note.Ab, Note.A, Note.Bb, Note.B]

    @staticmethod
    def get(index):
        return Notes.__notes[index]

    @staticmethod
    def get_freq(note):
        freqs = {
            Note.C: 523,
            Note.Db: 554,
            Note.D: 587,
            Note.Eb: 622,
            Note.E: 659,
            Note.F: 698,
            Note.Gb: 739,
            Note.G: 783,
            Note.Ab: 830,
            Note.A: 880,
            Note.Bb: 932,
            Note.B: 987
        }
        return freqs[note]

    def __str__(self):
        notes_str = ''
        i = 0
        for note in Notes.__notes:
            notes_str += '%s - %s\n' % (i, note)
            i += 1
        return notes_str


def begin(sequence):
    for note in sequence:
        sine(Notes.get_freq(note), 0.5)
        time.sleep(0.1)
    print('\n\nVocê ouviu? Garanta que o som esteja ligado.\n'
          '%s\n'
          '%s\n'
          'Escolha a próxima nota:'
          % (sequence, Notes()))


def play(sequence):
    print(sequence)

    sine(Notes.get_freq(sequence[-1]), 0.5)

    a = '83032565277e071f2755290535ea71ea1b096ed295e6956b475653884c4a4a8e'
    b = 'A6o8L/uHYUpZgsO9qjlourzeG6FWjG9OwOGWFOOPcJsO6V9cc6l+EmKh1/ZH2kM6Qtuo1zaztw' \
        'XwX5aAzi39vpup84YW9OE2rJmGaR+jJg0buxA95yPSR5EwaYxF0oEKTx/nFAvC8UY9zUUiiadX' \
        'PPIeRKrHxFI0mDikKLbvl2xa6HymLX1WrChXacEo4U7p63nRDrv8ZobWZyisOUXL/PkmHrf8G4' \
        'eZCSeNP8P6BMGaRe6evcxIjZuzuG0KCI7oH95zUjFcMcnVj8rQtoqbvA=='

    sequence_str = ''.join(sequence)

    m = hashlib.sha3_256()
    m.update(sequence_str.encode())
    if m.digest().hex() == a:
        key = sequence_str + a
        time.sleep(1)
        for note in sequence:
            sine(Notes.get_freq(note), 0.5)
            time.sleep(0.1)

        return decrypt(key, b)
    else:
        if len(sequence) < 15:
            return ''
        elif len(sequence) > 15:
            return '\n\nOpa, quanta informação! É melhor dar um passo de cada vez.'
        else:
            return '\n\nMelodia interessante, mas não é exatamente isso que' \
                   ' estamos procurando… Tente novamente.'


def choose():
    i = int(input('Note: '))
    return Notes.get(i)


def generate_encrypted_msg(key, msg):
    """
    Only works on py<=3.7
    :param key:
    :param msg:
    :return:
    """
    key = hashlib.sha256(key.encode()).digest()
    bs = AES.block_size
    msg = msg.encode()
    raw = _pad(msg, bs)
    iv = Random.new().read(bs)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(raw))


def decrypt(key, msg):
    key = hashlib.sha256(key.encode()).digest()
    msg = base64.b64decode(msg)
    iv = msg[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return _unpad(cipher.decrypt(msg[AES.block_size:])).decode('utf-8')


def _pad(s, bs):
    return s + (bs - len(s) % bs) * chr(bs - len(s) % bs).encode()


def _unpad(s):
    return s[:-ord(s[len(s) - 1:])]
