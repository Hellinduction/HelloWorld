from matplotlib import pyplot as plt

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

coke_sales = [201, 123, 542, 431, 852, 745, 300]
sprite_sales = [89, 69, 262, 236, 601, 124, 350]
fanta_sales = [92, 64, 127, 351, 442, 223, 152]

plt.plot(days, coke_sales, label="Coke", color="#614b0f")
plt.plot(days, sprite_sales, label="Sprite", color="#9e998d")
plt.plot(days, fanta_sales, label="Fanta", color="#ff9d00")

plt.legend()

plt.title("Drink sales per day")

plt.xlabel("Day of week")
plt.ylabel("Sales")

plt.show()
