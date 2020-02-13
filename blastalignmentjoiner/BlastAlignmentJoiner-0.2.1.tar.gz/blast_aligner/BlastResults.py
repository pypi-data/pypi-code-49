"""
This class encapsulates the general functionality of the application.
This takes in a file formatted as a BLAST9 file (with comments) and then turns it into a dictionary of results.
"""

from os.path import basename
from blast_aligner.SeqInterval import SeqInterval
from blast_aligner.BlastRow import BlastRow


class BlastResults:

    def __init__(self, datafile: str):
        """
        This class takes in a data file name and then processes it. As this is used to align multiple query sequences
        to the same subject sequence, and we want to find the results for all the data, we use a split technique to identify all the different
        query sequences.
        :param datafile: str, a single paramter which is the name of the file you want to process.
        """

        try:
            with open(datafile, 'r') as tsv:
                counter = -1
                data = [[]]
                for line in tsv:
                    if line.startswith("# Fields"):
                        counter += 1
                        data.append([])
                    elif line.startswith("#"):
                        continue
                    else:
                        data[counter].append(line)
                self.data = [d for d in data if d]
                self.sample = basename(datafile).split(".")[0]
                self.processed_data = self.process_data()
                self.results = self.generate_results()

        except FileNotFoundError as e:
            print("Cannot find the file.")
            print(e)

    def find_overlap_query(self, lines):
        """
        This function takes in a list of BlastRow objects and outputs a list of SeqInterval objects.
        This function sorts the lines by the q_start paramter and then iterates through the list. If it finds a start value that is larger
        than our current stop value, it creates a new SeqInterval object and continues from there. If the current start value is lesser than our end value
        it compares the end values for both and keeps the larger one.

        The sorting beforehand guarantees that the start value will always be larger as we iterate through the list.
        :param lines: List[BlastRow], a list of BlastRow objects
        :return: List[SeqInterval], a list of SeqInterval objects which has the longest contiguous segments.
        """
        sorted_rows = sorted(lines, key=lambda x: x.q_start)

        intervals = [SeqInterval()]

        interval_index = 0

        first = sorted_rows[0]

        intervals[interval_index] = SeqInterval(first.q_start, first.q_end, first.gap_openings, first.mismatches)
        intervals[interval_index].sequences.append(first.subject_id)

        for record in sorted_rows[1:]:
            if record.q_start > intervals[interval_index].end:
                interval_index += 1
                intervals.append(SeqInterval(record.q_start, record.q_end, record.gap_openings, record.mismatches))
                intervals[interval_index].sequences.append(record.subject_id)
            else:
                if record.q_end > intervals[interval_index].end:
                    old = intervals[interval_index]
                    old.end = record.q_end
                    old.gaps += record.gap_openings
                    old.mismatches += record.mismatches
                    old.sequences.append(record.subject_id)
                    old.calculate_length()
                elif record.q_start > intervals[interval_index].start and record.q_end < intervals[interval_index].end:
                    pass

        return intervals

    def return_overlaps(self, records):
        if records:
            overlaps = self.find_overlap_query(records)
            return overlaps
        else:
            return []

    def process_record(self, record):
        if record["identity"]:
            identity = record["identity"]
        else:
            identity = ""
        mate1 = self.return_overlaps(record["mate_1"])
        mate2 = self.return_overlaps(record["mate_2"])
        unmated = self.return_overlaps(record["mate_1"] + record["mate_2"])

        return {"identity": identity, "mate_1_intervals": mate1, "mate_2_intervals": mate2, "unmated_intervals": unmated}

    def process_data(self):
        """
        This function takes in the data read into the object and then runs the find_overlap_query on it to find the longest contiguous overlaps.
        :return: A list of dict with the values being a dictionary with the following schema:
        "identity": str, the query id,
        "mate_1": list, list of SeqInterval objects containing the longest contiguous alignments for mate_1
        "mate_2": list, list of SeqInterval objects containing the longest contiguous alignments for mate_2
        """
        output = []
        for collection in self.data:
            pioneer = BlastRow(collection[0])
            identity = pioneer.query_id
            processed = [BlastRow(x) for x in collection]
            mate1 = list(filter(lambda x: x.mate == 1, processed))
            mate2 = list(filter(lambda x: x.mate == 2, processed))
            split = {"identity": identity, "mate_1": mate1, "mate_2": mate2}
            output.append(split)

        return output

    def generate_results(self):
        res = []
        for item in self.processed_data:
            r = self.process_record(item)
            res.append(r)

        return res
