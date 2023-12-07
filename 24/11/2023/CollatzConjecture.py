def main():
    valid = False

    while not valid:
        n = input()

        if n.isdigit():
            n = int(n)

            if n < 1:
                print("Number cannot be below 1")
                continue

            valid = True
        else:
            print("Invalid number")
            continue

    answer = figure_it_out(n, 0)
    print(f"{answer} steps is required to reach 1")


def figure_it_out(n, steps):
    if n == 1:
        return steps

    is_even = n % 2 == 0

    if is_even:
        n = n / 2
    else:
        n = 3 * n + 1

    return figure_it_out(n, steps + 1)


if __name__ == "__main__":
    main()
