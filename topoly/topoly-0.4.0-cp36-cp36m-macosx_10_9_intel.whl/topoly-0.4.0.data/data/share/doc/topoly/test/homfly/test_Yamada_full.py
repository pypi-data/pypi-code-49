
from topoly.topoly_preprocess import chain_read_from_string

curve = []
for k in range(3):
    arc = []
    file_name = 'data/arc' + str(k+1)
    with open(file_name, 'r') as myfile:
        for line in myfile.readlines():
            arc.append(line.strip().split()[1:])
    curve.append(arc)


# print(yamada(curve, translate=True, debug=True))

for arc in curve:
    chain_read_from_string(str(arc).encode('utf-8'))

# from topoly_homfly import find_link_code_to_string
# print(find_link_code_to_string(['structures/arc1'.encode('utf-8'), 'structures/arc2'.encode('utf-8'), 'structures/arc3'.encode('utf-8')], yamada=True))