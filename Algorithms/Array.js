// NOTE: Working on it - will update as I learn

/*
Linear Search: Searches for an element by checking each element in the array one by one.
Given an array of integers and a target value, write a function to find the index of the target value. If the target value is not found, return -1.

Sample input: [1, 2, 3, 4, 5], 3
Sample output: 2
*/

function linearSearch(arr, target) {
  for (let i = 0; i <= arr.length; i++) {
    if (arr[i] == target) {
      return i;
    }
  }
  return -1;
}

console.log(linearSearch([1, 2, 3, 4, 5], 3));

/**
Bubble Sort: Repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.
Question: Implement bubble sort to sort an array of integers in ascending order.
Sample input: [64, 34, 25, 12, 22, 11, 90]
Sample output: [11, 12, 22, 25, 34, 64, 90]
 * 
 */

function bubbleSort(arr) {
  for (let i = 0; i < arr.length - 1; i++) {
    let swapped = false;
    for (let j = 0; j < arr.length - i - 1; j++) {
      if (arr[j] > arr[j + 1]) {
        [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
        swapped = true;
      }
    }
    if (!swapped) {
      break;
    }
  }
  return arr;
}

console.log(bubbleSort([64, 34, 25, 12, 22, 11, 90]));
