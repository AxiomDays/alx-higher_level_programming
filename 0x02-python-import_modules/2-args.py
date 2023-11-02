#!/usr/bin/python3
import sys
if (len(sys.argv) > 1):
    print(f"{len(sys.argv) - 1} arguments:")
else:
     print(f"{len(sys.argv) - 1} arguments.")
for j in range(len(sys.argv) - 1):
    print(f"{j+1}: {sys.argv[j+1]}")

