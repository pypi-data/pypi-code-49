from os import path
import sys


def run_tests(filelist):
    for f in filelist:
        print("Running " + f)
        cmd = ["python", f]
        framework.utils.run_command(cmd)
        print("Done")


if __name__ == '__main__':
    curdir = path.dirname(path.abspath(__file__))
    sys.path.append(path.join(curdir, "../../../tests"))

    import framework.utils

    filelist = framework.utils.get_test_files(curdir)
    filelist += framework.utils.get_test_files(path.join(curdir, "e2e_tests"))
    filelist += framework.utils.get_test_files(path.join(curdir, "unittests"))

    if len(sys.argv) > 1:
        # unit-test only build definition will pass this arg
        if sys.argv[1].lower() == 'unit-tests-only':
            print('Flag unit-tests-only is provided in the commandline. Limiting to unit tests')
            # uses file name convention to pick unit tests
            filelist = list(filter(lambda file: 'unittests' in file, filelist))
        # e2e-test only build definition will pass this arg
        elif sys.argv[1].lower() == 'e2e-tests-only':
            print('Flag e2e-tests-only is provided in the commandline. Limiting to e2e tests')
            # uses file name convention to filter out e2e tests
            filelist = list(filter(lambda file: 'e2e_tests' in file, filelist))
        elif sys.argv[1].lower() == 'compute-creation-tests-only':
            print('''Flag compute-creation-tests-only is provided in the commandline.
                     Limiting to compute creation tests''')
            # uses file name convention to filter out compute creation tests
            filelist = list(filter(lambda file: 'compute_creation_tests' in file, filelist))
    run_tests(filelist)
