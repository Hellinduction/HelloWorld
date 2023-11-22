def get(question, data_type):
    while True:
        try:
            i = data_type(input(question))
            assert i > 0
        except (ValueError, AssertionError):
            print("Invalid number.")
            continue

        break

    return i


def calculate_fine(value, days_late):
    multiplier = 0

    if value < 10:
        multiplier = 1.25
    elif 10 <= value <= 35:
        multiplier = 2.75
    elif value > 35:
        multiplier = 4

    return round(multiplier * days_late, 2)


def start():
    value = get("Value: ", float)
    days_late = get("Days Late: ", int)

    fine = calculate_fine(value, days_late)
    print(f"Fine: £{fine}")


if __name__ == "__main__":
    start()
