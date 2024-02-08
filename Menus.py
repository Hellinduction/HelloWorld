"""
This file is for generating menus easily
"""
import inspect


def get_number(question, data_type=int, upper_bound=-1, lower_bound=1):
    while True:
        try:
            i = data_type(input(question))

            if lower_bound != -1 and i < lower_bound:
                raise ValueError("Provided value was too low")

            if upper_bound != -1 and i > upper_bound:
                raise ValueError("Provided value was too high")
        except ValueError as e:
            print(e)
            continue

        break

    return i


class Menu:
    menu_options = {}

    @classmethod
    def option(cls, message):
        def decorator(func):
            cls.menu_options[message] = func
            return func

        return decorator

    @classmethod
    def process_file(cls, filename):
        cls.menu_options = {}

        module = __import__(filename[:-3])
        all_functions = inspect.getmembers(module, inspect.isfunction)

        decorated_functions = {
            name: func
            for name, func in all_functions
            if isinstance(func, type(cls.option)) and "wrapper" in func.__dict__
        }

        for message, func in cls.menu_options.items():
            if func.__name__ in decorated_functions:
                cls.menu_options[message] = decorated_functions[func.__name__]

    def display_menu(self):
        print("*** Main Menu ***")

        for i in range(1, len(self.menu_options) + 1):
            print(f"{i}. {list(self.menu_options.keys())[i - 1]}")

    def get_choice(self):
        self.display_menu()
        choice = get_number(f"Choose a menu option ({1}-{len(self.menu_options)}): ", lower_bound=1,
                            upper_bound=len(self.menu_options))
        return choice

    def process(self, *args):
        choice = self.get_choice()
        function = list(self.menu_options.values())[choice - 1]

        if len(args) == 0:
            function()
            return

        function(*args)
