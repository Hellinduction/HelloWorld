import math

import Utils


def start():
    print("Welcome to a thing!")

    avg_cured = float(input("Average number of cases cured per day: "))
    avg_infected = float(input("Average number of people infected per day: "))
    current_zombies = int(input("Current amount of zombies: "))

    days_left = (current_zombies - 0) / (avg_cured - avg_infected)
    print(Utils.formatColor("There are %s days left.", math.ceil(days_left)))


if __name__ == "__main__":
    start()
