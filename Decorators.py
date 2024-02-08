def decorator(func):
    def wrapper():
        print("Test1")
        func()
        print("Test2")

    return wrapper


@decorator
def test():
    print("Hello world!")


if __name__ == "__main__":
    test()
