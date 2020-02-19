from sys import argv, exit
from dom_query import lexer, parse
from pathlib import Path
import logging

logging.basicConfig(format='%(levelname)s: %(message)s',
                    level=logging.INFO)

if __name__ == "__main__":
    if len(argv) < 2:
        print(f"Usage: PYTHONPATH= python {argv[0]} [TESTFILE] ...")
        print(f"  PYTHONPATH should be the project root directory")
        exit(1)

    for test_src in map(Path, argv[1:]):
        if not test_src.exists():
            logging.error(f"File not found: '{test_src}'")
            continue

        if test_src.suffix == ".test-gen":
            #  Silently skip .test-gen files
            continue

        test_type = test_src.suffixes[-2]
        if test_type not in (".lexer", ".parser", ):
            logging.error(f"File name not valid: '{test_src}'")
            continue

        test_gen = test_src.with_suffix(".test-gen")

        src = test_src.open()
        gen = test_gen.open("w")

        logging.info(f"Generating test-gen for {test_src}")

        for line in src.read().splitlines():
            if len(line) == 0:
                continue

            try:
                result = None
                if test_type == ".lexer":
                    tokens = tuple(lexer(line))
                    result = repr(tokens)
                elif test_type == ".parser":
                    ast = parse(lexer(line))
                    result = repr(ast)
            except SyntaxError as e:
                result = repr(e)

            gen.write(f"{line}\n")
            gen.write(f"{result}\n")

        src.close()
        gen.close()
