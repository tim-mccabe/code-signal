# Overview of all Functions

# Extract Each Kth

Given array of integers, remove each kth element from it.

#### Example

For inputArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] and k = 3, the output should be
extractEachKth(inputArray, k) = [1, 2, 4, 5, 7, 8, 10].

#### Input/Output

* **[input] array.integer inputArray**

Guaranteed constraints:
5 ≤ inputArray.length ≤ 15,
-20 ≤ inputArray[i] ≤ 20.

* **[input] integer k**

Guaranteed constraints:
1 ≤ k ≤ 10.

* **[output] array.integer**

inputArray without elements k - 1, 2k - 1, 3k - 1 etc.

## First Digit

Find the leftmost digit that occurs in a given string.

#### Example

* For inputString = "var_1__Int", the output should be
  firstDigit(inputString) = '1';
* For inputString = "q2q-q", the output should be
  firstDigit(inputString) = '2';
* For inputString = "0ss", the output should be
  firstDigit(inputString) = '0'.
#### Input/Output

* **[input] string inputString**

A string containing at least one digit.

Guaranteed constraints:
3 ≤ inputString.length ≤ 10.

* **[output] char**

## Different Symbols Naive

Given a string, find the number of different characters in it.

#### Example

For s = "cabca", the output should be
differentSymbolsNaive(s) = 3.

There are 3 different characters a, b and c.

#### Input/Output

* **[input] string s**

A string of lowercase English letters.

Guaranteed constraints:
3 ≤ s.length ≤ 1000.

* **[output] integer**