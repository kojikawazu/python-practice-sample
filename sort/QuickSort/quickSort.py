from typing import List
# quickSort.py

# [1][8][3][9][4][5][7]

# [1][8][3][9][4][5][7]
#  ↑                 |- pivot (i= -1, j= 0, sort=True)
# [1][8][3][9][4][5][7]
#     ↑              |- pivot (i=  0, j= 1, sort=False)
# [1][8][3][9][4][5][7]
#        ↑           |- pivot (i=  1, j= 2, sort=True)
# [1][3][8][9][4][5][7]
#           ↑        |- pivot (i=  1, j= 3, sort=False)
# [1][3][8][9][4][5][7]
#              ↑     |- pivot (i=  2, j= 4, sort=True)
# [1][3][4][9][8][5][7]
#                 ↑  |- pivot (i=  3, j= 5, sort=True)
# [1][3][4][5][7][9][8]
#                    |- pivot (i=  4, j= 6, sort=True)

# [1][3][4][5][7][9][8]
#        Left -|- Right

# [1][3][4][5] | [7] | [9][8]

# [1][3][4][5] | [7] | [8][9]

# [1][3][4][5][7][8][9]

def partition(numbers: List[int], low: int, high: int) -> int:
    i = low - 1
    pivot = numbers[high]

    for j in range(low, high):
        if numbers[j] <= pivot:
            i += 1
            numbers[i], numbers[j] = numbers[j], numbers[i]
    
    numbers[i + 1], numbers[high] = numbers[high], numbers[i + 1]
    return i + 1
        
def quickSort(numbers: List[int]) -> List[int]:
    def _quick_sort(numbers: List[int], low: int, high: int) -> None:
        if low < high:
            partition_index = partition(numbers, low, high)
            _quick_sort(numbers, low, partition_index - 1)
            _quick_sort(numbers, partition_index + 1, high)
    
    _quick_sort(numbers, 0, len(numbers) - 1)
    return numbers

if __name__ == '__main__':
    import random
    nums = [random.randint(0, 1000) for i in range(10)]

    print('[1]')
    print(nums)
    print('-' * 100)

    news_nums = quickSort(nums)
    print(news_nums)
