"""
选择排序
"""


def select_sort(array: list[int | float]):
    for i in range(0, len(array)):
        min_index = i

        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j

        if i != min_index:
            # 最小值
            array[min_index], array[i] = array[i], array[min_index]


if __name__ == "__main__":
    data = [4, 1, 3, 5, 7, 6, 10, 2, 9, 8]
    select_sort(data)
    print(data)

    data2 = [1]
    select_sort(data2)
    print(data2)

    data3 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    select_sort(data3)
    print(data3)

    data4 = [2, 1]
    select_sort(data4)
    print(data4)
            