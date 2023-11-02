#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    co = len(sys.argv)
    if co == 1:
        print("{} arguments.".format(co - 1))
    elif co == 2:
        print("{} arguments:".format(co - 1))
    else:
        print("{} arguments:".format(co - 1))
    for i in range(1, co):
        print("{}: {}".format(i, sys.argv[i]))
