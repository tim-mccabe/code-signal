# Overview of all functions 

## All Longest Strings

Given an array of strings, return another array containing all of its longest strings.

#### Example

For `inputArray = ["aba", "aa", "ad", "vcd", "aba"]`, the output should be
`allLongestStrings(inputArray) = ["aba", "vcd", "aba"]`.

#### Input/Output

* **[input] array.string inputArray**

  A non-empty array.

  Guaranteed constraints:
  1 ≤ inputArray.length ≤ 10,
  1 ≤ inputArray[i].length ≤ 10.

* **[output] array.string**

  Array of the longest strings, stored in the same order as in the `inputArray`.

## Common Character Count

Given two strings, find the number of common characters between them.

#### Example

For `s1 = "aabcc"` and `s2 = "adcaa"`, the output should be
`commonCharacterCount(s1, s2) = 3`.

Strings have `3` common characters - `2` "a"s and `1` "c".

#### Input/Output

* **[input] string s1**

  A string consisting of lowercase English letters.

  Guaranteed constraints:
  1 ≤ s1.length < 15.

* **[input] string s2**

  A string consisting of lowercase English letters.

  Guaranteed constraints:
  1 ≤ s2.length < 15.

* **[output] integer**

## Is Lucky

Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

Given a ticket number `n`, determine if it's lucky or not.

#### Example

*  For `n = 1230`, the output should be
  `isLucky(n) = true`;
* For `n = 239017`, the output should be
  `isLucky(n) = false`.
#### Input/Output

* **[input] integer n**

  A ticket number represented as a positive integer with an even number of digits.

  Guaranteed constraints:
  10 ≤ n < 106.

* **[output] boolean**

  `true` if `n` is a lucky ticket number, `false` otherwise.

## Sort by Height

Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to rearrange the people by their heights in a non-descending order without moving the trees. People can be very tall!

#### Example

For `a = [-1, 150, 190, 170, -1, -1, 160, 180]`, the output should be
`sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190]`.

#### Input/Output

* **[input] array.integer a**

  If `a[i] = -1`, then the `ith` position is occupied by a tree. Otherwise `a[i]` is the height of a person standing in the `ith` position.

  Guaranteed constraints:
  1 ≤ a.length ≤ 1000,
  -1 ≤ a[i] ≤ 1000.

* **[output] array.integer**

  Sorted array `a` with all the trees untouched.

## Reverse in Parentheses

Write a function that reverses characters in (possibly nested) parentheses in the input string.

Input strings will always be well-formed with matching `()`s.

#### Example

* For `inputString = "(bar)"`, the output should be
  `reverseInParentheses(inputString) = "rab"`;
* For `inputString = "foo(bar)baz"`, the output should be
  `reverseInParentheses(inputString) = "foorabbaz"`;
* For `inputString = "foo(bar)baz(blim)"`, the output should be
  `reverseInParentheses(inputString) = "foorabbazmilb"`;
* For `inputString = "foo(bar(baz))blim"`, the output should be
  `reverseInParentheses(inputString) = "foobazrabblim"`.
  Because `"foo(bar(baz))blim"` becomes `"foo(barzab)blim"` and then `"foobazrabblim"`.
#### Input/Output

* **[input] string inputString**

  A string consisting of lowercase English letters and the characters `(` and `)`. It is guaranteed that all parentheses in `inputString` form a regular bracket sequence.

  Guaranteed constraints:
  0 ≤ inputString.length ≤ 50.

* **[output] string**

  Return `inputString`, with all the characters that were in parentheses reversed.