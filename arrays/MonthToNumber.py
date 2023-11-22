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
    month_name = input("Enter a month: ").title()
    month_day = months.index(month_name) + 1  # Index + 1
    print(month_day)


if __name__ == "__main__":
    start()
