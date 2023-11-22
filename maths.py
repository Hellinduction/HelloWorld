import Utils

@DeprecationWarning
def start():  # Unsafe
    env = {"locals": None, "globals": None, "__name__": None, "__file__": None, "__builtins__": None}
    equation = input(Utils.formatColor("Enter the equation: "))
    solve = eval(equation, env)
    print(Utils.formatColor("Answer: %s", solve))


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def divide(x, y):
    return x / y


def multiply(x, y):
    return x * y


def startMaths():  # This function takes in 2 numbers with an operator inbetween and does a mathematical calculation
    # based off of that
    equation = input(Utils.formatColor("Enter the equation: "))
    equation = equation.replace(" ", "")

    operator = None
    operatorFunc = None

    if "+" in equation:
        operatorFunc = add
        operator = "+"
    elif "-" in equation:
        operatorFunc = subtract
        operator = "-"
    elif "/" in equation:
        operatorFunc = divide
        operator = "/"
    elif "*" in equation:
        operatorFunc = multiply
        operator = "*"

    splits = equation.split(operator)

    x = float(splits[0])
    y = float(splits[1])

    answer = round(operatorFunc(x, y), 2)
    print(Utils.formatColor(f"%s {operator} %s = %s", x, y, answer))


if __name__ == "__main__":
    startMaths()
