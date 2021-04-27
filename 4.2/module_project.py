
""" Sprint 4.2: Hash Tables II - CodeSignal Assignment """



"""
Exercise 1: Isomorphic Strings (task 3 of 5)

Given two strings a and b, determine if they are isomorphic.
Two strings are isomorphic if the characters in 'a' can be replaced to get 'b'.

All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character but a character may map to itself.


* Examples:

    1.  Input: 
            a = "odd"
            b = "egg"

        Output: true


    2.  Input:
            a = "foo"
            b = "bar"

        Output: false


    3.  Input:
            a = "abca"
            b = "zbxz"

        Output: true


    4.  Input:
            a = "abc"
            b = ""

        Output: false


* UPER - Plan:
    requirements for isomorphic strings:
        - string 'a' and string 'b' must be same length
        - any letter change must apply to all of the same letter in original string
            - i.e. if letter 'l' -> 's', all 'l' in string 1 must become 's' in string 2
        - a letter can remain unchanged
            - i.e. same letter can map to itself, as long as the above req. is met

        - first check if strings are same length, otherwise return
        - init a new empty dictionary
            - key = char in string a, value = char in string b
            - {char_a: char_b}
        - use loop for i in range of len(a)
        - check if char_a is in dict
            - if so, ensure that the value for char_a maps to char_b
                - terminate early and return false if not
        - else, set dict[char_a] = char_b
        - if the loop completes, return true
"""

def csIsomorphicStrings(a, b):
    if len(a) != len(b):
        return False

    iso = dict()

    for i in range(len(a)):
        char_a = a[i]
        char_b = b[i]

        if char_a in iso.keys():
            if iso[char_a] != char_b:
                return False
        else:
            iso[char_a] = char_b


    return True



print("\nExercise 1:")
print(csIsomorphicStrings("", "")) # expected: True
print(csIsomorphicStrings("a", "")) # expected: False
print(csIsomorphicStrings("aaa", "aaa")) # expected: True
print(csIsomorphicStrings("aaa", "bbb")) # expected: True
print(csIsomorphicStrings("odd", "egg")) # expected: True
print(csIsomorphicStrings("foo", "bar")) # expected: False
print(csIsomorphicStrings("abca", "zbxz")) # expected: True
print(csIsomorphicStrings("abc", "")) # expected: False





"""
Exercise 2: Word Pattern (task 4 of 5)

Given a pattern and a string 'a', find if 'a' follows the same pattern.

Here, to "follow" means a full match, such that there is a one-to-one correspondence between a 
letter in pattern and a non-empty word in 'a'.


* Examples:
    1.  Input:
        pattern = "abba"
        a = "lambda school school lambda"

        Output: true

    2.  Input:
        pattern = "abba"
        a = "lambda school school coding"

        Output: false

    3.  Input:
        pattern = "aaaa"
        a = "lambda school school lambda"

        Output: false

    4.  Input:
        pattern = "abba"
        a = "lambda lambda lambda lambda"

        Output: false


* Notes:
    - pattern contains only lower-case English letters.
    - a contains only lower-case English letters and spaces ' '.
    - a does not contain any leading or trailing spaces.
    - All the words in a are separated by a single space.
"""

def csWordPattern(pattern, a):
    pass