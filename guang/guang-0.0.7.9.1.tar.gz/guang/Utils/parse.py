import argparse
def main():
    parser = argparse.ArgumentParser()
    parser.description = 'give me two number, out you one number!'
    parser.add_argument('-a',help='number 1', type=int)
    parser.add_argument('-b',help='number 2', type=int)
    args = parser.parse_args()
    a = args.a
    b = args.b
    print(f'emmm, I give you this:{(a+b)/2}')

if __name__ == '__main__':
    main()
