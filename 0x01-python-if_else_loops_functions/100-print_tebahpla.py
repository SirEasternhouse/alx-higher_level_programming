#!/usr/bin/python3
for char in reversed(range(ord('A'), ord('Z')+1)):
    if char % 2 == 0:
        print("{}".format(chr(char +32)), end='')
    else:
        print("{}".format(chr(char)), end='')
