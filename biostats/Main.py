import pandas as pd
import pandas.core.frame

import biostats.BioStat


def get_number(question, data_type=int):
    while True:
        try:
            i = data_type(input(question))

            if i <= 0:
                raise ValueError("Provided value of too low")
        except ValueError:
            print("Invalid number.")
            continue

        break

    return i


def display_menu():
    print("***Main Menu***")

    print("1. Display all names and ages")
    print("2. View by sex")
    print("3. View by weight range")
    print("4. View by average weight/height by age")
    print("5. View by BMI type")
    print("6. Exit")


def display_names_and_ages(stats: pandas.core.frame.DataFrame):
    names_and_ages = stats.sort_values(by="Age", ascending=True)
    stats = biostats.BioStat.convert(names_and_ages)

    for stat in stats:
        print(f"{stat.name} -> {stat.age} years old")


def view_by_sex(stats: pandas.core.frame.DataFrame):
    valid_sexes = ("M", "F")

    while True:
        sex = input("Sex (M/F): ").upper()

        if sex not in valid_sexes:
            print("Invalid sex.")
            continue

        stats_by_sex = stats.where(stats["Sex"] == sex).dropna()
        stats = biostats.BioStat.convert(stats_by_sex)

        for stat in stats:
            print(f"{stat.name} is {stat.age} years old and weighs {stat.weight} lbs and is {stat.height} in.")
        break


def range_search(stats: pandas.core.frame.DataFrame, lower_bound_question, upper_bound_question, bound_type, table_name):
    lower_bound = get_number(lower_bound_question, bound_type)
    upper_bound = get_number(upper_bound_question, bound_type)

    new_data = stats.where(
        (stats[table_name] >= lower_bound) & (stats[table_name] <= upper_bound)).dropna().sort_values(
        by=table_name, ascending=False)

    if new_data.empty:
        print("There was no data found inbetween the range you specified.")
        return []

    stats = biostats.BioStat.convert(new_data)
    return stats


def view_by_weight_range(stats: pandas.core.frame.DataFrame):
    stats = range_search(stats,
                         "Enter the lower weight (lb): ",
                         "Enter the higher height (lb): ",
                         int,
                         "Weight (lbs)")

    for stat in stats:
        print(f"{stat.name} is sex of {stat.sex} and is {stat.age} years old.")


def view_by_average_weight_and_height_by_age(stats: pandas.core.frame.DataFrame):
    stats = range_search(stats,
                         "Enter the lower age: ",
                         "Enter the upper age: ",
                         int,
                         "Age")

    total_height = sum(stat.height for stat in stats)
    total_weight = sum(stat.weight for stat in stats)

    length = len(stats)

    average_height = total_height / length
    average_weight = total_weight / length

    print(f"Average Height in the age range: {average_height:.2f} in")
    print(f"Average Weight in the age range: {average_weight:.2f} lbs")


def view_by_bmi_type(stats: pandas.core.frame.DataFrame):
    bmi_type = input("Enter the BMI type: ")
    stats = biostats.BioStat.convert(stats)

    for stat in stats:
        if stat.get_bmi_type().lower() != bmi_type.lower():
            continue

        print(f"{stat.name} -> {stat.calculate_bmi()}")


def start():
    stats = pd.read_csv("biostats.csv")

    while True:
        display_menu()
        choice = get_number("Choose a menu option (1-6): ")

        print()

        match choice:
            case 1:
                display_names_and_ages(stats)

            case 2:
                view_by_sex(stats)

            case 3:
                view_by_weight_range(stats)

            case 4:
                view_by_average_weight_and_height_by_age(stats)

            case 5:
                view_by_bmi_type(stats)

            case _:
                print("Thank you for using BioStats! Exiting...")
                break

        print()


if __name__ == "__main__":
    start()
