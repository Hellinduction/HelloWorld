import pandas.core.frame


class Oscar:
    def __init__(self, year: int, age: int, sex: str, name: str, movie: str):
        self.year = int(year)
        self.age = int(age)
        self.sex = sex
        self.name = name
        self.movie = movie


def convert(origin: pandas.core.frame.DataFrame, limit=-1) -> list:
    data = []

    if limit < 0 or len(origin) < limit:
        count = len(origin)
    else:
        count = limit

    years = origin["Year"].tolist()
    ages = origin["Age"].tolist()
    sexes = origin["Sex"].tolist()
    names = origin["Name"].tolist()
    movies = origin["Movie"].tolist()

    for i in range(count):
        year = years[i]
        age = ages[i]
        sex = sexes[i]
        name = names[i]
        movie = movies[i]

        oscar = Oscar(year, age, sex, name, movie)
        data.append(oscar)

    return data
