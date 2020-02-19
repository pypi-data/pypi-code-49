

SYMBOLS = ["SQ","DVN", "FCX", "COP", "PE"]
KEY     = "R543BDZKBF2LFSZX"
REDIZ_COLLIDER_CONFIG = {"template_url":"DEFAULT"+KEY,
                   "symbols":list(map(lambda s:s.lower(), sorted(SYMBOLS))),
                   "write_key":"collider-write-key-2e07a2a0-667b-4d38-a485-1be11bdef047",
                   "names":[ s+'.json' for s in SYMBOLS],
                   "password":"jegkHljhfhlkjadfslkjPjXEtSPyMZSV6NFB",
                   "host":"redis-12312.c2122.us-east-1-mz.ec2.cloud.rlrcp.com",
                   "port":"21133",
                   "delays":[70],
                   "delay_grace":5,
                   "num_predictions":300,
                   "max_ttl":5*60,
                   "obscurity":"0e4d-obscurity-collider-oiu6oi5786requy24"
                }


# https://www.guggenheiminvestments.com/mutual-funds/resources/interactive-tools/asset-class-correlation-map
