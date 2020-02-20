"""
Decorate the component description to add vivado HLS pragmas
"""

from pathlib import Path

DECORATE_TAG = "//@@HINT_DECORATE@@"

def decorate_comp(filename, output_file, max_latency=None):  
    in_file = Path(filename)
    out_file = Path(output_file)
    with in_file.open("r") as f:
        with out_file.open("w") as o:
            for line in f.readlines():
                if line.strip() == DECORATE_TAG:
                    o.write(line.replace(
                        DECORATE_TAG, 
                        "#pragma HLS INLINE recursive"
                    ))
                    if max_latency is not None:
                        o.write(line.replace(
                            DECORATE_TAG, 
                            "#pragma HLS LATENCY MIN={} MAX={}".format(
                                max_latency, 
                                max_latency)
                        ))
                    o.write(line.replace(
                        DECORATE_TAG, 
                        "#pragma HLS PIPELINE"
                    ))
                else:
                    o.write(line)
                    
