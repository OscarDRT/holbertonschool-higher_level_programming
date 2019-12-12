#!/usr/bin/python3
import sys
if __name__ == '__main__':
    leng = len(sys.argv)
    if leng == 1:
        print("0 arguments.")
    elif leng == 2:
        print("{:d} argument:".format(1))
        print("{:d}: {:s}".format(1,sys.argv[1]))
    else:
        print("{} argumentes:".format(leng - 1))
        for i in range(1, leng):
            print("{:d}: {:s}".format(i, sys.argv[i]))
