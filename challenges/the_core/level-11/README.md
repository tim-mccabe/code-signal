# Overview of all Functions

## Array Conversion

Given an array of `2k` integers (for some integer `k`), perform the following operations until the array contains only one element:

* On the `1st`, `3rd`, `5th`, etc. iterations (1-based) replace each pair of consecutive elements with their sum;
* On the `2nd`, `4th`, `6th`, etc. iterations replace each pair of consecutive elements with their product.

After the algorithm has finished, there will be a single element left in the array. Return that element.

#### Example

For `inputArray = [1, 2, 3, 4, 5, 6, 7, 8]`, the output should be
`arrayConversion(inputArray) = 186`.

We have `[1, 2, 3, 4, 5, 6, 7, 8] -> [3, 7, 11, 15] -> [21, 165] -> [186]`, so the answer is `186`.

#### Input/Output

* **[input] array.integer inputArray**

Guaranteed constraints:
1 ≤ inputArray.length ≤ 27,
-100 ≤ inputArray[i] ≤ 100.

* **[output] integer**

## Array Previous Less

Given array of integers, for each position `i`, search among the previous positions for the last (from the left) position that contains a smaller value. Store this value at position `i` in the answer. If no such value can be found, store `-1` instead.

#### Example

For `items = [3, 5, 2, 4, 5]`, the output should be
`arrayPreviousLess(items) = [-1, 3, -1, 2, 4]`.

#### Input/Output

* **[input] array.integer items**

Non-empty array of positive integers.

Guaranteed constraints:
3 ≤ items.length ≤ 15,
1 ≤ items[i] ≤ 200.

* **[output] array.integer**

Array containing answer values computed as described above.