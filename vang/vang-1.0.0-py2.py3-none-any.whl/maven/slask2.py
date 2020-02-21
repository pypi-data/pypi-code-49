from pprint import pprint

x = [(f'{m} * {n}', m * n) for m in range(1, 13) for n in range(1, 13)]
pprint(x)

x = [f'{str(m).rjust(2)} * {str(n).rjust(2)} = {str(m * n).rjust(3)}' for m in range(1, 13) for n in range(1, 13)]
pprint(x)


def do_it():
    for m in range(1, 13):
        print(m, end=' ')


do_it()
