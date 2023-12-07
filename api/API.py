import requests
import json

import Utils


class Selection:
    def __init__(self, name, method: classmethod):
        self.name = name
        self.method = method


def raw(games):
    formatted = json.dumps(games, indent=2)
    print(formatted)


def display_game(game, show_id=False):
    if show_id:
        print("ID: " + str(game["id"]))

    print("Name: " + game["name"])
    print("Genres: " + Utils.formatStrList(game["genre"]))


def display_games(games):
    for game in games:
        display_game(game)
        print("\n")


def search_game(games):
    game_name = input("Game to search for: ")

    for game in games:
        if game_name.lower() == game["name"].lower():
            display_game(game, show_id=True)


SELECTIONS = {
    1: Selection("View all games", display_games),
    2: Selection("Search for a game", search_game),
    3: Selection("Exit", None),
    4: Selection("View raw API json", raw)
}


def is_valid(selection_str: str):
    if not selection_str.isdigit():
        return False

    selection = int(selection_str)
    return min(SELECTIONS.keys()) - 1 < selection < max(SELECTIONS.keys()) + 1


def get_selection():
    print("\n***MAIN MENU***")

    for selection in SELECTIONS.keys():
        print(f"{selection}. {SELECTIONS[selection].name}")

    # print("1. View all games")
    # print("2. Search for a game")
    # print("3. Exit")
    # print("4. View raw API json")
    # print("\n")

    selection = input(f"Selection ({min(SELECTIONS.keys())}-{max(SELECTIONS.keys())}): ")
    return selection


def main():
    print("Loading...")

    response = requests.request("GET", "https://api.sampleapis.com/switch/games")

    if response.status_code != 200:
        print("Failed to get data")
        return

    games = response.json()

    # formatted = json.dumps(games, indent=2)
    # print(formatted)

    exit = False

    while not exit:
        selection = get_selection()

        if not is_valid(selection):
            print("Invalid selection")
            continue

        selection_num = int(selection)
        selection: Selection = SELECTIONS[selection_num]
        method = selection.method

        if method is not None:
            method(games)
            continue

        print("Exiting...")
        exit = True
    # for game in games:
    #     print("name: " + game["name"])
    #     print("genres: " + Utils.formatStrList(game["genre"]))


if __name__ == "__main__":
    main()
