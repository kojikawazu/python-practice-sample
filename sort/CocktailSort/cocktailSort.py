from typing import List
# cocktailSort.py

# ---------------------->
# [2] [5] [1] [8] [7] [3]
# <------------------
# [2] [1] [5] [7] [3] [8]
#     -------------->
# [1] [2] [3] [5] [7] [8]
#     <----------
# [1] [2] [3] [5] [7] [8]
#         ------>
# [1] [2] [3] [5] [7] [8]
# 
# [1] [2] [3] [5] [7] [8]

def cocktail_sort(numbers: List[int]) -> List[int]:

    len_numbers = len(numbers)
    swapped = True
    start = 0
    end = len_numbers - 1
    while swapped:
        swapped = False

        for i in range(start, end):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swapped = True
        
        if not swapped:
            break

        swapped = False
        end = end - 1

        for i in range(end - 1, start - 1, -1):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swapped = True
        
        start = start + 1
    
    return numbers
        
if __name__ == '__main__':
    import random
    nums = [random.randint(0, 1000) for i in range(10)]

    print('[1]')
    print(nums)
    print('-' * 100)

    news_nums = cocktail_sort(nums)
    print(news_nums)
