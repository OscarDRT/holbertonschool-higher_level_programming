#!/usr/bin/python3
def text_indentation(text):
    if type(text) != str:
        raise TypeError("text must be a string")
    else:
        flag = 0
        for i in range(len(text)):
            if flag == 0 and text[i] == " ":
                flag = 0
                continue
            flag = 1
            if (flag == 1) and (text[i] == '?' or text[i] == '.' or text[i] == ':'):
                print(text[i])
                print()
                flag = 0
            else:
                print(text[i], end='')