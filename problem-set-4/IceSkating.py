def start():
    num_of_judges = int(input("Judges: "))
    ratings = []

    for i in range(num_of_judges):
        rating = int(input("Rating: "))
        if rating < 1 or rating > 10:
            print("Invalid rating")
            continue

        ratings.append(rating)

    lowest = min(ratings)
    highest = max(ratings)

    ratings.remove(lowest)
    ratings.remove(highest)

    average = sum(ratings) / len(ratings)
    average = round(average)

    print(f"Final Rating: {average}")


if __name__ == "__main__":
    start()
