import Utils


NUMBERS_TO_ASK = 5


def start():
    print(Utils.formatColor("What is up!!!11?"))

    numbers = []
    for i in range(NUMBERS_TO_ASK):
        x = float(input("Enter a number: "))
        numbers.append(x)

    numbers_sum = sum(numbers)
    numbers_avg = numbers_sum / len(numbers)

    numbers_sum = round(numbers_sum, 2)
    numbers_avg = round(numbers_avg, 2)

    print(Utils.formatColor("Sum: %s", numbers_sum))
    print(Utils.formatColor("Average: %s", numbers_avg))


if __name__ == "__main__":
    start()
