"""
I fucking hate sorting algorithms
Suicide is a better option honestly
I'm too fucking braindead for this shit
"""


def bubble_sort(numbers):
    size = len(numbers)

    for turn in range(size - 1):
        swaps = 0

        for pos in range(size - turn - 1):
            left = numbers[pos]
            right = numbers[pos + 1]

            if left > right:
                numbers[pos] = right
                numbers[pos + 1] = left
                swaps += 1

        if swaps == 0:
            return


def insertion_sort(numbers):
    size = len(numbers)

    for turn in range(1, size):
        unsorted_number = numbers[turn]
        pos = turn - 1  # An index

        while pos >= 0 and unsorted_number < numbers[pos]:
            numbers[pos + 1] = numbers[pos]
            pos -= 1

        numbers[pos + 1] = unsorted_number
        # print("Sorting {} - {}".format(unsorted_number, numbers))


def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2

        left = array[:mid]
        right = array[mid:]

        merge_sort(left)
        merge_sort(right)

        left_pos = 0
        right_pos = 0
        new_pos = 0

        while left_pos < len(left) and right_pos < len(right):
            if left[left_pos] < right[right_pos]:
                array[new_pos] = left[left_pos]
                left_pos += 1
            else:
                array[new_pos] = right[right_pos]
                right_pos += 1

            new_pos += 1

        while left_pos < len(left):
            array[new_pos] = left[left_pos]
            left_pos += 1
            new_pos += 1

        while right_pos < len(right):
            array[new_pos] = right[right_pos]
            right_pos += 1
            new_pos += 1


def start():
    numbers = [5, 1, 3, 7, 14, 2, 13, 19, 67, 32]
    merge_sort(numbers)

    print(numbers)


if __name__ == "__main__":
    start()
