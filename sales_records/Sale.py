import pandas.core.frame


class Sale:
    def __init__(self, country: str, item_type: str, order_date: str, order_id: int, ship_date: str, units_sold: int,
                 unit_price: float, unit_cost: float):
        self.country = country
        self.item_type = item_type
        self.order_date = order_date
        self.order_id = order_id
        self.ship_date = ship_date
        self.units_sold = units_sold
        self.unit_price = unit_price
        self.unit_cost = unit_cost

    def calc_revenue(self) -> float:
        return round(self.units_sold * self.unit_price, 2)

    def calc_total_cost(self) -> float:
        return round(self.units_sold * self.unit_cost, 2)

    def calc_profit(self) -> float:
        return round(self.calc_revenue() - self.calc_total_cost(), 2)

    def to_str_short(self) -> str:
        return f"[{self.order_id}] ({self.order_date}) -> Country: {self.country} -> Type: {self.item_type} ->" \
               f" Sold: {self.units_sold}"

    def to_str(self) -> str:
        return f"ID: {self.order_id}\nOrder Date: {self.order_date}\nShip Date: {self.ship_date}\nCountry: {self.country}" \
               f"\nType: {self.item_type}\nUnits Sold: {self.units_sold}\nUnit Price: {self.unit_price}" \
               f"\nUnit Cost: {self.unit_cost}"


def convert(origin: pandas.core.frame.DataFrame, limit: int = -1) -> list:
    sales = []

    if limit < 0 or len(origin) < limit:
        count = len(origin)
    else:
        count = limit

    countries: list = origin["Country"].tolist()
    item_types: list = origin["Item Type"].tolist()
    order_dates: list = origin["Order Date"].tolist()
    order_ids: list = origin["Order ID"].tolist()
    ship_dates: list = origin["Ship Date"].tolist()
    units_sold_list: list = origin["Units Sold"].tolist()
    unit_prices: list = origin["Unit Price"].tolist()
    unit_costs: list = origin["Unit Cost"].tolist()

    for i in range(count):
        country: str = str(countries[i])
        item_type: str = str(item_types[i])
        order_date: str = str(order_dates[i])
        order_id: int = int(order_ids[i])
        ship_date: str = str(ship_dates[i])
        units_sold: int = int(units_sold_list[i])
        unit_price: float = float(unit_prices[i])
        unit_cost: float = float(unit_costs[i])

        sale = Sale(country, item_type, order_date, order_id, ship_date, units_sold, unit_price, unit_cost)
        sales.append(sale)

    return sales
