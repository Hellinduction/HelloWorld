import Utils


HOURS_WORKED_PER_DAY = 7


def start():
    print(Utils.formatColor("WELCOME! <3"))

    wage = float(input("How much do you earn per hour? "))
    days_worked = int(input("How many days did you work this month? "))
    rent = float(input("How much rent do you pay per month? "))
    other = float(input("How much money do other expenses cost you per month? "))

    money_in = (wage * HOURS_WORKED_PER_DAY) * days_worked
    total_cost = other + rent

    if total_cost > money_in:  # Broke
        print(Utils.formatColor("You do not have enough income to cover all your outgoings."))
    else:
        print(Utils.formatColor("%s", "You have enough income to cover all your outgoings."))


if __name__ == "__main__":
    start()
