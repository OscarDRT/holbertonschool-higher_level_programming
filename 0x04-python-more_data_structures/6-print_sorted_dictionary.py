def print_sorted_dictionary(a_dictionary):
    new_dic = sorted(a_dictionary.items())
    for key in enumerate(new_dic):
        print("{}: {}".format(key[1][0], key[1][1]))
