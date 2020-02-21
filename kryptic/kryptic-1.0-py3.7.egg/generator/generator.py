import secrets
import string

class Generator(object):
    """ 
    Creates a Generator class that utilizes some RNG source to 
    generate a Pseudo Random Output
    """
    def __init__(self, source='CryptGenRandom', minlength=6, maxlength=6):
        self.source=source
        self.minlength=max(minlength,1) # only positive numbers allowed
        self.maxlength=max(self.minlength,maxlength) # max cannot be below min

    def generate(self, minlength=0, maxlength=0, *flags) -> str:
        """
        Generates string with specified parameters (default=all alphanumerics and symbols)
        Flags:
            - c or char:
                generate string using only alphabetic characters
            - a or alphanum:
                generate  string using only alphanumeric characters
            - n or num:
                generate password using only numeric characters
        """
        # select universe
        src=string.printable[:95] # default; chars 95+ are escaped characters
        if 'char' in flags or 'c' in flags:
            src=string.ascii_letters
        elif 'alphanum' in flags or 'a' in flags:
            src=string.printable[:62] # chars 62+ are symbols & escaped
        elif 'num' in flags or 'n' in flags:
            src=string.digits
        r=len(src) # reduce recomputation
        if minlength < 1:
            minlength=self.minlength
        if maxlength < 1:
            maxlength=self.maxlength
        output=''

        # random length between min length and max length
        for __ in range(self.getRandomLength(minlength, maxlength)):
            num=secrets.SystemRandom(self.source)._randbelow(r)
            output += src[num] # append each new random character
        return output

    def generatePassword(self, minlength=0, maxlength=0, *flags) -> str:
        """
        Generates password string with specified parameters (default=all alphanumerics and symbols)
        Flags:
            - c or char:
                generate string using only alphabetic characters
            - a or alphanum:
                generate  string using only alphanumeric characters
            - n or num:
                generate password using only numeric characters
        """
        return self.generate(minlength, maxlength, flags)

    def generateUsername(self, minlength=0, maxlength=0) -> str:
        """
        Generates an alphanumeric string
        """
        return self.generate(minlength, maxlength, 'a')

    def getRandomLength(self, minlength=0, maxlength=0) -> int:
        """
        Generates a random number between length minlength and maxlength
        """
        if minlength < 1:
            minlength=self.minlength
        if maxlength < 1:
            maxlength=self.maxlength
            
        if minlength==maxlength:
            return minlength
        else:
            return secrets.SystemRandom(self.source)\
                ._randbelow(maxlength-minlength) + minlength
