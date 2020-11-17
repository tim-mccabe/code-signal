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

## Remove Array Part

Remove a part of a given array between given 0-based indexes `l` and `r` (inclusive).

#### Example

For `inputArray = [2, 3, 2, 3, 4, 5]`, `l = 2`, and `r = 4`, the output should be
`removeArrayPart(inputArray, l, r) = [2, 3, 5]`.

#### Input/Output

* **[input] array.integer inputArray**

Guaranteed constraints:
2 ≤ inputArray.length ≤ 104,
-105 ≤ inputArray[i] ≤ 105.

* **[input] integer l**

Left index of the part to be removed (0-based).

Guaranteed constraints:
0 ≤ l ≤ r.

* **[input] integer r**

Right index of the part to be removed (0-based).

Guaranteed constraints:
l ≤ r < inputArray.length.

* **[output] array.integer**

## Is Smooth?

We define the *middle* of the array `arr` as follows:

* if `arr` contains an odd number of elements, its *middle* is the element whose index number is the same when counting from the beginning of the array and from its end;
* if `arr` contains an even number of elements, its *middle* is the sum of the two elements whose index numbers when counting from the beginning and from the end of the array differ by one.
An array is called *smooth* if its first and its last elements are equal to one another and to the *middle*. Given an array `arr`, determine if it is *smooth* or not.

#### Example

* For `arr = [7, 2, 2, 5, 10, 7]`, the output should be
  `isSmooth(arr) = true`.

  The first and the last elements of `arr` are equal to `7`, and its *middle* also equals `2 + 5 = 7`. Thus, the array is *smooth* and the output is `true`.

* For `arr = [-5, -5, 10]`, the output should be
  `isSmooth(arr) = false`.

  The first and *middle* elements are equal to `-5`, but the last element equals `10`. Thus, `arr` is not *smooth* and the output is `false`.

#### Input/Output

* **[input] array.integer arr**

The given array.

Guaranteed constraints:
2 ≤ arr.length ≤ 105,
-109 ≤ arr[i] ≤ 109.

* **[output] boolean**

`true` if `arr` is *smooth*, `false` otherwise.
