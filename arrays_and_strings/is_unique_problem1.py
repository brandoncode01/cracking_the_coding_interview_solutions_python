""" 
Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you 
    cannot use additional data structures? 
    
    Thought process
    
    APPROACH 1 -> using dictionary
    
    One possible solution to this problem could be using a dictionary (also known as hashmap in the book)
    as soon as we detect that a character occurs more than one return False you can see the implementation
    in the method is_unique_ap
    
    Time Complexity = O(n)
    Space Complexity = O(n)
    ---------------------------
    
    APPROACH 2 -> using array with bit manipulation    

    This third approach is using an array with length of 26(English alphabet consist of 26 character)
    convert every character into int and increment it's integer representation by 1

    Time Complexity = O(n)
    Space Complexity = O(n)
    --------------------------
    
    APPROACH 3 -> sorting the characters
    The problem also asks what if you cannot use additional data structures? In that case we can sort the data 
    structure and return as soon as we find that two characters are equals by comparing current caracter with previous
    Time Complexity = O(nlogn)
    Space Complexity = O(1)

"""
from collections import defaultdict

def is_unique_map(s_str:str) -> bool:
    count = defaultdict(int) # as an alternative you can define {} and validate it inside the for loop
    
    for char in s_str:
        count[char] += 1 # Increment current character by 1
        if count[char] > 1: return False # If curr char appears more tha once return False
        
        
    return True # no more than 1 occurrence appear so return True


def is_unique_bit(s_str:str) -> bool:
    count = [0] * 26 # Initially 0 character for every element in the alphabet
    for char in s_str:
        count[ord(char) - ord('a')] += 1 # get the integer representation of current character
        
        if count[ord(char)- ord('a')] > 1: return False # if appears more than one return False
        
    return True



def is_unique_sorting(s_str:str) -> bool:
    s_str = sorted(list(s_str)) # create string as list and sort the list of characters
    for i in  range(1, len(s_str)):
        if s_str[i] == s_str[i-1]: # when two same characters are found return False
            return False
    return True



#------------------------------------------  TEST CASES -------------------------------------
def testcases():
    approaches = [is_unique_map, is_unique_bit, is_unique_sorting]
    strings = ['abc', '', 'aaaa', 'aba', 'bbbc', 'abcde', 'a', 'b', 'abcdewc']
    expected = [True, True, False, False, False, True, True, True, False]
    
    for i in range(len(approaches)):
        for j in range(len(strings)):
            assert approaches[i](strings[j]) == expected[j], f' Approach {i+1} failed on string {j+1} -> {strings[j]}'
            print(f"test case {i+1} with string {j+1} passed.")
    
    print("All test cases passed!")

testcases()