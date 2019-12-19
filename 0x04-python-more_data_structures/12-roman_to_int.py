#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string == "":
        return 0
    else:
        rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        num = 0
        ant = rom[roman_string[0]]
        for i in roman_string:
            if rom[i] <= ant:
                num += rom[i]
                ant = rom[i]
            else:
                num = num + rom[i] - (2 * ant)
                ant = rom[i]
        return num
