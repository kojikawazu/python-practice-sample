from typing import List
# insertionSort.py

#     |-----|
# [2] [5] [1] [8] [7] [3]
# |-----|
# [2] [1] [5] [8] [7] [3]
#             |-----|
# [1] [2] [5] [8] [7] [3]
# |-----|
# [1] [2] [5] [7] [8] [3]
#                 |-----|
# [1] [2] [5] [7] [8] [3]
#             |-----|
# [1] [2] [5] [7] [3] [8]
#         |-----|
# [1] [2] [5] [3] [7] [8]
# |-----|
# [1] [2] [3] [5] [7] [8]

def insertion_sort(numbers: List[int]) -> List[int]:

    len_numbers = len(numbers)
    for i in range(1, len_numbers):
        tmp = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > tmp:
            numbers[j + 1] = numbers[j]
            j = j - 1

        numbers[j + 1] = tmp
    
    return numbers

if __name__ == '__main__':
    import random
    nums = [random.randint(0, 1000) for i in range(10)]

    print('[1]')
    print(nums)
    print('-' * 100)

    news_nums = insertion_sort(nums)
    print(news_nums)