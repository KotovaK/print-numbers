import sys
import library
# 't' means test, t-0.1 test version 0.1

VERSION = "2.0"
# sys.argv - list of arguments, example ['print-numbers.py', 'arg1', 'arg2', ...]
# sys.argv[0] - is the name of the python file
PROGRAM_NAME = sys.argv[0]

if "-h" in sys.argv or len(sys.argv) == 1:
    library.print_help(PROGRAM_NAME)

if "-v" in sys.argv:
    library.print_version(PROGRAM_NAME, VERSION)

# sys.argv[1] is string type, we need to convert to integer type using int() function
library.print_numbers(int(sys.argv[1]))



