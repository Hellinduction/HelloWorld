import Utils


def start():
    print("Hi!")

    miles_ran = float(input("How many miles did you run? "))
    minutes = float(input("How many minutes did it take you? "))

    pace = minutes / miles_ran
    pace = round(pace, 2)

    print(Utils.formatColor("It took you %s minute(s) to run each mile!", pace))


if __name__ == "__main__":
    start()
