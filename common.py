

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
    if operation == '+':
        return True
    elif operation == '-':
        return True
    elif operation == '*':
        return True
    elif operation == '/':
        return True
    else:
        return False