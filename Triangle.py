import Utils


def calc(b, h):
    b = float(b)
    h = float(h)

    return 0.5 * b * h


base = input("What is the base? ")
height = input("What is the height? ")

out = round(calc(base, height), 2)

print(Utils.formatColor("The area of a triangle is: %s!", out))
