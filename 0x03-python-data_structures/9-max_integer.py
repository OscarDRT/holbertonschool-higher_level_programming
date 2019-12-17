def max_integer(my_list=[]):
    if not my_list:
        return None
    biggest = 0
    for i in range(len(my_list)):
        if int(my_list[i]) >= biggest:
            biggest = int(my_list[i])
    return biggest
