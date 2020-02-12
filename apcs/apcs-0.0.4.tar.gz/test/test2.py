from apcs import Config

def main():
    parser, cfg = Config.auto_argparser()
    args = parser.parse_args()
    cfg.merge_from_args(args)
    
    print(cfg.gpus)
    print(cfg.model_kwargs)
    print(cfg.root)
    print(cfg.imagelist)

    cfg.merge_from_args(args, lazy=True)
    
    print(cfg.gpus)
    print(cfg.model_kwargs)
    print(cfg.root)
    print(cfg.imagelist)

if __name__ == '__main__':
    main()