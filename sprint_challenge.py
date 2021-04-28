

""" Sprint 4 - Final Challenge """



"""
Exercise 1: Condense Linked List (task 1 of 3)

Given a linked list of integers, remove any nodes from the linked list that have values that have previously 
occurred in the linked list. Your function should return a reference to the head of the updated linked list.

* Example:

    Input: (3) -> (4) -> (3) -> (2) -> (6) -> (1) -> (2) -> (6) -> N
    Output: (3) -> (4) -> (2) -> (6) -> (1) -> N
    Explanation: The input list contains redundant nodes (3), (6), and (2), so those should be removed from the list.


* UPER - Plan:
    * keywords: return ref to head, remove duplicate values

    - start with a curr pointer to head of list
    - prev pointer as None
    - init an emtpy 'seen values' set
    - since the head will never be removed we can safely return head at end

    - iterate through list
    - at each node check if curr_value in seen nums
        - if it is we need to remove the node
        - use a temp pointer to store next node in list
        - set prev.next to temp
    - if not in seen nums, add to set and continue
    - update prev and curr to next nodes in list
"""

class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None

    def __repr__(self):
        return f"{self.value}->{self.next}"


def condense_linked_list(node):
    seen = set()
    curr = node
    prev = None

    while curr:
        temp = curr.next

        if curr.value in seen:
            curr = temp
            prev.next = curr
        else:
            seen.add(curr.value)    
            prev = curr
            curr = curr.next
        
    return node



a = ListNode(3)
b = ListNode(4)
c = ListNode(3)
d = ListNode(2)
e = ListNode(6)
f = ListNode(1)
g = ListNode(2)
h = ListNode(6)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g
g.next = h

print(condense_linked_list(a)) # expected: (3) -> (4) -> (2) -> (6) -> (1) -> N





"""
Exercise 2: First Non-Repeating Character (task 2 of 3)

Given a string s consisting of small English letters, find and return the first instance of a non-repeating 
character in it. If there is no such character, return '_'.


* Examples:
    For s = "abacabad", the output should be
    first_not_repeating_character(s) = 'c'.

    - There are 2 non-repeating characters in the string: 'c' and 'd'. Return c since it appears in the string first.


    For s = "abacabaabacaba", the output should be
    first_not_repeating_character(s) = '_'.

    - There are no characters in this string that do not repeat.


* UPER - Plan:
    - init empty dictionary
    - iterate through input and check if character in dict
    - if it is, iterate count += 1
    - else set count to 1

    - use second loop to iterate through string and reference if letter in dict has a value of 1
    - return first letter w/value of 1
    - return "_" if all characters are repeated
"""

def first_not_repeating_character(s):
    char_counts = {}

    for char in s:
        if char in char_counts.keys():
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    
    for char in s:
        if char_counts[char] == 1:
            return char
    
    return "_"



print(first_not_repeating_character("abacabad")) # expected: c
print(first_not_repeating_character("abacabaabacaba")) # expected: _
print(first_not_repeating_character("z")) # expected: z
print(first_not_repeating_character("bcb")) # expected: c
print(first_not_repeating_character("bcccccccb")) # expected: _
print(first_not_repeating_character("abcdefghijklmnopqrstuvwxyziflskecznslkjfabe")) # expected: d
print(first_not_repeating_character("bcccccccccccccyb")) # expected: y





"""
Exercise 3: Uncover Spy (task 3 of 3)

In a city-state of n people, there is a rumor going around that one of the n people is a spy for the 
neighboring city-state.

The spy, if it exists:
    - Does not trust anyone else.
    - Is trusted by everyone else (he's good at his job).
    - Works alone; there are no other spies in the city-state.

You are given a list of pairs, trust. Each trust[i] = [a, b] represents the fact that person a trusts person b.

If the spy exists and can be found, return their identifier. Otherwise, return -1.


* Examples:

    Input: n = 2, trust = [[1, 2]]
    Output: 2
    Explanation: Person 1 trusts Person 2, but Person 2 does not trust Person 1, so Person 2 is the spy.

    Input: n = 3, trust = [[1, 3], [2, 3]]
    Output: 3
    Explanation: Person 1 trusts Person 3, and Person 2 trusts Person 3, but Person 3 does not trust either 
    Person 1 or Person 2. Thus, Person 3 is the spy.

    Input: n = 3, trust = [[1, 3], [2, 3], [3, 1]]
    Output: -1
    Explanation: Person 1 trusts Person 3, Person 2 trusts Person 3, and Person 3 trusts Person 1. Since everyone 
    trusts at least one other person, there is no spy.

    Input: n = 3, trust = [[1, 2], [2, 3]]
    Output: -1
    Explanation: Person 1 trusts Person 2, and Person 2 trusts Person 3. However, in this situation, we don't have 
    any one person who is trusted by everyone else. So we can't determine who the spy is in this case.

    Input: n = 4, trust = [[1, 3],[1, 4],[2, 3],[2, 4],[4, 3]]
    Output: 3
    Explanation: Person 1 trusts Person 3 and Person 4, Person 2 trusts Person 3 and Person 4, Person 4 trusts Person 3. 
    Since everyone trusts Person 3 but Person 3 does not trust anyone, they are the spy.
"""

def uncover_spy(n, trust):
    pass