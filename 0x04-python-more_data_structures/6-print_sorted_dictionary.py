def print_sorted_dictionary(a_dictionary):
    new_dic = list(sorted(a_dictionary.keys()))
    for key in new_dic:
        print("{}: {}".format(key, a_dictionary[key]))
