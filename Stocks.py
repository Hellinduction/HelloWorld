import Utils


def calc(quantity, buyPrice, sellPrice):
    quantity = int(quantity)
    buyPrice = float(buyPrice)
    sellPrice = float(sellPrice)

    buyPrice = buyPrice * quantity
    sellPrice = sellPrice * quantity

    return sellPrice - buyPrice


def start():
    print(Utils.formatColor("Welcome to Warrens Stock Profits!"))

    buyPrice = input("What was the cost of 1 stock when you bought it: ")
    sellPrice = input("What was the cost of 1 stock when you sold it: ")
    quantity = input("How many stocks did you exchange: ")

    profit = calc(quantity, buyPrice, sellPrice)
    print(Utils.formatColor("Profit: $%s!", profit))


if __name__ == "__main__":
    start()
