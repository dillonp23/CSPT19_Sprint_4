
""" Sprint 4.1: Hash Tables I - CodeSignal Assignment """



"""
Exercise 1: Find The Single Number (task 4 of 6)

You are given a non-empty array of integers. One element appears exactly once, with every other element appearing 
at least twice, perhaps more.

Write a function that can find and return the element that appears exactly once.


* Examples:
    Input: [1,1,2,1]
    Output: 2

    Input: [1,2,1,2,1,2,80]
    Output: 80


* Note: You should be able to develop a solution that has O(n) time complexity.
"""

# init a new 'seen nums' dict
# loop through input
# check if num is in the seen dict
    # if it is, if the value is true, change to false
    # if the fvalue is false, pass
# if not add to seen nums dict and set to tru (true == only appears once)

# use a second loop and return the key whose value is True

def csFindTheSingleNumber(nums):
    seen_nums = dict()

    for num in nums:
        if num in seen_nums.keys():
            seen_nums[num] = False
        else:
            seen_nums[num] = True

    
    for key in seen_nums.keys():
        if seen_nums[key] == True:
            return key
    
    return None



print("\nExercise 1:")
nums = [2, 2, -3, 2]
print(csFindTheSingleNumber(nums))

nums = [1,1,9,1,2,3,4,4,5,3,4,9,6,5,2]
print(csFindTheSingleNumber(nums))

nums = [0, 1, 0, 1, 0, 1, 99]
print(csFindTheSingleNumber(nums))