from typing import List
# selectSort.py

# ---------------------->
# [2] [5] [1] [8] [7] [3]
#     ------------------>
# [1] [5] [2] [8] [7] [3]
#         -------------->
# [1] [2] [5] [8] [7] [3]
#             ---------->
# [1] [2] [3] [8] [7] [5]
#                 ------>
# [1] [2] [3] [5] [7] [8]
#                     -->
# [1] [2] [3] [5] [7] [8]

def selection_sort(numbers: List[int]) -> List[int]:

    len_numbers = len(numbers)
    for i in range(len_numbers):
        min_idx = i
        for j in range(i + 1, len_numbers):
            if numbers[min_idx] > numbers[j]:
                min_idx = j

        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]

    return numbers


if __name__ == '__main__':
    import random
    nums = [random.randint(0, 1000) for i in range(10)]

    print('[1]')
    print(nums)
    print('-' * 100)

    news_nums = selection_sort(nums)
    print(news_nums)