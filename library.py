def print_help(PROGRAM_NAME):
    print("Usage: {} [OPTION]... [NUMBER]".format(PROGRAM_NAME))
    print("-h   display this help and exit")
    print("-v   output version information and exit")
    exit()

def print_version(PROGRAM_NAME, VERSION):
    print("{} version {}".format(PROGRAM_NAME, VERSION))
    exit()

def print_numbers(count, reverse_order):
    start = 0
    end = count
    delta = 1

    if reverse_order:
        start = count - 1
        end = -1
        delta = -1

    while start != end:
        print(start)
        start = start + delta 