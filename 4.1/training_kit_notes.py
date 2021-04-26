

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




"""
Objective 2: Describe and Implement Hash Tables


* Basics
    - hash tables will take a key and hash it, then map the value to an index

        hashing function + values array = hash table


    * example: create a basic hashing function
        - we can use pythons ".encode()" method to get byte representation of a string
        - each character will be represented by a int
        - get sum of all characters and then conert it to an index using the mod operator (%)
        - returned value will be the index that a given input string maps to in hash table
"""

def my_hasher(input_string, table_size):

    byte_repr = input_string.encode()

    sum = 0
    for byte in byte_repr:
        sum += byte

    return sum % table_size


print("\nExample of a Basic Hashing Function")
print(my_hasher("hello", 10))




"""
Objective 3: Implement a User Defined Hash Table Class

We define a hash table as an empty array and hash function as a function that takes a value and converts it into an array 
index where you will store that value. Let's put the two together. Let's implement a HashTable class where we can:
    - insert values into a hash table
    - retrieve values from a hash table
    - delete values from a hash table
"""

# basic hash table class blueprint (does not handle collisions!)
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.item_count = 0


    def get_num_slots(self):
        # not number of items in table, but number of slots in main list
        return len(self.storage)


    def djb2_hasher(self, key):
        # DJB2 Hash fxn, 32 bit

        # cast key to string and get bytes
        str_key = str(key).encode()

        # start w/arbitrary large prime
        hash_val = 5381

        # bit-shift and sum val of each character
        for byte in str_key:
            hash_val = ((hash_val << 5) + hash_val) + byte
            hash_val &= 0xffffffff   # only keep 32 bits

        return hash_val

    
    def hash_index(self, key):
        # use hasher func to map key to an index in storage array
        return self.djb2_hasher(key) % self.capacity

    
    def put(self, key, value):
        # update to handle collisions later
        index = self.hash_index(key)

        self.storage[index] = value
        return


    def delete(self, key, value):
        #  update to handle collisions later
        index = self.hash_index(key)
        self.storage[index] = None

    
    def get(self, key):
        index = self.hash_index(key)
        return self.storage[index]