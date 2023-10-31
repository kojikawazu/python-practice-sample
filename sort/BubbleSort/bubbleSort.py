from typing import List
# bubbleSort.py

# ---------------------->
# [2] [5] [1] [8] [7] [3]
# ------------------>
# [2] [1] [5] [7] [3] [8]
# -------------->
# [1] [2] [5] [3] [7] [8]
# ---------->
# [1] [2] [3] [5] [7] [8]
# ------>
# [1] [2] [3] [5] [7] [8]
# -->
# [1] [2] [3] [5] [7] [8]
# >
# [1] [2] [3] [5] [7] [8]

def bubble_sort(numbers: List[int]) -> List[int]:

    len_numbers = len(numbers)
    for i in range(len_numbers):
        for j in range(len_numbers - 1 - i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

if __name__ == '__main__':
    import random
    nums = [random.randint(0, 1000) for i in range(10)]

    print('[1]')
    print(nums)
    print('-' * 100)

    news_nums = bubble_sort(nums)
    print(news_nums)
