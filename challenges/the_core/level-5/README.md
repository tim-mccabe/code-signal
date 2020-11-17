# Overview of all Functions

## Create Array

Given an integer size, return array of length size filled with 1s.

#### Example

For size = 4, the output should be
createArray(size) = [1, 1, 1, 1].

#### Input/Output

* **[input] integer size**

A positive integer.

Guaranteed constraints:
1 ≤ size ≤ 1000.

* **[output] array.integer**

## Arraye Replace

Given an array of integers, replace all the occurrences of elemToReplace with substitutionElem.

#### Example

For inputArray = [1, 2, 1], elemToReplace = 1, and substitutionElem = 3, the output should be
arrayReplace(inputArray, elemToReplace, substitutionElem) = [3, 2, 3].

#### Input/Output

* **[input] array.integer inputArray**

Guaranteed constraints:
0 ≤ inputArray.length ≤ 104,
0 ≤ inputArray[i] ≤ 109.

* **[input] integer elemToReplace**

Guaranteed constraints:
0 ≤ elemToReplace ≤ 109.

* **[input] integer substitutionElem**

Guaranteed constraints:
0 ≤ substitutionElem ≤ 109.

* **[output] array.integer**

## First Reverse Try

Reversing an array can be a tough task, especially for a novice programmer. Mary just started coding, so she would like to start with something basic at first. Instead of reversing the array entirely, she wants to swap just its first and last elements.

Given an array arr, swap its first and last elements and return the resulting array.

#### Example

For arr = [1, 2, 3, 4, 5], the output should be
firstReverseTry(arr) = [5, 2, 3, 4, 1].

#### Input/Output

* **[input] array.integer arr**

Guaranteed constraints:
0 ≤ arr.length ≤ 50,
-104 ≤ arr[i] ≤ 104.

* **[output] array.integer**

Array arr with its first and its last elements swapped.

## Concatenate Arrays

Given two arrays of integers `a` and `b`, obtain the array formed by the elements of `a` followed by the elements of `b`.

#### Example

For `a = [2, 2, 1]` and `b = [10, 11]`, the output should be
`concatenateArrays(a, b) = [2, 2, 1, 10, 11]`.

#### Input/Output

* **[input] array.integer a**

Guaranteed constraints:
1 ≤ a.length ≤ 10,
1 ≤ a[i] ≤ 15.

* **[input] array.integer b**

Guaranteed constraints:
0 ≤ b.length ≤ 10,
1 ≤ b[i] ≤ 15.

* **[output] array.integer**
