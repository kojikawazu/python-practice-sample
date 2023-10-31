from typing import List
# bucketSort.py

# [1] [5] [28] [25] [100] [52] [27] [91] [22] [99]

# [0]: [1] [5] -> InsertionSort ->  [1] [5]
# [1]:
# [2]: [28] [25] [27] [22] -> InsertionSort -> [22] [25] [27] [28]
# [3]:
# [4]:
# [5]: [52] -> InsertionSort -> [52]
# [6]:
# [7]:
# [8]:
# [9]: [100] [91] [99] -> InsertionSort -> [91] [99] [100]

# [1] [5] [22] [25] [27] [28] [52] [91] [99] [100]

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

def bucket_sort(numbers: List[int]) -> List[int]:
    max_num = max(numbers)
    len_numbers = len(numbers)
    size = max_num // len_numbers

    buckets = [[] for _ in range(size)]
    for num in numbers:
        i = num // size
        if i != size:
            buckets[i].append(num)
        else:
            buckets[size - 1].append(num)

    for i in range(size):
        insertion_sort(buckets[i])

    result = []
    for i in range(size):
        result += buckets[i]

    return result

if __name__ == '__main__':
    import random
    nums = [random.randint(0, 1000) for i in range(10)]

    print('[1]')
    print(nums)
    print('-' * 100)

    news_nums = bucket_sort(nums)
    print(news_nums)