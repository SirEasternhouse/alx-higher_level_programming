#!/usr/bin/python3
for char in range(ord('a'), ord('z') + 1):
    print("{}".format(chr(char)), end='\n' if char == ord('z') else'')
