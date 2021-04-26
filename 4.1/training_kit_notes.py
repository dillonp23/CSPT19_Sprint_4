

""" Sprint 4.1 Training Kit Notes - Hash Tables I """



"""
Objective 1: Time & Space Complexity, Strengths & Weaknesses, and Common Uses


* Hash Tables:
    - data structures that map to key/value pairs
    - extremely efficient lookups if you know the key
        - constant-time operation lookups with key
    - may also be called:
        - "hash maps"
        - "dictionaries"
        - "maps"
        - "unordered maps"


* Time & Space Complexity:

    * Lookups - O(1)
        - average case, but can be O(n) in worst case
        - worst-case happens when there is a hash collision
            - two keys hash to same index


    * Insertions - O(1)
        - like lookups, the worst case could be O(n) with a hash collision


    * Deletions - O(1)
        - like lookups, the worst case could be O(n) with a hash collision


    * Space Complexity - O(n)
        - each key-value pair takes up space in memory


* Strengths:
    - avg. case lookup in constant time
        - great solution when you'll be performing many lookups
    - allow any hashable object to be a key
        - i.e. allows a wide range of uses to map a key to value


* Weaknesses:
    - mapping only goes one way
        - knowing a key is incredibly efficient to find its value
        - but knowing the value and needing to find the key is not efficient
    - hash tables with many collisions causes the complexity to increase
        - w/hash collisions a linked list is used to store the values corresponding to the key
        - if there are many collisions, & many linked lists, we get inefficient time complexity


* Hash Collisions:
    - theoretically no perfect hashing function
    - need a strategy to deal with collisions
        - can't have table overwrite pre-existing values
    - most common solution is to use a linked list
    - each index in the values array holds the single value for key, or a linked list of values
        - each node of list would hold a key, value, and reference to next node
    - worst case situation would be all values map to same index
        - i.e. all values would be stored as a single linked list held at an index of values array
        - so worst case scenario, has same efficiency as a linked list
"""