import time

# def linear_search(strList: list, string: str) -> int:
#     index: int = 0
#
#     for item in strList:
#         if item == string:
#             return index
#             break
#
#         index += 1
#
#     return -1


def linear_search(strList: list, string: str) -> int:
    for index, item in enumerate(strList):
        if item == string:
            return index

    return -1


def binary_search(strList: list, string: str) -> int:
    if len(strList) == 0:
        return -1

    strList = sorted(strList)

    low_index: int = 0
    high_index: int = len(strList) - 1

    while low_index <= high_index:
        mid: int = int((high_index + low_index) / 2)

        if strList[mid] == string:
            return mid

        if string > strList[mid]:
            low_index = mid + 1
            continue

        high_index = mid - 1

    return -1


fruits: list = [
    "Watermelon",
    "Kiwi",
    "Apple",
    "Banana",
    "Grapes",
    "Cherries",
    "Pineapple",
]

search: str = "Kiwi"


def start():
    print("Welcome to the search algorithm!")

    print(binary_search(fruits, search))


if __name__ == "__main__":
    start()
