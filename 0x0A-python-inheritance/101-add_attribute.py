#!/usr/bin/python3
def add_attribute(instance, name, value):
    print(hasattr(instance, name))
        #raise TypeError("can't add new attribute")
    instance.name = value