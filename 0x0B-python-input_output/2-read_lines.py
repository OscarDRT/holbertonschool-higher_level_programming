#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open(filename, encoding='utf-8') as f:
        leng = len(f.readlines())
    if nb_lines >= leng or nb_lines <= 0:
        with open(filename, encoding='utf-8') as f:
            print(f.read())
    else:
        with open(filename, encoding='utf-8') as f:
            for i in range(nb_lines):
                print(f.readline(), end="")
