#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    ant = roman[roman_string[0]]
    if type(roman_string) is not str or roman_string == '':
        return 0
    else:
        for i in roman_string:
            if roman[i] <= ant:
                num += roman[i]
                ant = roman[i]
            else:
                num = num + roman[i] - (2 * ant)
                ant = roman[i]
    return num
