def start():
    print("Hellooo!!!1")

    number = int(input("Enter number: "))

    string = ""
    for i in range(1, number + 1):
        divisible_by_3 = i % 3 == 0
        divisible_by_5 = i % 5 == 0

        if divisible_by_3:
            string += "Fizz"
        if divisible_by_5:
            string += "Buzz"

        if not divisible_by_3 and not divisible_by_5:
            print(i)
        else:
            print(string)

        string = ""


if __name__ == "__main__":
    start()

