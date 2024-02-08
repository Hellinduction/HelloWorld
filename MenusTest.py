import Menus
from Menus import Menu


@Menu.option("Print hello world")
def hello_world():
    print("Hello world!")


@Menu.option("Add two numbers together")
def numbers():
    a = Menus.get_number("First number: ")
    b = Menus.get_number("Second number: ")

    print(f"{a} + {b} = {a + b}")


def start():
    menu = Menu()
    menu.process_file("MenusTest.py")
    menu.process()


if __name__ == "__main__":
    start()
