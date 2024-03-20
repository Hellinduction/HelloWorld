import pandas as pd
import pandas.core.frame
from matplotlib import pyplot as plt

import sales_records.Sale

PATH = "sales.csv"


# predicate -> Should be a function that accepts a number and if it returns true it will fail
# response -> Response to predicate returning true
def get(question: str, predicate=None, response: str = "Your choice is out of the bounds of this menu :(", upper_bound: int = 0, var_type=int):
    while True:
        try:
            choice: var_type = var_type(input(question))

        except ValueError:
            print("That is not a valid number :(")
            continue

        if predicate is not None and predicate(choice, upper_bound):
            print(response)
            continue

        break

    return choice


def display_all_by_units_sold(data: pandas.core.frame.DataFrame):
    values = data.sort_values(by="Units Sold", ascending=False)
    sales = sales_records.Sale.convert(values)

    print("Sales by units sold:")

    for sale in sales:
        print(sale.to_str_short())

    print("\n")


def search_for_order(data: pandas.core.frame.DataFrame):
    order_id: int = get("Enter the Order's ID: ")
    data = data.where(data["Order ID"] == order_id).dropna()

    sale = sales_records.Sale.convert(data)[0]
    print(sale.to_str())


def get_countries(data: pandas.core.frame.DataFrame) -> list:
    return data["Country"].unique().tolist()


def get_sales_by_country(data: pandas.core.frame.DataFrame) -> list:
    countries: list = get_countries(data)
    present_choices(countries)

    max_choice: int = len(countries)
    choice = get(f"Select an option (1-{max_choice}): ", predicate=is_out_of_bounds, upper_bound=max_choice)
    country = countries[choice - 1]

    data = data.where(data["Country"] == country).dropna()
    sales = sales_records.Sale.convert(data)

    return sales


def show_orders_by_country(data: pandas.core.frame.DataFrame):
    sales = get_sales_by_country(data)
    print(f"Sales from {sales[0].country}:\n")

    for sale in sales:
        print(f"[{sale.order_date}] Type: {sale.item_type} -> Revenue: {sale.calc_revenue()}")


def get_item_types(data: pandas.core.frame.DataFrame):
    return data["Item Type"].unique().tolist()


def show_profit_for_type(data: pandas.core.frame.DataFrame):
    total_profit: float = 0
    types: list = get_item_types(data)

    max_choice: int = len(types)
    present_choices(types)
    choice = get(f"Select an option (1-{max_choice}): ", predicate=is_out_of_bounds, upper_bound=max_choice)
    item_type = types[choice - 1]

    data = data.where(data["Item Type"] == item_type).dropna()
    sales = sales_records.Sale.convert(data)

    for sale in sales:
        total_profit += sale.calc_profit()

    print(f"The total profit for {item_type} is ${total_profit}.")


def profit_range_search(data: pandas.core.frame.DataFrame):
    lower = get("Enter the lower bound for profit: ", var_type=float)
    upper = get("Enter the upper bound for profit: ", var_type=float)

    sales = sales_records.Sale.convert(data)
    sales = filter(lambda s: lower < s.calc_profit() < upper, sales)

    print(f"The following are in the profit range of {lower}-{upper}:\n")

    for sale in sales:
        print(f"[{sale.order_id}] Type: {sale.item_type} -> Country: {sale.country} -> Units Sold: {sale.units_sold}")


def display_pie_chart(data: pandas.core.frame.DataFrame):
    sales = get_sales_by_country(data)
    type_counts = {}

    for sale in sales:
        count = 1

        if sale.item_type in type_counts.keys():
            count += type_counts[sale.item_type]

        type_counts[sale.item_type] = count

    plt.pie(type_counts.values(),
            labels=type_counts.keys(),
            autopct="%.0f%%")

    plt.title(f"Ordered item types in {sales[0].country}")
    plt.show()


MENU = {
    "Display all by units sold": display_all_by_units_sold,
    "Search for an order by its ID": search_for_order,
    "Show orders by country": show_orders_by_country,
    "Show profits for item type": show_profit_for_type,
    "Search by a profit range": profit_range_search,
    "Display a pie chart of most ordered item types in country": display_pie_chart
}


def present_choices(keys):
    counter: int = 0
    for key in keys:
        counter += 1
        print(f"{counter}. {key}")


def menu():
    print("***MAIN MENU***\n")
    present_choices(MENU.keys())

    print("\n")


def is_out_of_bounds(choice: int, upper_bound: int) -> bool:
    return choice < 1 or choice > upper_bound


def get_menu_choice() -> int:
    max_choice: int = len(MENU)
    choice = get(f"Select an option (1-{max_choice}): ", predicate=is_out_of_bounds, upper_bound=len(MENU))
    return choice


def main():
    global PATH

    data = pd.read_csv(PATH)
    while True:
        menu()
        choice: int = get_menu_choice()
        func = list(MENU.values())[choice - 1]

        func(data)


if __name__ == "__main__":
    main()
