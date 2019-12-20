#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        sumw = 0
        sums = 0
        for i in range(len(my_list)):
            sums = sums + (my_list[i][0] * my_list[i][1])
            sumw += my_list[i][1]
        return sums / sumw
    else:
        return 0
