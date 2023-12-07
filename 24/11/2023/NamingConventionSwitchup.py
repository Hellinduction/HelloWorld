def main():
    valid = False

    while not valid:
        snake_case = input("Enter a snake case variable name: ")

        if len(snake_case) == 0:
            print("Variable name is too short!")
            continue

        valid = True

    camel_case = convert(snake_case)
    print(camel_case)


def convert(snake_case: str):
    camel_case = snake_case.lower()

    if "_" not in camel_case:
        return camel_case

    splits = camel_case.split("_")
    camel_case = ""

    first_iteration = True

    for part in splits:
        length = len(part)

        first_letter = part[0]

        if not first_iteration:
            first_letter = first_letter.upper()
        else:
            first_iteration = False

        camel_case += first_letter
        camel_case += part[length - length + 1:length]

    return camel_case


if __name__ == "__main__":
    main()
