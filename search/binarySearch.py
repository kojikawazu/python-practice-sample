from typing import List, NewType
# binarySearch

# Search 15

# リニアサーチ(先頭から順次)
# [0][1][5][9][11][15][20][24]

# バイナリサーチ
#  L        M              R
# [0][1][5][9][11][15][20][24]
#           ↑ →

#           L      M       R
# [0][1][5][9][11][15][20][24]
#                  ↑ Hit!!

IndexNum = NewType('IndexNum', int)

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

def linear_search(numbers: List[int], value: int) -> int:

    for i in range(0, len(numbers)):
        if numbers[i] == value:
            return i
    return -1

def binary_search(numbers: List[int], value: int) -> int:
    left, right = 0, len(numbers) - 1
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == value:
            return mid
        elif numbers[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# リカーシブル版
def binary_search_r(numbers: List[int], value: int) -> int:
    def _binary_search(numbers: List[int], value: int,
                        left: IndexNum, right: IndexNum) -> IndexNum:
        if left > right:
            return -1
        
        mid = (left + right) // 2
        if numbers[mid] == value:
            return mid
        elif numbers[mid] < value:
            return _binary_search(numbers, value, mid + 1, right)
        else:
            return _binary_search(numbers, value, left, mid - 1)

    return _binary_search(numbers, value, 0, len(numbers) - 1)        

if __name__ == '__main__':
    import random
    nums = [random.randint(0, 1000) for i in range(10)]
    nums = quickSort(nums)
    search = random.randint(0, 9)

    print('[numbers]')
    print(nums)
    print('-' * 100)
    print()

    print('[1]')
    idx = linear_search(nums, nums[search])
    print(f'Linear Search: {nums[search]} answer: {idx}')
    print('-' * 100)
    print()

    print('[2]')
    idx = binary_search(nums, nums[search])
    print(f'Binary Search: {nums[search]} answer: {idx}')
    print()

    print('[3]')
    idx = binary_search_r(nums, nums[search])
    print(f'Binary Search(recursive) : {nums[search]} answer: {idx}')
    print()