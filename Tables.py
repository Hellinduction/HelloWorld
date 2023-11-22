import Utils


def start():
    print(Utils.formatColor("What is up gamer???!"))

    number = int(input("Enter a number: "))

    for i in range(1, 11):
        value = i * number
        print(Utils.formatColor("%s x %s = %s", i, number, value))


if __name__ == "__main__":
    start()
