from apcs import Config

def main():
    parser, cfg = Config.auto_argparser()
    args = parser.parse_args()
    cfg.merge_from_args(args, lazy=True)
    
    print(cfg)

if __name__ == '__main__':
    main()