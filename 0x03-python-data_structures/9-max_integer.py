#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    new_max = my_list[0]
    for i in my_list:
        if i > new_max:
            new_max = i
    return new_max
