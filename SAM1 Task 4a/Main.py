import pandas as pd
import pandas.core.frame
from matplotlib import pyplot as plt
import CurrencyConversion

FILE_PATH = "Data.csv"
DATA: pandas.core.frame.DataFrame = None


# Displays the main menu with numbered options
def display_menu():
    print()
    print("***MAIN MENU***")

    print("1. Convert between currencies")
    print("2. View trends for GBP TO USD")
    print("3. View trends for USD TO GBP")
    print("4. Exit")
    print()


"""
Gets a choice from the user
options is how many options there are in the menu
"""


def get_choice(options: int) -> int:
    choice = input(f"Select an option (1-{options}): ")

    try:
        choice = int(choice)  # Ensures choice is an integer and reassigns it
    except ValueError:
        print(f"{choice} is not a valid number.")
        return

    if choice < 1 or choice > options:  # Checks whether choice is outside the allowed bounds
        print("Selected option is out of the bounds of this menu.")
        return

    return choice


# Displays all dates and rates, trends, averages and highest/lowest rate
def display(dates: list, rates: list):
    items = len(DATA)

    # Loop through and print date and rate
    for i in range(items):
        date = dates[i]
        rate = rates[i]

        print(f"{date} - {rate}")

    print()

    # Print lowest and highest rate
    print(f"Lowest rate - {min(rates)}")
    print(f"Highest rate - {max(rates)}")

    print()

    # Work out the average
    average = sum(rates) / len(rates)
    average = round(average, 5)

    print(f"Average rate - {average}")


# Displays a line graph
def display_graph(currency: str, dates: list, rates: list):
    plt.plot(dates, rates)
    plt.xticks(rotation=90)

    plt.title(f"Currency Conversion Rates by Date for {currency}")

    plt.xlabel("Date")
    plt.ylabel("Conversion Rate")

    plt.show()


# Displays information about a currency conversion and displays the graph
def view_trends(currency: str):
    dates = DATA["Date"].tolist()
    rates = DATA[currency].tolist()

    display(dates, rates)
    display_graph(currency, dates, rates)


# Main function called on program start
def main():
    global DATA

    DATA = pd.read_csv(FILE_PATH)  # Reading CSV file
    alive = True

    while alive:
        display_menu()
        choice = get_choice(4)

        if choice is None:
            continue

        # Matching the selected choice with the function
        match choice:
            case 1:
                CurrencyConversion.main()
            case 2:  # GBP TO USD
                view_trends("GBP - USD")
            case 3:  # USD TO GBP
                view_trends("USD - GBP")
            case 4:
                print("Exiting...")
                alive = False


if __name__ == "__main__":
    main()
