# SRP006387|*Legume|C0023263|140062|ET|Entry Term Replacement for "Fabaceae";RtM via: Fabaceae;checkForceMH Boosted;Forced Non-Leaf Node Lookup:legumes|TI|MM;RC|181^6^0
# SRP006387|*High-Throughput Nucleotide Sequencing|C2936621|119455|MH|RtM via: High-Throughput Nucleotide Sequencing;RtM via: Massively-Parallel Sequencing;Forced Lookup:next generation sequencing|TI|MM;RC|1475^15^1;1492^10^1;1355^26^0;94^26^0

from pydantic import BaseModel
from typing import List

class MTIResult(BaseModel):
    identifier: str
    name: str
    main: bool=False
    concept: str
    score: int=None
    entry_type: List[str]
    explanation: List[str]
    location: List[str]
    stuff: List[str]
    occurrences: List[str]

    @staticmethod
    def parse_mti_line(line):
        def do_split(s):
            s = s.split(';')
            return s
        line = line.strip()
        line = line.split('|')
        for n in range(0,9-len(line)):
            line.append('')
        
        try:
            mti_result = MTIResult(
            identifier = line[0],
            name = line[1].strip('*'),
            main = line[1].startswith('*'),
            concept = line[2],
            score = int(line[3]),
            entry_type = do_split(line[4]),
            explanation = do_split(line[5]),
            location = do_split(line[6]),
            stuff = do_split(line[7]),
            occurrences = do_split(line[8]))
            return mti_result
        except:
            return None

    @staticmethod
    def mti_record_iterator(fname):
        with open(fname, 'r') as fhandle:
            for line in fhandle:
                res = MTIResult.parse_mti_line(line)
                if(res is not None):
                    yield res
        

def main():
    import sys
    fname = sys.argv[1]
    for rec in MTIResult.mti_record_iterator(fname):
        print(rec.json())
    
if __name__ == '__main__':
    main()
