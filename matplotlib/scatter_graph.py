from matplotlib import pyplot as plt

temps = [18, 20, 22, 13, 15, 27, 19, 15]
rentals = [32, 72, 67, 24, 24, 79, 44, 15]

plt.scatter(temps, rentals, color="#00ffff")

plt.title("Bike rentals by temperature")

plt.xlabel("Temperatures")
plt.ylabel("Bike rentals")

plt.show()
