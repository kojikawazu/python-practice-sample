from typing import List
# radixSort.py

# [24][10][11][324][201][101][55]

# 1桁目(countingSort)
# [24][10][11][324][201][101][55]
# [10][11][201][101][24][324][55]

# 2桁目(countingSort)
# [10][11][201][101][24][324][55]
# [201][101][10][11][24][324][55]

# 3桁目(countingSort)
# [201][101][10][11][24][324][55]
# [10][11][24][55][101][201][324]

def counting_sort(numbers: List[int], place: int) -> List[int]:

    counts = [0] * 10
    result = [0] * len(numbers)

    for num in numbers:
        index = int(num / place) % 10
        counts[index] += 1

    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]
     
    i = len(numbers) - 1
    while i >= 0:
        index = int(numbers[i] / place) % 10
        result[counts[index] - 1] = numbers[i]
        counts[index] -= 1
        i -= 1
    
    return result

def radix_sort(numbers: List[int]) -> List[int]:

    max_num = max(numbers)
    place = 1

    while max_num > place:
        numbers = counting_sort(numbers, place)
        place *= 10
    
    return numbers

if __name__ == '__main__':
    import random
    nums = [random.randint(0, 1000) for i in range(10)]

    print('[1]')
    print(nums)
    print('-' * 100)

    news_nums = radix_sort(nums)
    print(news_nums)