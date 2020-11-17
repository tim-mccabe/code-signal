# Overview of all Functions

## Is Power?

Determine if the given number is a power of some non-negative integer.

#### Example

* For `n = 125`, the output should be
  `isPower(n) = true`;
* For `n = 72`, the output should be
  `isPower(n) = false`.
#### Input/Output

* **[input] integer n**

A positive integer.

Guaranteed constraints:
1 ≤ n ≤ 400.

* **[output] boolean**

`true` if `n` can be represented in the form `ab` (`a` to the power of `b`) where `a` and `b` are some non-negative integers and `b ≥ 2`, false otherwise.

## Is Sum of Consecutive 2

Find the number of ways to express `n` as sum of some (at least two) consecutive positive integers.

#### Example

* For `n = 9`, the output should be
  `isSumOfConsecutive2(n) = 2`.

  There are two ways to represent `n = 9`: `2 + 3 + 4 = 9 and 4 + 5 = 9`.

* For `n = 8`, the output should be
  `isSumOfConsecutive2(n) = 0`.

  There are no ways to represent `n = 8`.

#### Input/Output

* **[input] integer n**

A positive integer.

Guaranteed constraints:
1 ≤ n ≤ 104.

* **[output] integer**