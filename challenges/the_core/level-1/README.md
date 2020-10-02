# Overview of all functions 

## Add Two Digits

You are given a two-digit integer n. Return the sum of its digits.

#### Example

For n = 29, the output should be
addTwoDigits(n) = 11.

#### Input/Output

* **[input] integer n**

A positive two-digit integer.

Guaranteed constraints:
10 ≤ n ≤ 99.

* **[output] integer**

The sum of the first and second digits of the input number.

## Largest Number

Given an integer n, return the largest number that contains exactly n digits.

#### Example

For n = 2, the output should be
largestNumber(n) = 99.

#### Input/Output

* **[input] integer n**

Guaranteed constraints:
1 ≤ n ≤ 9.

* **[output] integer**

The largest integer of length n.

## Candies

n children have got m pieces of candy. They want to eat as much candy as they can, but each child must eat exactly the same amount of candy as any other child. Determine how many pieces of candy will be eaten by all the children together. Individual pieces of candy cannot be split.

#### Example

For n = 3 and m = 10, the output should be
candies(n, m) = 9.

Each child will eat 3 pieces. So the answer is 9.

#### Input/Output

* **[input] integer n**

The number of children.

Guaranteed constraints:
1 ≤ n ≤ 10.

* **[input] integer m**

The number of pieces of candy.

Guaranteed constraints:
2 ≤ m ≤ 100.

* **[output] integer**

The total number of pieces of candy the children will eat provided they eat as much as they can and all children eat the same amount.