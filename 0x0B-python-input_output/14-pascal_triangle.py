#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        my_list = [[]]
    if n == 1:
        my_list = [[1]]
    else:
        my_list = [[1], [1, 1]]
    for i in range(my_list):
        for j in range(my_list[i]):
            print my_list[i][j]
    return my_list