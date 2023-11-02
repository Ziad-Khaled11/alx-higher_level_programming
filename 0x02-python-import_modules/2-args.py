#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    argv = sys.argv[0:]
    co = len(sys.argv)
    index = 1
    if co == 1:
        print("{} arguments.".format(co - 1))
    elif co == 2:
        print("{} arguments:".format(co - 1))
    else:
        print("{} arguments:".format(co - 1))
    while co - 1 > 0:
        print("{}: {}".format(index, argv[index]))
        index += 1
        co -= 1
