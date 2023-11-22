def get_float(question):
    while True:
        try:
            i = float(input(question))
            assert i > 0
        except (ValueError, AssertionError):
            print("Invalid number.")
            continue

        break

    return i


def classify(bmi):
    if bmi < 18.5:
        return "Underweight"

    if 18.5 > bmi < 24.9:
        return "Normal weight"

    if 25 > bmi < 29.9:
        return "Overweight"

    if 30 > bmi < 39.9:
        return "Obese"

    return "Morbidly obese"


def start():
    weight = get_float("Weight (kg): ")
    height = get_float("Height (metres): ")

    bmi = round(weight / height ** 2, 2)
    classification = classify(bmi)

    print(f"BMI: {bmi}")
    print(f"Classification: {classification}")


if __name__ == "__main__":
    start()
