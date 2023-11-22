import Utils

quantities = {"Pencils": 2, "Rulers": 5, "Staples": 7}


def start():
    print("Welcome!!")


def view():
    print(Utils.formatStrList(quantities))


def edit(key, value):
    add(key, value)


def add(key, value):
    quantities[key] = value


def remove(key):
    quantities.pop(key)


if __name__ == "__main__":
    start()
