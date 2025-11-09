



def main():
    while True:
        input_string = input("-->")
        if input_string == "exit":
            return
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

