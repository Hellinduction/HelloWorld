import Utils


def start():
    print(Utils.formatColor("Welcome to the temperature convertor!"))

    celcius = float(input("Enter the temperature (celcius): "))
    fahrenheit = (celcius * 9 / 5) + 32
    fahrenheit = round(fahrenheit, 2)

    print(Utils.formatColor("Fahrenheit: %s", fahrenheit))


if __name__ == "__main__":
    start()
