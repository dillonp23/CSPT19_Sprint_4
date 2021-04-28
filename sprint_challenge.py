

""" Sprint 4 - Final Challenge """



"""
Exercise 1: Condense Linked List (task 1 of 3)

Given a linked list of integers, remove any nodes from the linked list that have values that have previously 
occurred in the linked list. Your function should return a reference to the head of the updated linked list.

* Example:

    Input: (3) -> (4) -> (3) -> (2) -> (6) -> (1) -> (2) -> (6) -> N
    Output: (3) -> (4) -> (2) -> (6) -> (1) -> N
    Explanation: The input list contains redundant nodes (3), (6), and (2), so those should be removed from the list.
"""

class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None


def condense_linked_list(node):
    pass