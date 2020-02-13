"""
This class takes in a row and then splits it into component parts. It then parses them as the required data and returns
the data in a usable form.
"""

class BlastRow(dict):

    def __init__(self, line: str):
        """
        This class takes in a line in the BLAST row format and parses it into the components.
        :param line: str, The line to parse.
        """
        items = line.split()
        items = [i.strip() for i in items if i]
        self.query_id = items[0]
        self.subject_id = items[1]
        self.percent_identity = float(items[2])
        self.alignment_length = int(items[3])
        self.mismatches = int(items[4])
        self.gap_openings = int(items[5])
        self.q_start = int(items[6])
        self.q_end = int(items[7])
        self.s_start = int(items[8])
        self.s_end = int(items[9])
        self.mate = int(self.subject_id.split("/")[1])
        dict.__init__(
            self,
            query_id = self.query_id,
            subject_id = self.subject_id,
            percent_identity = self.percent_identity,
            alignment_length = self.alignment_length,
            mismatches = self.mismatches,
            gap_openings = self.gap_openings,
            q_start = self.q_start,
            q_end = self.q_end,
            s_start = self.s_start,
            s_end = self.s_end
        )

    def __repr__(self):
        return repr((self.query_id, self.q_start, self.q_end))