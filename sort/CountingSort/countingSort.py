from typing import List
# countingSort.py

# [4] [3] [6] [2] [3] [4] [7]

#  0   1   2   3   4   5   6   7
# [0] [0] [0] [0] [0] [0] [0] [0]

#  0   1   2   3   4   5   6   7
# [0] [0] [1] [2] [2] [0] [1] [1]

#  0   1   2   3   4   5   6   7
# [0] [0] [1] [3] [5] [5] [6] [7]

# -----------------------------------------------------

# [4] [3] [6] [2] [3] [4] [7]

#  0   1   2   3   4   5   6   7
# [0] [0] [1] [3] [5] [5] [6] [6]
#  0   1   2   3   4   5   6
# [ ] [ ] [ ] [ ] [ ] [ ] [7]

#  0   1   2   3   4   5   6   7
# [0] [0] [1] [3] [4] [5] [6] [6]
#  0   1   2   3   4   5   6
# [ ] [ ] [ ] [ ] [4] [ ] [7]

#  0   1   2   3   4   5   6   7
# [0] [0] [1] [2] [4] [5] [6] [6]
#  0   1   2   3   4   5   6
# [ ] [ ] [3] [ ] [4] [ ] [7]

#  0   1   2   3   4   5   6   7
# [0] [0] [0] [2] [4] [5] [6] [6]
#  0   1   2   3   4   5   6
# [2] [ ] [3] [ ] [4] [ ] [7]

#  0   1   2   3   4   5   6   7
# [0] [0] [0] [2] [4] [5] [5] [6]
#  0   1   2   3   4   5   6
# [2] [ ] [3] [ ] [4] [6] [7]

#  0   1   2   3   4   5   6   7
# [0] [0] [0] [2] [4] [5] [5] [6]
#  0   1   2   3   4   5   6
# [2] [3] [3] [ ] [4] [6] [7]

#  0   1   2   3   4   5   6   7
# [0] [0] [0] [2] [4] [5] [5] [6]
#  0   1   2   3   4   5   6
# [2] [3] [3] [4] [4] [6] [7]

def counting_sort(numbers: List[int]) -> List[int]:

    max_num = max(numbers)
    counts = [0] * (max_num + 1)
    result = [0] * len(numbers)

    for num in numbers:
        counts[num] += 1

    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]
    
    i = len(numbers) - 1
    while i >= 0:
        index = numbers[i]
        result[counts[index] - 1] = numbers[i]
        counts[index] -= 1
        i -= 1
    
    return result

if __name__ == '__main__':
    import random
    nums = [random.randint(0, 1000) for i in range(10)]

    print('[1]')
    print(nums)
    print('-' * 100)

    news_nums = counting_sort(nums)
    print(news_nums)