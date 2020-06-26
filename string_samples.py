# Python program to print all permutations with
# duplicates allowed

#from strop import count
from collections import Counter


def toString(List):
    return ''.join(List)


#def isAnagram():
    

#def isPalindrome():


#def firstNonRepeatedCharacter():


def reverseStringInPlace(s):
    str =''
    for i in s:
        str = i + str
    return str


def reverseStringInPlaceRecursive(s):
    if len(s) == 0:
        return s
    else:
        return reverseStringInPlaceRecursive(s[1:]) + s[0]


# Naive method
def count_characters(given_str):
    print('Count of characters 1')
    count = 0
    for i in given_str:
        if i == 'B':
            count +=1
    print('Count of character is : '+str(count))


# Naive method
def count_characters1(given_str):
    print('Count of characters 2')
    print(given_str.count('A'))


def count_characters2(given_str):
    print('Count of characters 2')
    count2 = Counter(given_str)
    print('Count of character is : '+str(count2['e']))


# Function to print permutations of string
# This function takes three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.
def permute(a, l, r):
    if l == r:
        print(toString(a))
    else:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]
            permute(a, l + 1, r)
            a[l], a[i] = a[i], a[l]  # backtrack


# Driver program to test the above function
str2 = "ABC"
permute(list(str2), 0, len(str2) - 1)
str1 = 'aaabbcaa'
count_characters(str1)
count_characters1(str1)
count_characters2(str1)

print('Reversed string by iterative way of  ' + str2 + ' is ' + reverseStringInPlace(str2))
print('Reversed string by recursive way of  ' + str2 + ' is ' + reverseStringInPlaceRecursive(str2))