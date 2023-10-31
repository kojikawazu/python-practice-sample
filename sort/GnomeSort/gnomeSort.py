from typing import List
# gnomeSort.py

# |-----|
# [2] [5] [1] [8] [7] [3]
#     |-----|
# [2] [1] [5] [8] [7] [3]
# |-----|
# [1] [2] [5] [8] [7] [3]
#     |-----|
# [1] [2] [5] [8] [7] [3]
#         |-----|
# [1] [2] [5] [8] [7] [3]
#             |-----|
# [1] [2] [5] [7] [8] [3]
#         |-----|
# [1] [2] [5] [7] [8] [3]
#             |-----|
# [1] [2] [5] [7] [8] [3]
#                 |-----|
# [1] [2] [5] [7] [3] [8]
#             |-----|
# [1] [2] [5] [3] [7] [8]
#         |-----|
# [1] [2] [3] [5] [7] [8]
#     |-----|
# [1] [2] [3] [5] [7] [8]
#         |-----|
# [1] [2] [3] [5] [7] [8]
#             |-----|
# [1] [2] [3] [5] [7] [8]
#                 |-----|
# [1] [2] [3] [5] [7] [8]

def gnome_sort(numbers: List[int]) -> List[int]:

    len_numbers = len(numbers)
    index = 0

    while index < len_numbers:
        if index == 0:
            index = index + 1
        if numbers[index] >= numbers[index - 1]:
            index = index + 1
        else:
            numbers[index], numbers[index - 1] = numbers[index - 1], numbers[index]
            index = index - 1

    return numbers

if __name__ == '__main__':
    import random
    nums = [random.randint(0, 1000) for i in range(10)]

    print('[1]')
    print(nums)
    print('-' * 100)

    news_nums = gnome_sort(nums)
    print(news_nums)