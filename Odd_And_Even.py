import Utils


def start():
    print(Utils.formatColor("Welcome!!!"))

    word = input("Enter a word: ")

    isEvenLength = len(word) % 2 == 0
    out = "Even" if isEvenLength else "Odd"

    print(Utils.formatColor("Odd or even: %s", out))


if __name__ == "__main__":
    start()
