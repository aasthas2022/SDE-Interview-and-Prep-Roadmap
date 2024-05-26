# NOTE: Working on it - will update as I learn

'''
Linear Search: Searches for an element by checking each element in the array one by one.

Given an array of integers and a target value, write a function to find the index of the target value. If the target value is not found, return -1.

Sample input: [1, 2, 3, 4, 5], 3
Sample output: 2
'''

## Approach 1 - Using len - range:
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

print(linear_search([1, 2, 3, 4, 5], 3)) # Outputs: 2
print(linear_search([1, 2, 3, 4, 5], 6)) # Outputs: -1

## Approach 2 - Using Enumerate:
def linear_search_1(arr, target):
    for index, val in enumerate(arr):
        if val == target:
            return index
    return -1


print(linear_search_1([1, 2, 3, 4, 5], 3)) # Outputs: 2
print(linear_search_1([1, 2, 3, 4, 5], 6)) # Outputs: -1
    
    
'''
Binary Search: Searches for an element in a sorted array by repeatedly dividing the search interval in half.
Question: Given a sorted array of integers and a target value, write a function to find the index of the target value using binary search. If the target value is not found, return -1.

'''

'''

TODO: 
1,2,3,4,5  - 4

len - 5 , half - 3, left - 1,2,3, right - 4,5
taget - 4, right
len - 2, half 1, left - 4, right - 5
'''

'''
Bubble Sort: Repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.
Question: Implement bubble sort to sort an array of integers in ascending order.
Sample input: [64, 34, 25, 12, 22, 11, 90]
Sample output: [11, 12, 22, 25, 34, 64, 90]
''' 
def bubbleSort(arr):
    for i in range(len(arr)-1):
        swapped = False
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                swapped = True
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if not swapped:
            break
    return arr
print(bubbleSort([64, 34, 25, 12, 22, 11, 90])) ## Output: [11, 12, 22, 25, 34, 64, 90]