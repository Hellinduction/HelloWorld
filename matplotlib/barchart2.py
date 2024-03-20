from matplotlib import pyplot as plt

products = ["Computer", "Apple", "Pear", "Water Bottle", "Juice Bottle"]

sales_on_monday = [23, 53, 34, 154, 123]
sales_on_tuesday = [15, 46, 37, 149, 112]

plt.bar(products, sales_on_monday, label="Monday")
plt.bar(products, sales_on_tuesday, label="Tuesday")
plt.title("Sales Of Products")

plt.xlabel("Products")
plt.ylabel("Sales")

plt.legend()
plt.show()
