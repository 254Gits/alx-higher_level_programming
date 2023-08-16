#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    num = len(sys.argv) - 1

    if num == 1:
        arg_word = "argument"
    else:
        arg_word = "arguments"

    print("{} {}:".format(num, arg_word))

    for i, arg in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(i, arg))
