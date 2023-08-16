#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sums = 0
    for t in range(1, len(sys.argv)):
        sums += int(sys.argv[t])
    print("{}".format(sums))
