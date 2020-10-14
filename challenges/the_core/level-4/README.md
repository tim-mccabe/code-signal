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

## Magical Well

You are standing at a magical well. It has two positive integers written on it: a and b. Each time you cast a magic marble into the well, it gives you a * b dollars and then both a and b increase by 1. You have n magic marbles. How much money will you make?

#### Example

For a = 1, b = 2, and n = 2, the output should be
magicalWell(a, b, n) = 8.

You will cast your first marble and get $2, after which the numbers will become 2 and 3. When you cast your second marble, the well will give you $6. Overall, you'll make $8. So, the output is 8.

#### Input/Output

* **[input] integer a**

Guaranteed constraints:
1 ≤ a ≤ 2000.

* **[input] integer b**

Guaranteed constraints:
1 ≤ b ≤ 2000.

* **[input] integer n**

The number of magic marbles in your possession, a non-negative integer.

Guaranteed constraints:
0 ≤ n ≤ 5.

* **[output] integer**