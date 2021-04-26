
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





"""
Exercise 2: Average of Top Five (task 5 of 6)

Given a list of different students' scores, write a function that returns the average of each student's top five 
scores. You should return the averages in ascending order of the students' id numbers.

Each entry (scores[i]) has the student's id number (scores[i][0]) and the student's score (scores[i][1]). The 
averages should be calculated using integer division.


* Example:
    Input: [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]

    Output: [[1,87],[2,88]]

    Explanation:
        The average student `1` is `87`.
        The average of student `2` is `88.6`, but with integer division is `88`.


* Notes:
    The score of the students is between 1 and 100.
"""