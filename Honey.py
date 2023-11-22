import Utils


def start():
    print(Utils.formatColor("Welcome to the honey calculator!"))

    honeyAmount = int(input("Amount of honey in ml: "))
    size = int(input("Size of your jars in ml: "))

    filled = honeyAmount // size
    remainder = honeyAmount % size

    print(Utils.formatColor("Number of jars filled %s!", filled))
    print(Utils.formatColor("Honey you get to keep %s ml!", remainder))


if __name__ == "__main__":
    start()
