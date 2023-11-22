from enum import Enum

import Utils


class Result(Enum):
    WIN = 3
    DRAW = 1
    LOSS = 0


def start():
    print(Utils.formatColor("What is up g???!!"))

    score = 0
    while True:
        result = Result[input("Game result: ").upper()]
        score += result.value

        more = Utils.toBool(input("Would you like to enter another result? "))
        if not more:
            break

    print(Utils.formatColor("The team has accumulated %s points.", score))


if __name__ == "__main__":
    start()
