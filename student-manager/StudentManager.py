import json
from json import JSONDecodeError

PATH = "students.json"
ITERATIONS = 3  # Number of scores each student should have


def get_choice():
    valid = False

    while not valid:
        try:
            choice = input("Menu choice (1-3): ")
            assert choice.isdigit()

            choice = int(choice)
            assert 3 >= choice >= 1
        except AssertionError:
            print("Your selection is invalid. Must be between 1 and 3!")

        valid = True

    return choice


def get_students():
    file = open(PATH, 'r')

    try:
        students = dict(json.load(file))
    except JSONDecodeError:
        students = {}

    file.close()
    return students


def add_student(student_name, scores):
    students = get_students()
    students[student_name] = scores

    file = open(PATH, 'w')
    json.dump(students, file, indent=4)
    file.close()


def get_scores(student_name):
    students = get_students()
    return students[student_name]


def get_student_name():
    valid = False

    while not valid:
        student_name = input("Enter the students name: ")
        student_name_length = len(student_name)

        if not (2 <= student_name_length <= 15):
            print("The entered students name is of an invalid length!")
            continue

        students = get_students()

        if student_name in students.keys():
            print("A student by this name is already registered.")
            continue

        valid = True

    return student_name


def get_score(num):
    valid = False

    while not valid:
        score = input(f"Score #{num}: ")

        if not score.isdigit():
            print("Entered score is not a number.")
            continue

        score = int(score)

        if score < 0:
            print("Entered score is below 0.")
            continue

        valid = True

    return score


def start():
    should_exit = False

    print("1. View all")
    print("2. Add new")
    print("3. Exit software")

    while not should_exit:
        choice = get_choice()

        match choice:
            case 1:
                students = get_students()
                counter = 1

                if len(students) == 0:
                    print("There are no stored students :(")
                    continue

                for student_name in students.keys():
                    scores = students[student_name]

                    print(f"\nStudent {counter}:")
                    print(f"Name: {student_name}")

                    score_counter = 1
                    for score in scores:
                        print(f"Score {score_counter}: {score}")
                        score_counter += 1

                    # print("\n")

                    counter += 1
            case 2:
                student_name = get_student_name()
                scores = []

                for i in range(ITERATIONS):
                    score = get_score(i + 1)
                    scores.append(score)

                add_student(student_name, scores)
                print(f"Registered student {student_name}!")
            case 3:
                print("Exiting software...")
                should_exit = True

        print("\n")


if __name__ == "__main__":
    start()
