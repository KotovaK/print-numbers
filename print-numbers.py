import sys
# 't' means test, t-0.1 test version 0.1

VERSION = "t-0.3"
# sys.argv - list of arguments, example ['print-numbers.py', 'arg1', 'arg2', ...]
# sys.argv[0] - is the name of the python file
PROGRAM_NAME = sys.argv[0]

def print_help(PROGRAM_NAME):
    print("Usage: {} [OPTION]... [NUMBER]".format(PROGRAM_NAME))
    print("-h   display this help and exit")
    print("-v   output version information and exit")
    exit()

def print_version(PROGRAM_NAME, VERSION):
    print("{} version {}".format(PROGRAM_NAME, VERSION))
    exit()

def print_numbers(count):
    for i in range(count):
        print(i)

if "-h" in sys.argv:
    print_help(PROGRAM_NAME)

if "-v" in sys.argv:
    print_version(PROGRAM_NAME, VERSION)

# sys.argv[1] is string type, we need to convert to integer type using int() function
print_numbers(int(sys.argv[1]))