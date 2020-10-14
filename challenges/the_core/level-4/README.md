# Overview of all Functions

## Least Factorial

Given an integer n, find the minimal k such that

* k = m! (where m! = 1 * 2 * ... * m) for some integer m;
* k >= n.
In other words, find the smallest factorial which is not less than n.

#### Example

For n = 17, the output should be
leastFactorial(n) = 24.

17 < 24 = 4! = 1 * 2 * 3 * 4, while 3! = 1 * 2 * 3 = 6 < 17).

#### Input/Output

* **[input] integer n**

A positive integer.

Guaranteed constraints:
1 ≤ n ≤ 120.

* **[output] integer**

## Count Sum of Two Representations 2

Given integers n, l and r, find the number of ways to represent n as a sum of two integers A and B such that l ≤ A ≤ B ≤ r.

#### Example

For n = 6, l = 2, and r = 4, the output should be
countSumOfTwoRepresentations2(n, l, r) = 2.

There are just two ways to write 6 as A + B, where 2 ≤ A ≤ B ≤ 4: 6 = 2 + 4 and 6 = 3 + 3.

#### Input/Output

* **[input] integer n**

A positive integer.

Guaranteed constraints:
5 ≤ n ≤ 109.

* **[input] integer l**

A positive integer.

Guaranteed constraints:
1 ≤ l ≤ r.

* **[input] integer r**

A positive integer.

Guaranteed constraints:
l ≤ r ≤ 109,
r - l ≤ 106.

* **[output] integer**