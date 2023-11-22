def start():
    people = []
    num_of_people = int(input("Number of people: "))

    for i in range(num_of_people):
        age = int(input("Age: "))
        people.append(age)

    youngest = min(people)
    oldest = max(people)
    average = sum(people) / num_of_people

    youngest = round(youngest)
    oldest = round(oldest)
    average = round(average)

    print(f"Youngest: {youngest}")
    print(f"Oldest: {oldest}")
    print(f"Average: {average}")


if __name__ == "__main__":
    start()
