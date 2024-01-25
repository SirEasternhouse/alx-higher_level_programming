#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    best_key = None
    best_value = float('-inf')

    for key, value in a_dictionary.items():
        if value > best_value:
            best_key, best_value = key, value
    return best_key
