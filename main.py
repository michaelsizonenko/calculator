from common import is_operation, is_float, is_integer, is_digit


def main():
    display = '0'
    left_operand = '0'
    operation = None
    right_operand = '0'
    while True:
        input_string = input("-->")

        if input_string == "exit":
            return

        if input_string == "":
            print("Empty input")
            print(display)
            continue

        if is_digit(input_string):
            print("Digit input")
            if left_operand and operation:
                right_operand = input_string if right_operand == "0" else right_operand + input_string
                display = right_operand
                print(display)
                continue

            left_operand = input_string if left_operand == "0" else left_operand + input_string
            display = left_operand
            print(display)
            continue

        if is_operation(input_string):
            print("Operation input")
            operation = input_string
            print(display)
            continue

        if input_string == "=":
            print(left_operand, operation, right_operand)
            if int(left_operand) and operation and int(right_operand):
                result = eval(f"{left_operand}{operation}{right_operand}")

                left_operand = result
                operation = None
                right_operand = 0

                display = result
                print(display)
                continue

            print(display)
            continue



if __name__ == '__main__':
    try:
        print("Starting...")
        main()
    except Exception as e:
        print(e)
    finally:
        print("Finished.")

