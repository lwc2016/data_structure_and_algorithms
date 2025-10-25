"""
冒泡排序
"""


def bubble_sort(array: list[int | float]):
    # 轮次
    for i in range(0, len(array)):
        # 是否交换位置
        is_turned = False
        for j in range(0, len(array) - 1 - i):
            curr_value = array[j]
            next_value = array[j + 1]

            if curr_value > next_value:
                array[j] = next_value
                array[j + 1] = curr_value
                is_turned = True

        # 如果没有调换顺序，说明已经排好了，直接终止
        if not is_turned:
            break


if __name__ == "__main__":
    # data = [4, 1, 3, 5, 7, 6, 10, 2, 9, 8]
    # bubble_sort(data)
    # print(data)

    # data2 = [1]
    # bubble_sort(data2)
    # print(data2)
    #
    # data3 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    # bubble_sort(data3)
    # print(data3)
    #
    # data4 = [2, 1]
    # bubble_sort(data4)
    # print(data4)

    data5 = [2, 1, 4, 3, 6, 5, 7, 8, 9, 10]
    bubble_sort(data5)
    print(data5)
