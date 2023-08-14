#!/usr/bin/python3
def no_c(my_string):
    new = list(my_string)
    new = [char for char in new if char.lower() != 'c']
    mplinti = ''.join(new)
    return mplinti
