#!/usr/bin/python3
"""function that prints a text with 2 new lines after each
 of these characters: ., ? and :
"""


def text_indentation(text):
    """
        text must be a string, otherwise raise a TypeError
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    else:
        t = text
        flag = 0
        for i in range(len(t)):
            if flag == 0 and t[i] == " ":
                flag = 0
                continue
            flag = 1
            if (flag == 1) and (t[i] == '?' or t[i] == '.' or t[i] == ':'):
                print(t[i])
                print()
                flag = 0
            else:
                print(t[i], end='')
