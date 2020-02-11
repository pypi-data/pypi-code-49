# Begin 'get'

config_1 = """# 0
[fully_connected]
in_size=784
out_size=1000
activation=relu

# 1
[fully_connected]
in_size=1000
out_size=1000
activation=relu

# 2
[fully_connected]
in_size=1000
out_size=10
activation=softmax
"""

config_2 = """# 0
[fully_connected]
in_size=784
out_size=1000
activation=tanh

# 1
[fully_connected]
in_size=1000
out_size=1000
activation=tanh

# 2
[fully_connected]
in_size=1000
out_size=10
activation=softmax
"""


def get(config_path, num):
    assert (num in [1, 2]), "Your config number is not in range."
    config = ""
    if num == 1:
        config = config_1
    elif num == 2:
        config = config_2
    with open(config_path, 'w') as f:
        f.write(config)


# Begin 'load'


def load(config_path):
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
