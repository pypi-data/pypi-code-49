import fire
from pycalci.calculator import Calculator

def main():
    calculator = Calculator()
    fire.Fire(Calculator)


if __name__ == '__main__':
    main()
