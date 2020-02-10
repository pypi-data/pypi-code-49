class CharacterMap:
    def __init__(self, alphabet: str, case_sensitive=False):
        self.map = 256 * [0]
        for i, character in enumerate(alphabet):
            if case_sensitive:
                self.map[ord(character)] = i
            else:
                self.map[ord(character.upper())] = i
                self.map[ord(character.lower())] = i
        self.alphabet = alphabet

    def translate(self, sequence: str):
        return [self.map[ord(character)] for character in sequence]
