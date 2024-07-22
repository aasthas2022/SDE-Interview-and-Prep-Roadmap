'''
Example 1: Given a string s, return true if it is a palindrome, false otherwise.

A string is a palindrome if it reads the same forward as backward. That means, after reversing it, it is still the same string. For example: "abcdcba", or "racecar".

'''
def palindrom(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
        
    return True
        

'''
125. Valid Palindrome - https://leetcode.com/problems/valid-palindrome/description/
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Input: s = "A man, a plan, a canal: Panama"
Output: true

Input: s = "race a car"
Output: false

Input: s = " "
Output: true
'''

def isPalindrome(s):
    s = ''.join(char for char in s if char.isalnum()).lower()
    left = 0
    right = len(s) - 1
    while left < right:
        if (s[left] != s [right]):
            return False
        left += 1
        right -=1
    return True


'''
1. Two Sum - https://leetcode.com/problems/two-sum/description/ but SORTED

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

def twoSum(nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
        sum = nums[left] + nums[right]
        if sum == target:
            return [left, right]
        elif sum > target:
            right -= 1
        else:
            left += 1
    return [-1, -1]

'''
Example: Given two sorted integer arrays arr1 and arr2, return a new array that combines both of them and is also sorted.
'''

def merged_sorted(arr1, arr2):
    i, j = 0, 0
    result = []
    while i < len(arr1) and j<len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
            
    while i<len(arr1):
        result.append(arr1[i])
        i += 1
    
    while j<len(arr2):
        result.append(arr2[j])
        j += 1
    return result

print(merged_sorted([1,2,5,6], [4,5,7,8]))