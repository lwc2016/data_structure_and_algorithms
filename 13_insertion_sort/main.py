"""
插入排序
"""


def insertion_sort(array: list[int | float]):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
            else:
                break


if __name__ == "__main__":
    data = [4, 1, 3, 5, 7, 6, 10, 2, 9, 8]
    insertion_sort(data)
    print(data)

    data2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    insertion_sort(data2)
    print(data2)

    data3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    insertion_sort(data3)
    print(data3)
