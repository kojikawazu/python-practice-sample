from typing import List
# mergeSort.py

# [5][4][1][8][7][3][2][9]

# [5][4][1][8]  |  [7][3][2][9]

# [5][4]  |  [1][8]  |  [7][3]  |  [2][9]

# [5]  |  [4]  |  [1]  |  [8]  |  [7]  |  [3]  |  [2]  |  [9]

# [4][5]  |  [1][8]  |  [3][7]  |  [2][9]

# [1][4][5][8]  |  [2][3][7][9]

# [1][2][3][4][5][7][8][9]

def merge_sort(numbers: List[int]) -> List[int]:

    if len(numbers) <= 1:
        return numbers

    center = len(numbers) // 2
    left   = numbers[:center]
    right  = numbers[center:]

    merge_sort(left)
    merge_sort(right)

    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            numbers[k] = left[i]
            i += 1
        else:
            numbers[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        numbers[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        numbers[k] = right[j]
        j += 1
        k += 1

    return numbers

if __name__ == '__main__':
    import random
    nums = [random.randint(0, 1000) for i in range(10)]

    print('[1]')
    print(nums)
    print('-' * 100)

    news_nums = merge_sort(nums)
    print(news_nums)