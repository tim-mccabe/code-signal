# Overview of all Functions

## Count Bits

Implement a function that, given an integer n, uses a specific method on it and returns the number of bits in its binary representation.

*Note: in this task and most of the following tasks you will be given a code snippet with some part of it replaced by the ellipsis (...). Only this part is allowed to be changed.*

#### Example

For n = 50, the output should be
countBits(n) = 6.

5010 = 1100102, a number that consists of 6 digits. Thus, the output should be 6.

#### Input/Output

* **[input] integer n**

A positive integer.

Guaranteed constraints:
1 ≤ n ≤ 109.

* **[output] integer**

The number of bits in binary representation of n.

## Modulus

It frustrates you more than you'd like to admit that the modulus operator in Python can be applied to non-integer values. When you write code, you expect the result of the modulus operator to always be an integer, but thanks to Python this isn't always the case.

To fix this, you've decided to write your own modulus operator as a function. Your task is to implement a function that, given a number n, returns -1 if this number is not an integer and n % 2 otherwise. It is guaranteed that if the number represents an integer, it will be written without a decimal point.

#### Example

* For n = 15, the output should be
  modulus(n) = 1;

* For n = 23.12, the output should be
  modulus(n) = -1.

#### Input/Output

* **[input] numeric n**

A non-negative number that can be an int, a float, or a long.

Guaranteed constraints:
0 ≤ n ≤ 1000.

* **[output] integer**

Return n % 2 if n is an integer, otherwise return -1.

## Simple Sort

To understand how efficient the built-in Python sorting function is, you decided to implement your own simple sorting algorithm and compare its speed to the speed of the Python sorting. Write a function that, given an array of integers arr, sorts its elements in ascending order.

#### Example

For arr = [2, 4, 1, 5], the output should be
simpleSort(arr) = [1, 2, 4, 5].

#### Input/Output

* **[input] array.integer arr**

Guaranteed constraints:
1 ≤ arr.length ≤ 500,
-105 ≤ arr[i] ≤ 105.

* **[output] array.integer**

The given array with elements sorted in ascending order.

## Base Conversion

Your university professor decided to have a little fun and asked the class to implement a function that, given a number n and a base x, converts the number from base x to base 16. To make things more interesting, he announced that the first student to write the solution will have to answer fewer question than the rest of the class during the final exam.

Laughing devilishly, you asked if it was okay to use a language of your choice, and the unsuspecting professor answered "yes". It's settled then: Python is your language of choice!

Now you're bound to win. Implement a function that, given an integer number n and a base x, converts n from base x to base 16.

#### Example

For n = "1302" and x = 5, the output should be
baseConversion(n, x) = "ca".

Here's why:
13025 = 20210 = ca16.

#### Input/Output

* **[input] string n**

A valid non-negative integer in base x. The string is guaranteed to consist of digits and lowercase English letters.

Guaranteed constraints:
1 < n.length ≤ 10.

* **[input] integer x**

The base of n.

Guaranteed constraints:
2 ≤ x ≤ 36.

* **[output] string**

The value of n in base 16. The string should contain only digits and lowercase English letters 'a' - 'f'.

## Mex Function

You've just started to study impartial games, and came across an interesting theory. The theory is quite complicated, but it can be narrowed down to the following statements: solutions to all such games can be found with the *mex* function. *Mex* is an abbreviation of *minimum excludant:* for the given set s it finds the minimum non-negative integer that is not present in s.

You don't yet know how to implement such a function efficiently, so would like to create a simplified version. For the given set s and given an upperBound, implement a function that will find its *mex* if it's smaller than upperBound or return upperBound instead.

*Hint: for loops also have an else clause which executes when the loop completes normally, i.e. without encountering any breaks*

#### Example

* For s = [0, 4, 2, 3, 1, 7] and upperBound = 10,
  the output should be
  mexFunction(s, upperBound) = 5.

  5 is the smallest non-negative integer that is not present in s, and it is smaller than upperBound.

* For s = [0, 4, 2, 3, 1, 7] and upperBound = 3,
  the output should be
  mexFunction(s, upperBound) = 3.

  The minimum excludant for the given set is 5, but it's greater than upperBound, so the output should be 3.

#### Input/Output

* **[input] array.integer s**

Array of distinct non-negative integers.

Guaranteed constraints:
0 ≤ s.length ≤ 100,
0 ≤ s[i] ≤ 100.

* **[input] integer upperBound**

A positive integer.

Guaranteed constraints:
1 ≤ upperBound ≤ 100.

* **[output] integer**

Mex of s if it's smaller than upperBound, or upperBound instead.