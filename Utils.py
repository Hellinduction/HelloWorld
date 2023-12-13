import random
import string

from colorama import Fore, Style

colors = [Fore.RED, Fore.GREEN, Fore.BLACK, Fore.BLUE, Fore.CYAN, Fore.LIGHTBLACK_EX, Fore.YELLOW, Fore.MAGENTA]


def toBool(b):
    b = b.lower()

    if b == "y" or b == "yes":
        return True

    if b == "n" or b == "no":
        return False

    return False


def getRandomColor():
    length = len(colors)
    rand = random.randint(0, length - 1)
    return colors[rand]


"""
Returns a nicely formatted version of the list as a string :)
"""


def formatStrList(strList):
    text = ", ".join(strList)

    text = text[0:len(text)] + "."
    return text


def formatDict(dict):
    text = ""

    for key in dict:
        text += str(key) + " -> " + str(dict[key]) + ", "

    text = text[0:len(text) - 2] + "."
    return text


"""
A bit hacky, but gets the key from a value in a dictionary
"""


def getKeyFromValue(dict, value):
    keys = list(dict.keys())
    values = list(dict.values())

    if value not in values:
        return None

    index = values.index(value)
    return keys[index]


def getRandomColor():
    length = len(colors)
    rand = random.randint(0, length - 1)
    return colors[rand]


def getRandomString(length):
    rnd = ""

    for i in range(length):
        rnd += random.choice(string.ascii_uppercase)

    return str(rnd)


def formatColor(text, *args):
    length = len(args)

    for i in range(length):
        text = text.replace("%s", Fore.GREEN + str(args[i]) + Fore.RED, 1)

    return Fore.RED + text + Style.RESET_ALL
