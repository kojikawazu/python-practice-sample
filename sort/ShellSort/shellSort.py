from typing import List
# shellSort.py

# |---------|
# [5] [6] [9] [2] [3]
#     |---------|
# [5] [2] [9] [6] [3]
#         |---------|
# [5] [2] [3] [6] [9]
# |---------|
# [3] [2] [5] [6] [9]
# |-----|
# [2] [3] [5] [6] [9]
#     |-----|
# [2] [3] [5] [6] [9]
#         |-----|
# [2] [3] [5] [6] [9]
#             |-----|
# [2] [3] [5] [6] [9]

def shell_short(numbers: List[int]) -> List[int]:

    len_numbers = len(numbers)
    gap = len_numbers // 2

    while gap > 0:
        for i in range(gap, len_numbers):
            temp = numbers[i]
            j = i
            while j >= gap and numbers[j - gap] > temp:
                numbers[j] = numbers[j - gap]
                j -= gap
            numbers[j] = temp
        gap = gap // 2
    
    return numbers

if __name__ == '__main__':
    import random
    nums = [random.randint(0, 1000) for i in range(10)]

    print('[1]')
    print(nums)
    print('-' * 100)

    news_nums = shell_short(nums)
    print(news_nums)

