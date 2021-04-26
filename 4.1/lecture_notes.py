

""" Sprint 4.1 Lecture Notes - Hash Tables I """



"""
* Hash Table Basics:
    - great for searches if we know the key
    - one of most common data structures
        - dictionaries and sets built on top of hash tables
    - uses a hash fxn to get/store/delete values in O(1) time
    - uses a list to store values
    - use modulo to get an index within the bounds of values list
    - overall idea in hashing is to scramble input and turn into a index in underlying list
    

    * hashing functions:
        - take in a variable input
            - typically a string
        - deterministic
            - same input always has same resulting output
        - good hashing fxns have minimal duplication of output values
            - want our output to be distributed across a wide range of values
        - hashing should always be constant time to get value for key
"""




"""
Exercise 1: "705. Design HashSet" (https://leetcode.com/problems/design-hashset/)

Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:
    - void add(key) Inserts the value key into the HashSet.
    - bool contains(key) Returns whether the value key exists in the HashSet or not.
    - void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.
 

* Example:
    - Input:
        ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
        [[], [1], [2], [1], [3], [2], [2], [2], [2]]
    
    - Output:
        [null, null, null, true, false, null, true, null, false]

    - Explanation:
        MyHashSet myHashSet = new MyHashSet();
        myHashSet.add(1);      // set = [1]
        myHashSet.add(2);      // set = [1, 2]
        myHashSet.contains(1); // return True
        myHashSet.contains(3); // return False, (not found)
        myHashSet.add(2);      // set = [1, 2]
        myHashSet.contains(2); // return True
        myHashSet.remove(2);   // set = [1]
        myHashSet.contains(2); // return False, (already removed)
"""

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        pass

    def add(self, key: int) -> None:
        pass

    def remove(self, key: int) -> None:
        pass

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        pass