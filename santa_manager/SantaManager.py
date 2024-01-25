import os
from json import JSONDecodeError

import jsonpickle
import matplotlib.pyplot as plt

import Utils

PATH = "recipients.json"


class Recipient:
    def __init__(self, name: str, is_nice: bool, income: int):
        self.name = name
        self.is_nice = is_nice
        self.income = income

    """
    Gets the number of presents/coal for this recipient
    """
    def calc_items(self):
        if not self.is_nice:
            return 2  # Every naughty recipient gets 2 coal

        if self.income <= 30000:
            return 3
        elif 30000 <= self.income <= 50000:
            return 5
        elif 50000 <= self.income <= 100000:
            return 7

        return 10


def create_recipients_file():
    if not os.path.exists(PATH):
        file = open(PATH, 'x')
        file.close()


def get_recipients():
    file = open(PATH, 'r')

    try:
        recipients = dict(jsonpickle.decode(file.read()))
    except JSONDecodeError:
        recipients = {}

    file.close()
    return recipients


def save_recipients(recipients):
    file = open(PATH, 'w')
    file.write(jsonpickle.encode(recipients, indent=4))
    file.close()


def display_menu():
    print("1. Add recipient")
    print("2. Edit recipient")
    print("3. Remove recipient")
    print("4. Calculate presents/coal required")
    print("5. Display pie chart")
    print("6. List all recipients")
    print("7. Exit")


def validate_name(name):
    return 2 < len(name) < 32


def add_recipient(edit):
    recipients = get_recipients()
    valid = False

    while not valid:
        name = input("Name: ")
        is_nice = Utils.toBool(input("Is nice (Y/N): "))
        income = input("Household Income: ")

        if not validate_name(name):
            print("Invalid name")
            continue

        if not income.isdigit():
            print("Invalid income")
            continue

        income = int(income)

        if name.lower() in recipients.keys():
            print("A recipient by that name already exists")
            continue

        valid = True

    recipient = Recipient(name, is_nice, income)
    recipients[name.lower()] = recipient

    save_recipients(recipients)

    if not edit:
        print(f"Added recipient {name}!")
    else:
        print(f"Updated details for {name}!")


def edit_recipient(remove):
    recipients = get_recipients()
    valid = False

    while not valid:
        name = input("Name: ")

        if not validate_name(name):
            print("Invalid name")
            continue

        if name.lower() not in recipients.keys():
            print("No such recipient was found")
            continue

        recipients.pop(name.lower())
        save_recipients(recipients)

        if not remove:
            print("Enter the new details of this recipient:")
            add_recipient(True)
        else:
            print(f"The recipient {name} has been removed.")

        valid = True


def calculate_items_required():
    print("Calculating...")

    presents = 0
    coal = 0

    recipients = get_recipients()

    for recipient in recipients.values():
        items = recipient.calc_items()

        if recipient.is_nice:
            presents += items
        else:
            coal += items

    print(f"Total presents required is {presents}.")
    print(f"Total coal required is {coal}.")


def display_pie_chart():
    nice = 0
    naughty = 0

    recipients = get_recipients()

    for recipient in recipients.values():
        if recipient.is_nice:
            nice += 1
        else:
            naughty += 1

    values = (nice, naughty)

    plt.pie(values, labels=("Nice", "Naughty"))
    plt.title("Nice vs Naughty")
    plt.show()


def list_all():
    recipients = get_recipients()

    print(f"Recipients: {Utils.formatStrList(recipients.keys())}")


def main():
    create_recipients_file()
    should_exit = False

    print("\n***Welcome to the Santa's Secret Selector***")

    display_menu()

    while not should_exit:
        selection = input("Selection: ")

        if not selection.isdigit():
            print("A digit was not provided")
            continue

        numeric_selection = int(selection)

        if 1 > numeric_selection > 5:
            print("Invalid selection provided")
            continue

        match numeric_selection:
            case 1:
                add_recipient(False)
            case 2:
                edit_recipient(False)
            case 3:
                edit_recipient(True)
            case 4:
                calculate_items_required()
            case 5:
                display_pie_chart()
            case 6:
                list_all()
            case 7:
                print("Exiting...")
                should_exit = True


if __name__ == "__main__":
    main()
