import math

import Utils


def area_of_circle(radius):
    return math.pi * radius ** 2


def start():
    print(Utils.formatColor("Welcome!!!"))

    radius_of_pizza = float(input("Radius of pizza: "))
    radius_of_pizza_without_crust = float(input("Radius of pizza without crust: "))

    area_of_pizza = area_of_circle(radius_of_pizza)
    area_of_pizza_without_crust = area_of_circle(radius_of_pizza_without_crust)

    area_of_crust = area_of_pizza - area_of_pizza_without_crust
    area_of_crust = round(area_of_crust, 2)

    print(Utils.formatColor("Area of crust: %s", area_of_crust))


if __name__ == "__main__":
    start()
