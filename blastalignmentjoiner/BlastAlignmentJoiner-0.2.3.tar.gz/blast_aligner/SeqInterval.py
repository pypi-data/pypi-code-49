"""
This is a class that defines the interval of a Sequence.
"""

class SeqInterval(dict):

    def __init__(self, start = 0, end = 0, gaps = 0, mismatches = 0):
        """
        This initializes the SEQuence INTERVAL for a given sequence.
        :param start: int
        :param end: int
        :param gaps: int
        :param mismatches: int
        """

        self.start = start
        self.end = end
        self.gaps = gaps
        self.mismatches = mismatches
        self.calculate_length()
        self.percent_identity = self.calculate_percent_identity() * 100
        self.sequences = []
        dict.__init__(self,
                      start=self.start,
                      end=self.end,
                      gaps=self.gaps,
                      mismatches=self.mismatches,
                      length=self.length,
                      percent_identity=self.percent_identity,
                      sequences = self.sequences)

    def __repr__(self):
        output = f'Start: {self.start}; End: {self.end}; Length: {self.length}; % Ident: {self.percent_identity}'
        return repr((output))

    def calculate_length(self):
        """
        This function calculates the length of a sequence. This is done by subtracting the start from the end.
        :return: int, the length of the sequence
        """
        self.length = self.end - self.start

    def calculate_percent_identity(self):
        """
        This function calculates the amount of sequece that is identical tot he subject. This is done by subtracting
        the mismatches and gaps from the length, and then dividing by length.
        :return: float, The percentage of the sequence that is identical.
        """
        identical = self.length - self.mismatches - self.gaps
        try:
            return round(identical/self.length, 2)
        except ZeroDivisionError:
            return 0