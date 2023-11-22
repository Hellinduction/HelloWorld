import Utils


def getPrice(age):
    if 0 < age < 13:
        return 8
    elif 12 < age < 19:
        return 12
    elif 19 < age < 59:
        return 18
    elif age > 59:
        return 15


def start():
    print(Utils.formatColor("NO WAY????!!!1"))

    age = int(input("What is your age? "))
    price = getPrice(age)

    print(Utils.formatColor("The price of your ticket will be: £%s.", price))


if __name__ == "__main__":
    start()
