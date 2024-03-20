from matplotlib import pyplot as plt

colors = ["Blue", "Brown", "Green", "Grey"]
values = [5, 3, 0, 1]

plt.pie(values,
        labels=colors,
        colors=["#327ae6", "#916216", "#32a852", "#4a4a4a"],
        autopct="%.0f%%")

plt.title("T Level Class Eye Color")

plt.show()
