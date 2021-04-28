

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
"""