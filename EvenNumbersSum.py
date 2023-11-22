import Utils


def start():
    print(Utils.formatColor("What is up gamer man??1!!!11"))

    number = int(input("Enter a number g: "))
    numbers = []

    for i in range(1, number + 1):
        if i % 2 == 0:
            numbers.append(i)

    total = sum(numbers)
    print(Utils.formatColor("Sum: %s", total))


if __name__ == "__main__":
    start()
