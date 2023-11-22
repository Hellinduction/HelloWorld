import Utils


capital_map = {
    "england": "London",
    "wales": "Cardiff",
    "scotland": "Edinburgh",
    "ireland": "Dublin"
}


def start():
    print(Utils.formatColor("\"Hey whats going on guys!!\""))

    country = input("Enter a country g: ").lower()
    capital = capital_map.get(country)

    if capital is None:
        print(Utils.formatColor("Unknown country \"%s\".", country))
        return

    print(Utils.formatColor("The capital city of %s is %s.", country, capital))


if __name__ == "__main__":
    start()
