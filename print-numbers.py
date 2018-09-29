import sys
# 't' means test, t-0.1 test version 0.1
VERSION = "t-0.1"
PROGRAM_NAME = sys.argv[0]

if "-h" in sys.argv:
    print("Usage: {} [OPTION]... [NUMBER]".format(PROGRAM_NAME))
    print("-h   display this help and exit")
    print("-v   output version information and exit")

if "-v" in sys.argv:
    print("{} version {}".format(PROGRAM_NAME, VERSION))

# count = 10
# for i in range(count):
#     print(i)