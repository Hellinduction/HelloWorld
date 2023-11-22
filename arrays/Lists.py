import Utils

fruits = [
    "Pineapple",  # If you don't think it belongs in pizza, we cant be friends!
    "Apple",
    "Orange",
    "Grape",
    "Mango"
]


weed_strains = [  # I have tried all of these and more!
    "Gorilla Glue",
    "Skywalker",
    "Cheese",
    "Star Dawg",
    "Dosido",
    "White Widow",
    "Jack Herer"
]


def start():
    strain = input("Enter a weed strain you have tried: ")
    weed_strains.append(strain)

    print(Utils.formatStrList(weed_strains))


if __name__ == "__main__":
    start()
