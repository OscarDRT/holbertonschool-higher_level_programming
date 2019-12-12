#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    leng = len(argv)
    if leng == 1:
        print("0 arguments.")
    elif leng == 2:
        print("{}: argument:".format(leng - 1))
        print("{:d}: {:s}".format(1, argv[1]))
    else:
        print("{}: argumentes:".format(leng - 1))
        for i in range(1, leng):
            print("{:d}: {:s}".format(i, argv[i]))
