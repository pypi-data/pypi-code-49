from . import cli
from . import config
from . import server

def main():
    args = cli.args
    c = config.Config(args)
    server.start_server(c)

if __name__ == "__main__":
    main()
