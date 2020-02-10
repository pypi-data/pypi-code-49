from examples.level import main as level


def test(function, function_name: str):
    try:
        function()
        print('test {} function PASS'.format(function_name))
    except Exception as exc:
        print(exc)
        print('{} FUNCTION TEST FAILED'.format(function_name.upper()))


def main():

    test(level, 'level')


if __name__ == '__main__':
    main()
