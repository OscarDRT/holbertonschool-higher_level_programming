#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        my_list = [[]]
    else:
        final = []
        for index in range(1, n + 1):
            new_list = []
            for x in range(index):
                new_list.append(1)
            final.append(new_list)

        for i in range(len(final)):
            for j in range(len(final[i])):
                if j != 0 and j != len(final[i - 1]):
                    final[i][j] = final[i - 1][j] + final[i - 1][j - 1]
        return final
