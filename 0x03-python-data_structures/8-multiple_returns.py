#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        length = len(sentence)
        first_char = sentence[0]
    else:
        lenght = 0
        first_char = None

    return length, first_char
