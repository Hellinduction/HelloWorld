import os
import Utils
import keyboard

students = []

options = (
    "ADD",
    "EDIT",
    "REMOVE",
    "VIEW"
)

option = "ADD"


def handleKey(e):
    global option

    index = options.index(option)
    up = keyboard.is_pressed("up")

    if (not up and index > len(option) - 2) or (up and index < 1):
        return

    toAdd = 1
    if up:
        toAdd = -1

    option = options[index + toAdd]
    display(option)


def handleEnter(e):
    match option:
        case "ADD":
            addStudent()
        case "EDIT":
            editStudent()
        case "REMOVE":
            removeStudent()
        case"VIEW":
            view()

    display()


def start():
    while True:
        display(option)

        keyboard.on_press_key("up", handleKey)
        keyboard.on_press_key("down", handleKey)

        keyboard.on_press_key("enter", handleEnter)

        keyboard.wait()


def display(option):
    os.system("cls")
    print("Welcome to the Student Manager!")

    for o in options:
        if o == option:
            print("> " + o)
            continue

        print(o)


def addStudent():
    name = input("Students name: ")
    students.append(name)
    print(f"The student {name} has been added.")


def editStudent():
    old_name = input("Students current name: ")

    if old_name not in students:
        print("That student does not exist.")

    new_name = input("Enter the new name for this student: ")
    index = students.index(old_name)
    students[index] = new_name
    print(f"Student {old_name} has been changed to {new_name}.")


def removeStudent():
    name = input("Student to remove: ")
    students.remove(name)
    print(f"Student {name} has been removed.")


def view():
    print(Utils.formatStrList(students))


if __name__ == "__main__":
    start()
