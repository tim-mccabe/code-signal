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

## Square Digits Sequence

Consider a sequence of numbers `a0`, `a1`, ..., `an`, in which an element is equal to the sum of squared digits of the previous element. The sequence ends once an element that has already been in the sequence appears again.

Given the first element `a0`, find the length of the sequence.

#### Example

* For `a0 = 16`, the output should be
  `squareDigitsSequence(a0) = 9`.

  Here's how elements of the sequence are constructed:

  * `a0 = 16`
  * `a1 = 12 + 62 = 37`
  * `a2 = 32 + 72 = 58`
  * `a3 = 52 + 82 = 89`
  * `a4 = 82 + 92 = 145`
  * `a5 = 12 + 42 + 52 = 42`
  * `a6 = 42 + 22 = 20`
  * `a7 = 22 + 02 = 4`
  * `a8 = 42 = 16`, which has already occurred before (`a0`)
  Thus, there are `9` elements in the sequence.

* For `a0 = 103`, the output should be
  `squareDigitsSequence(a0) = 4`.

  The sequence goes as follows: `103 -> 10 -> 1 -> 1`, `4` elements altogether.

#### Input/Output

* **[input] integer a0**

  First element of a sequence, positive integer.

  Guaranteed constraints:
  1 ≤ a0 ≤ 105.

* **[output] integer**