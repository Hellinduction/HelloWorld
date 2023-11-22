import Utils


def getGrade(mark):  # Kinda special
    match mark:
        case _ if mark < 40:
            return "Fail"
        case _ if 40 <= mark <= 49:
            return "D"
        case _ if 50 <= mark <= 59:
            return "C"
        case _ if 60 <= mark <= 69:
            return "B"
        case _ if mark >= 70:
            return "A"


def start():
    print(Utils.formatColor("Go fuck yourself! :D"))

    first_score = float(input("What is the first test score? "))
    second_score = float(input("What is the second test score? "))

    avg = (first_score + second_score) / 2
    avg = round(avg)
    grade = getGrade(avg)

    print(Utils.formatColor("Average: %s", avg))
    print(Utils.formatColor("Grade: %s", grade))


if __name__ == "__main__":
    start()
