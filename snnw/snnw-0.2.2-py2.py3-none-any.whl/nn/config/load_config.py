def load_config(config_path):
    with open(config_path, 'r') as f:
        # each layer config is separated by an empty new line
        layers = f.read().split('\n\n')
    layer_configs = []
    for layer in layers:
        layer_config = {}
        layer = layer.splitlines()
        assert (len(layer) == 5), "check that your config format matches the examples given"
        for line in layer:
            in_size = 'in_size='
            out_size = 'out_size='
            activation = 'activation='
            if line[0] == '#':
                continue
            elif line[0] == '[' and line[-1] == ']':
                layer_config['layer_type'] = line[1:-1]
            elif line[:len(in_size)] == in_size:
                layer_config['in_size'] = int(line[len(in_size):])
            elif line[:len(out_size)] == out_size:
                layer_config['out_size'] = int(line[len(out_size):])
            elif line[:len(activation)] == activation:
                layer_config['activation'] = line[len(activation):]
        layer_configs.append(layer_config)
    return layer_configs
