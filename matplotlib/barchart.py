from matplotlib import pyplot as plt

pets = ["Dog", "Cat", "Bird", "Fish", "Hamster"]
values = [4, 2, 1, 0, 1]

plt.bar(pets, values, color="#ff00ff")
plt.title("Pets owned by our class")

plt.xlabel("Pet")
plt.ylabel("Number of students")

plt.show()
