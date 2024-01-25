import pandas as pd


CSV_FILE_PATH: str = "mlb_teams_2012.csv"


def display_menu():
    print("*** MAIN MENU ***")

    print("1. View all teams")
    print("2. View payroll leaderboard")
    print("3. Search for a team")
    print("4. View teams with payroll within specified range")
    print("5. Exit")


class Team:
    def __init__(self, name, payroll, wins):
        self.name = name
        self.payroll = payroll
        self.wins = int(wins)


def convert_to_teams(teams_data, limit=-1):
    teams = []

    team_names = teams_data["Team"].tolist()
    payrolls = teams_data["Payroll (millions)"].tolist()
    wins_list = teams_data["Wins"].tolist()

    if limit < 0 or len(teams_data) < limit:
        count = len(teams_data)
    else:
        count = limit

    for i in range(count):
        team_name = team_names[i]
        payroll = payrolls[i]
        wins = int(wins_list[i])

        team = Team(team_name, payroll, wins)
        teams.append(team)

    return teams


def view_teams(data):
    teams = data["Team"].tolist()
    teams.sort()

    print("Competing teams:")

    for team in teams:
        print(f"-> {team}")


def view_payroll_leaderboard(data, limit=10):
    payroll_lb = data.sort_values(by="Payroll (millions)", ascending=False)

    print("Payroll leaderboard:")

    rank = 1

    for team in convert_to_teams(payroll_lb, limit):
        print(f"{rank}. {team.name} -> {team.payroll} million")
        rank += 1


"""
Probably bad because I am manipulating way more data than I need to
"""
# def search_for_team(data):
#     teams = data["Team"].tolist()
#     team_name = input("Enter the name of the team you would like to search for: ").title()
#
#     if team_name not in teams:
#         print("That team does not exist!")
#         return
#
#     index = teams.index(team_name)
#     payroll = data["Payroll (millions)"][index]
#     wins = data["Wins"][index]
#
#     print(f"{team_name} has a payroll of {payroll} million and has {wins} wins!")


def search_for_team(data):
    team_name = input("Enter the name of the team you would like to search for: ").title()
    teams_data = data.where(data["Team"] == team_name).dropna()

    if teams_data.empty:
        print("That team does not exist!")
        return

    team = convert_to_teams(teams_data)[0]
    print(f"{team.name} has a payroll of ${team.payroll} million and has {team.wins} wins!")


def get_number(question, data_type=int):
    while True:
        try:
            i = data_type(input(question))

            if i <= 0:
                raise ValueError("Provided value of too low")
        except ValueError:
            print("Invalid number.")
            continue

        break

    return i


def payroll_range_search(data):
    lower_bound = get_number("Enter the lower bound of the range (in millions) : $", float)
    upper_bound = get_number("Enter the upper bound of the range (in millions): $", float)

    payroll_data = data.where((data["Payroll (millions)"] >= lower_bound) & (data["Payroll (millions)"] <= upper_bound)).dropna().sort_values(by="Payroll (millions)", ascending=False)

    if payroll_data.empty:
        print("There were no teams found inbetween the payrolls you specified.")
        return

    teams = convert_to_teams(payroll_data)

    for team in teams:
        print(f"{team.name} : ${team.payroll} million : {team.wins} wins")


def start():
    data = pd.read_csv(CSV_FILE_PATH)

    while True:
        display_menu()
        choice = input("Choose a menu option (1-5): ")

        print()

        match choice:
            case "1":
                view_teams(data)

            case "2":
                view_payroll_leaderboard(data)

            case "3":
                search_for_team(data)

            case "4":
                payroll_range_search(data)

            case "5":
                print("Thank you! exiting...")
                return

        print()


if __name__ == "__main__":
    start()
