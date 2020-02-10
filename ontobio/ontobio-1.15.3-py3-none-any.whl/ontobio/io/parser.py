import requests
import tempfile
import logging
import io
import gzip

class Id


def _pair_to_id(db, localid, config):
    """
    Config is assocparser.AssocParserConfig
    """
    if config.remove_double_prefixes:
        ## Switch MGI:MGI:n to MGI:n
        if localid.startswith(db+":"):
            localid = localid.replace(db+":", "")
    return db + ":" + localid

def _ensure_file(file):
    logging.info("Ensure file: {}".format(file))
    if isinstance(file, str):
        # TODO Let's fix this if/elseif chain.
        if file.startswith("ftp"):
            f = tempfile.NamedTemporaryFile()
            fn = f.name
            cmd = ['wget',file,'-O',fn]
            subprocess.run(cmd, check=True)
            return open(fn,"r")
        elif file.startswith("http"):
            url = file
            with closing(requests.get(url, stream=False)) as resp:
                logging.info("URL: {} STATUS: {} ".format(url, resp.status_code))
                ok = resp.status_code == 200
                if ok:
                    logging.debug("HEADER: {}".format(resp.headers))
                    if file.endswith(".gz"):
                        return io.StringIO(str(gzip.decompress(resp.content),'utf-8'))
                    else:
                        out = io.StringIO(resp.content)
                        return out
                else:
                    return None
        else:
            logging.info("Testing suffix of {}".format(file))
            if file.endswith(".gz"):
                return gzip.open(file, "rt")
            else:
                return open(file, "r")
    else:
        return file
