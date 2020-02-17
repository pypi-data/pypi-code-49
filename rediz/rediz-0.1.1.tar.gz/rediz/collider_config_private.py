

SYMBOLS = ["SQ","DVN", "FCX", "COP", "PE"]
KEY     = "ETYWSB3ZKFB2L3KX"
REDIZ_COLLIDER_CONFIG = {"template_url":"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=SYMBOL&apikey="+KEY,
                   "symbols":list(map(lambda s:s.lower(), sorted(SYMBOLS))),
                   "write_key":"collider-write-key-2e07a2a0-667b-4d38-a485-1be11bdef047",
                   "names":[ s+'.json' for s in SYMBOLS],
                   "password":"jebBj8iyfcGQt7iaPcXEtSPyMZSV6NFB",
                   "host":"redis-15521.c6721.us-east-1-mz.ec2.cloud.rlrcp.com",
                   "port":"15521",
                   "delays":[70],
                   "delay_grace":5,
                   "num_predictions":300,
                   "max_ttl":5*60,
                   "obscurity":"0e4d-obscurity-collider-e07adadsfasf893c"
                }


# https://www.guggenheiminvestments.com/mutual-funds/resources/interactive-tools/asset-class-correlation-map