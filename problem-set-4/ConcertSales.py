def start():
    num_of_concerts = int(input("Concerts: "))
    concerts = {}

    for i in range(num_of_concerts):
        performer = input("Performer: ")
        sales = int(input("Sales: "))

        concerts[sales] = performer

    least = concerts[min(concerts.keys())]
    most = concerts[max(concerts.keys())]

    print(f"Least: {least}")
    print(f"Most: {most}")


if __name__ == "__main__":
    start()
