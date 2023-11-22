import Utils

months = (
    "Jan",
    "Feb",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "Sep",
    "October",
    "November",
    "December"
)


def start():
    running = True

    while running:
        month_num = int(input("Enter the number of the month [1-12]: "))

        if month_num > len(months) or month_num < 1:
            print("The number you entered is not a valid month!")
            continue

        print(f"The number you entered corresponds to {months[month_num - 1]}")
        running = Utils.toBool(input("Do you want to convert another number? "))


if __name__ == "__main__":
    start()
