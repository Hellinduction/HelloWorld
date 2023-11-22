import Utils


SQUARE_CHAR = '+'


def start():
    print(Utils.formatColor("Welcome to PLUS SQUARES!!!!1"))

    length = int(input("Number: "))
    to_print = SQUARE_CHAR * length

    for i in range(length):
        print(to_print)


if __name__ == "__main__":
    start()
