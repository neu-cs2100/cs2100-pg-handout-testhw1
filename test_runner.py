'''
This script is used to run unit tests in specified test files provided as command line args.
'''
import unittest
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Test runner")

    parser.add_argument("-t",
                        "--tests", 
                        nargs="+",
                        required=False,
                        type=str,
                        default=[],
                        help="Test file names/patterns")

    args = parser.parse_args()
    tests = args.tests


    if tests != []:
        print("\n\nRunning the following test file(s): ")
        for test in tests:
            print (f"   -tests/{test}")
        print("\n")
        for test in tests:
            print(f"Test results for tests/{test}\n")
            suite = unittest.defaultTestLoader.discover(start_dir='tests', pattern=test)

            unittest.TextTestRunner(
                verbosity=2
            ).run(suite)
    else:
        print("\n\033[1m    1)Running interface tests: make sure these test file " \
        "names start with `test_`, or they won't run\033[0m\n")
        interface_suite = unittest.defaultTestLoader.discover(start_dir='tests',
                                                              pattern='test_*.py')

        unittest.TextTestRunner(
            verbosity=2
        ).run(interface_suite)


        print("\n\033[1m    2)Running implementation tests: make sure these test " \
        "file names start with `impl_`, or they won't run\033[0m\n")
        impl_suite = unittest.defaultTestLoader.discover(start_dir='tests', pattern='impl_*.py')

        unittest.TextTestRunner(
            verbosity=2
        ).run(impl_suite)
