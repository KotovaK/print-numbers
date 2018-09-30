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