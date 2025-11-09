
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


def main():
    while True:
        input_string = input("-->")
        if input_string == "":
            continue


if __name__ == '__main__':
    try:
        print("Starting...")
        main()
    except Exception as e:
        print(e)
    finally:
        print("Finished.")

