#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    try:
        for i in range(list_length):
            try:
                val_1 = my_list_1[i] if i < len(my_list_1) else 0
                val_2 = my_list_2[i] if i < len(my_list_2) else 0
                if isinstance(val_1, (int, float)) and \
                        isinstance(val_2, (int, float)):
                    if val_2 != 0:
                        result.append(val_1 / val_2)
                    else:
                        print("division by 0")
                        result.append(0)
                else:
                    print("wrong type")
                    result.append(0)
            except IndexError:
                print("out of range")
                break
    except Exception as e:
        print("Error:", e)
    finally:
        return result
