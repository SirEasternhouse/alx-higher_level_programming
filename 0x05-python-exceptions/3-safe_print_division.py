#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Inside result: None")
        return None
    except TypeError:
        print("Inside result: None")
        return None
    else:
        print("Inside result: {}".format(result))
    finally:
        return result if 'result' in locals() else None
