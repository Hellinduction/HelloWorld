# Loops (Called it this cuz tribute to friend)
import random


def start():
    risk_score()


def multiples_of_3():
    num = int(input())

    for i in range(1, num + 1):
        if i % 3 == 0:
            print(i)


def risk_score():
    num_of_patients = int(input("Number of patients: "))

    for i in range(num_of_patients):
        name = input("Name: ")
        age = int(input("Age: "))
        cavities = int(input("Cavities: "))
        missing_teeth = int(input("Missing teeth: "))

        risk = 0.5 * age + cavities * 2 + missing_teeth * 5
        print(f"Risk score for {name} is {risk}.")

        rand = random.randint(1, 100)
        if rand >= 99:
            print("Your going to fucking die")


def let_the_guessing_begin():
    rand = random.randint(1, 10)
    print("Guess the number between 1 and 10")

    while True:
        guess = int(input("Guess: "))
        if guess < 1 or guess > 10:
            print("Invalid")
            continue

        if guess == rand:
            print("CORRECT")
            break

        if guess > rand:
            print("Go lower")
            continue

        print("Go higher")


def i_dont_even_care_anymore():
    num = int(input("Enter a number: "))

    if num < 1:
        print("Ha your funny")

    val = num
    count = 0

    while val < 1000000:
        val *= 2
        count += 1

    print(f"In order to reach/surpass 1 million, it must double {count} times.")


if __name__ == "__main__":
    start()
