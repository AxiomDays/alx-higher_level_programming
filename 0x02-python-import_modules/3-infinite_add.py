#!/usr/bin/python3
import sys
buff = 0
if __name__ == "__main__":
    if (len(sys.argv) > 1):
        for i in sys.argv[1:]:
            buff += int(i)
        print(buff)
    else:
        print(0)
