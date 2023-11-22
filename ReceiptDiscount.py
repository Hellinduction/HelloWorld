import Utils


def apply_discount(cost, amount):
    take_off = cost * (amount / 100)
    return cost - take_off


def start():
    print(Utils.formatColor("YOOOOO!!1"))

    prices = []
    while True:
        item_price = float(input("Item price: "))
        prices.append(item_price)

        another = Utils.toBool(input("Enter another? "))
        if not another:
            break

    total_cost = sum(prices)
    should_apply_discount = Utils.toBool(input("Discount? "))

    diff = None

    if should_apply_discount:
        discount = int(input("Discount percentage: "))
        new_cost = apply_discount(total_cost, discount)
        diff = round(total_cost - new_cost, 2)
        total_cost = round(new_cost, 2)

    if diff is not None:
        print(Utils.formatColor("The discount saved the customer $%s.", diff))

    print(Utils.formatColor("The total cost is $%s.", total_cost))


if __name__ == "__main__":
    start()
