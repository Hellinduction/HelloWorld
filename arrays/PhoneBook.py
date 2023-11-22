import Utils

phone_book = {
    "Charlie": "07718963352",
    "Robbie": "06649275592",
    "Gabriel": "95192820571",
    "Bill": "06628193950",
    "Harry": "07729102759"
}


def start():
    displayMenu()

    while True:
        selectChoice()


def displayMenu():
    print("*** MAIN MENU ***")
    print("1. Search by name")
    print("2. Search by a phone number")
    print("3. Add contact")
    print("4. Edit existing contact")
    print("5. Remove a contact")
    print("6. View the phone book contents")
    print("7. Exit")


def searchByName():
    name = input("Enter a contact name: ").title()

    if name not in phone_book:
        print("We do not recognise this name!")
        return

    number = phone_book[name]
    print(f"Phone number: {number}")


def searchByNumber():
    number = input("Enter the phone number: ")
    name = Utils.getKeyFromValue(phone_book, number)

    if name is None:
        print("We did not recognise that number!")
        return

    print(f"The name associated with that number is: {name}")


def addContact():
    name = input("Enter the name of the new contact: ").title()

    if len(name) == 0:
        print("Invalid name!")
        return

    if name in phone_book:
        print(f"{name} is already in the phone book!")
        return

    number = input("Enter the phone number of the new contact: ")

    phone_book[name] = number
    print(f"Associated {name} with the phone number: {number}")


def editContact():
    name = input("Enter the name of the contact you want to edit: ").title()
    number = input("Enter the phone number of the updated contact: ")

    if name not in phone_book:
        print("We did not recognise that name!")
        return

    phone_book[name] = number
    print(f"Updated {name} with the new phone number: {number}")


def removeContact():
    name = input("Enter the name of the contact you want to remove: ").title()

    if name not in phone_book:
        print("We did not recognise that name!")
        return

    phone_book.pop(name)
    print(f"Removed {name} from the phone book.")


def view():
    print(Utils.formatDict(phone_book))


def exitProgram():
    print("Exiting... Have a nice day")
    exit(0)


choices = {
    1: searchByName,
    2: searchByNumber,
    3: addContact,
    4: editContact,
    5: removeContact,
    6: view,
    7: exitProgram
}


def selectChoice():
    choice = input("Select an option [1-7]: ")

    if not choice.isdigit():
        print("Choice is not an integer.")
        return

    choice = int(choice)

    if choice not in choices:
        print("Invalid choice.")
        return

    method = choices[choice]
    method()


if __name__ == "__main__":
    start()
