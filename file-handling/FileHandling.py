import json
from json import JSONDecodeError


def start():
    path = "data.txt"

    file = open(path, 'r')

    try:
        names = list(json.load(file))
    except JSONDecodeError:
        names = []

    file.close()

    name = input("What is your name: ")
    names.append(name)

    file = open(path, 'w')
    json.dump(names, file, indent=4)
    file.close()

    file = open(path, 'r')

    for line in file.readlines():
        print(line.replace("\n", ""))

    file.close()


def E():
    path = "yep.txt"
    file = open(path, 'x')

    file.write("ok")

    # print(file.read())
    # file.write("T")


if __name__ == "__main__":
    start()
