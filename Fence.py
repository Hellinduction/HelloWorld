import math

import Utils

ONE_CAN_OF_PAINT_COST = 6.99
ONE_CAN_OF_PAINT_COVERAGE = 9.55


def start():
    print(Utils.formatColor("Welcome to the fence calculation program!"))

    length = float(input("Enter the length of your garden: "))
    width = float(input("Enter the width of your garden: "))
    height = float(input("Enter the height of your fence: "))

    surface_area = length * height
    surface_area += width * height
    surface_area *= 2

    cans = surface_area / ONE_CAN_OF_PAINT_COVERAGE
    cans = math.ceil(cans)
    cost = round(cans * ONE_CAN_OF_PAINT_COST, 2)

    print(Utils.formatColor("Cans %s.", cans))
    print(Utils.formatColor("Cost $%s.", cost))


if __name__ == "__main__":
    start()
