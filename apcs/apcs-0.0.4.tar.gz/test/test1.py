from apcs import Config

def main():
    cfg = Config.fromfile('test/config.py')
    print(cfg.root)
    print(cfg.gpus)

if __name__ == '__main__':
    main()