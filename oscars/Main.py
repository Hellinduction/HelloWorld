import pandas as pd
import pandas.core.frame
from inspect import signature

import oscars.Oscar


def display_oscars_list(oscars_list: list):
    for oscar in oscars_list:
        print(f"{oscar.year} -> {oscar.name} at {oscar.age} years old")


def display_all(data: pandas.core.frame.DataFrame):
    sorted_data = data.sort_values(by="Year", ascending=True)
    oscars_list = oscars.Oscar.convert(sorted_data)
    display_oscars_list(oscars_list)


def display_each_year_by_gender(data: pandas.core.frame.DataFrame):
    years = data.sort_values(by="Year", ascending=True)["Year"].tolist()

    for year in years:
        males = data.where((data["Sex"] == "M") & (data["Year"] == year)).dropna()
        females = data.where((data["Sex"] == "F") & (data["Year"] == year)).dropna()

        males = oscars.Oscar.convert(males)
        females = oscars.Oscar.convert(females)

        print(f"Year {year}:")
        print("\tMales:")

        for m in males:
            print(f"\t\t{m.name}")

        print("\tFemales:")

        for f in females:
            print(f"\t\t{f.name}")


def range_search(data: pandas.core.frame.DataFrame):
    lower = get_number("Enter the lower year: ")
    upper = get_number("Enter the higher year: ")
    sex = get_sex()

    new_data = data.where(
        (data["Year"] >= lower) &
        (data["Year"] <= upper) &
        (data["Sex"] == sex)
    ).dropna().sort_values(by="Year", ascending=True)

    oscars_list = oscars.Oscar.convert(new_data)
    display_oscars_list(oscars_list)


def display_duplicates(data: pandas.core.frame.DataFrame):
    duplicates = data["Name"].value_counts().dropna()
    duplicates = duplicates[duplicates > 1]

    for duplicate in duplicates.keys():
        print(duplicate)


def display_average_age_by_sex(data: pandas.core.frame.DataFrame):
    sex = get_sex()

    mean = data.where(data["Sex"] == sex).dropna().sort_values(by="Year", ascending=True)["Age"].mean()
    mean = round(mean)

    print(f"Average age of {sex} is: {mean}")


def exit_program():
    print("Thank you!")
    exit(0)


MENU = {
    "Display all names and ages in ascending order of year": display_all,
    "Display names by gender for each year": display_each_year_by_gender,
    "Display all by age range and sex": range_search,
    "Display actors who have won multiple times": display_duplicates,
    "Display average age of a sex": display_average_age_by_sex,
    "Exit": exit_program
}


def display_menu():
    print("*** Main Menu ***")

    for i in range(1, len(MENU) + 1):
        print(f"{i}. {list(MENU.keys())[i - 1]}")


def get_number(question, data_type=int, upper_bound=-1, lower_bound=-1):
    while True:
        try:
            i = data_type(input(question))

            if i <= 0 or (lower_bound != -1 and i < lower_bound):
                raise ValueError("Provided value was too low")

            if upper_bound != -1 and i > upper_bound:
                raise ValueError("Provided value was too high")
        except ValueError as e:
            print(e)
            continue

        break

    return i


def get_sex():
    valid_sexes = ("M", "F")

    while True:
        sex = input("Enter sex (M/F): ").upper()

        if sex not in valid_sexes:
            print(f"'{sex}' is not a valid sex.")
            continue

        break

    return sex


FILE = "oscar_winners.csv"


def start():
    data = pd.read_csv(FILE)

    while True:
        display_menu()
        choice = get_number(f"Choose a menu option ({1}-{len(MENU)}): ", lower_bound=1, upper_bound=len(MENU))

        print()

        function = list(MENU.values())[choice - 1]

        if len(signature(function).parameters) == 0:
            function()
        else:
            function(data)

        print()


if __name__ == "__main__":
    start()
