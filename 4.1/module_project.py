
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


* UPER - Plan:
    - init a new dict
    - students id (scores[i][0]) as the key in dict
    - since student id is unique, we can be sure that there won't be any collisions

    - loop through input array
        - check if student is in dict yet
            - if so append score to students score array
        - else
            - create a new key-val pair for student in dict
            - init a new array
            - append score to array
            - set dict[scores[i][0]] = new_array (with the score held inside)
    
    - loop through the dict and check len of each score array
        - if scores count is greater than 5:
            - sort scores
            - get the sum of scores[-5]
    - if the student has less than 5 scores in dict[stu_id], append the score to values
    - otherwise compare new value to 5 values currently in dict for student
        - if the new value is less than all 5, pass
        - otherwise keep the new value and remove the min value
"""

def csAverageOfTopFive(scores):
    grade_book = dict()

    for i in range(len(scores)):
        stu_id = scores[i][0]
        grade = scores[i][1]

        if stu_id in grade_book:
            grade_book[stu_id].append(grade)
        else:
            stu_grades = [grade]
            grade_book[stu_id] = stu_grades


    averages = []
    
    for student in grade_book.keys():
        stu_grades = grade_book[student]

        if len(stu_grades) > 5:
            stu_grades.sort()
            stu_grades = stu_grades[-5:]


        grade_sum = sum(stu_grades)
        avg = (grade_sum // len(stu_grades))

        averages.append([student, avg])


    return averages



print("\nExercise 2:")
scores = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]] # expected: [[1,87],[2,88]]
print(csAverageOfTopFive(scores))

scores = []
print(csAverageOfTopFive(scores)) # expected: []

scores = [[1,2]]
print(csAverageOfTopFive(scores)) # expected: [[1,2]]

scores = [[1,96],[3,55],[2,66],[2,72],[1,82],[4,56],[1,59],[5,73],[2,93],[2,0],[2,76],[3,0]]
print(csAverageOfTopFive(scores)) # expected: [[1, 79], [3, 27], [2, 61], [4, 56], [5, 73]]