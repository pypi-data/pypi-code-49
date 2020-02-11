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


def get_config(config_path, num):
    assert (num in [1, 2]), "Your config number is not in range."
    config = ""
    if num == 1:
        config = config_1
    elif num == 2:
        config = config_2
    with open(config_path, 'w') as f:
        f.write(config)
