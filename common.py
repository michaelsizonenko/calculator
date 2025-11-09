

def is_digit(s):
    return s in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def is_operation(operation):
    return operation in ["+", "-", "*", "/"]