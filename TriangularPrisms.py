import Utils


def calc(base, height, length):  # Calculate the volume of a triangular prism
    return 0.5 * base * height * length


def start():
    print(Utils.formatColor("Calculate the volume of a triangular prism!"))

    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    length = float(input("Enter length: "))

    vol = calc(base, height, length)
    print(Utils.formatColor("The volume is %s!", vol))


if __name__ == "__main__":
    start()
