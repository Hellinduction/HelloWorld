def start():
    # fraction = input("Fraction: ")
    # splits = fraction.split("/")
    #
    # numerator = int(splits[0])
    # denominator = int(splits[1])
    #
    # result = numerator / denominator

    # Now I know the above code works an all but isn't it fun having RCE exploits in your program for no reason :D
    result = eval(input("Fraction: "))

    if result > 1:
        print("More than 1")
    else:
        print("Not more than 1")


if __name__ == "__main__":
    start()
