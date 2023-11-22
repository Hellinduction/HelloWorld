import Utils


PROGRAMMERS_TO_GET = 3


def find(ls, highest):
    found = None

    for salary in ls:
        if found is None:
            found = salary

        if highest:
            if salary > found:
                found = salary
        else:
            if salary < found:
                found = salary

    return found


def start():
    print(Utils.formatColor("Welcome!!111 :DDDDDD"))

    programmers = []
    for i in range(PROGRAMMERS_TO_GET):
        salary = float(input(Utils.formatColor("Enter the salary of programmer %s: ", i + 1)))
        programmers.append(salary)

    # print(programmers)

    highest = find(programmers, True)
    lowest = find(programmers, False)

    print(Utils.formatColor("Most: $%s", highest))
    print(Utils.formatColor("Least: $%s", lowest))


if __name__ == "__main__":
    start()
