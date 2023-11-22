def get_int(question):
    while True:
        try:
            i = int(input(question))
            assert i > 0
        except (ValueError, AssertionError):
            print("Invalid number.")
            continue

        break

    return i


def get_points(books):
    if books == 1:
        return 5

    if 2 <= books <= 3:
        return 15

    return 30


def start():
    members = get_int("Members: ")
    points = 0

    for i in range(members):
        books = get_int("Books: ")
        points += get_points(books)

    print(f"Points: {points}")


if __name__ == "__main__":
    start()
