class BioStat:
    def __init__(self, name, sex, age, height, weight):
        self.name = name
        self.sex = sex
        self.age = age
        self.height = height
        self.weight = weight

    def calculate_bmi(self):
        return round(self.weight / self.height ** 2 * 703, 2)

    def get_bmi_type(self):
        bmi = self.calculate_bmi()

        if 0 <= bmi < 18.5:
            return "Underweight"

        elif 18.5 <= bmi < 25:
            return "Healthy weight"

        elif 25 <= bmi < 30:
            return "Overweight"

        elif 30 <= bmi < 40:
            return "Obese"

        else:
            return "Morbidly obese"


def convert(stats_data, limit=-1):
    stats = []

    if limit < 0 or len(stats_data) < limit:
        count = len(stats_data)
    else:
        count = limit

    names = stats_data["Name"].tolist()
    sexes = stats_data["Sex"].tolist()
    ages = stats_data["Age"].tolist()
    heights = stats_data["Height (in)"].tolist()
    weights = stats_data["Weight (lbs)"].tolist()

    for i in range(count):
        name: str = names[i]
        sex: str = sexes[i]
        age: int = int(ages[i])
        height: int = int(heights[i])
        weight: int = int(weights[i])

        bioStat = BioStat(name, sex, age, height, weight)
        stats.append(bioStat)

    return stats
