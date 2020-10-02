# Overview of all functions 

## Alternating Sums

Several people are standing in a row and need to be divided into two teams. The first person goes into team 1, the second goes into team 2, the third goes into team 1 again, the fourth into team 2, and so on.

You are given an array of positive integers - the weights of the people. Return an array of two integers, where the first element is the total weight of team 1, and the second element is the total weight of team 2 after the division is complete.

#### Example

For a = [50, 60, 60, 45, 70], the output should be
alternatingSums(a) = [180, 105].

#### Input/Output

* **[execution time limit] 4 seconds (py3)**

* **[input] array.integer a**

Guaranteed constraints:
1 ≤ a.length ≤ 105,
45 ≤ a[i] ≤ 100.

* **[output] array.integer**

## Add Border

Given a rectangular matrix of characters, add a border of asterisks(*) to it.

#### Example

For

picture = ["abc",
           "ded"]
the output should be

addBorder(picture) = ["*****",
                      "*abc*",
                      "*ded*",
                      "*****"]
#### Input/Output

* **[execution time limit] 4 seconds (py3)**

* **[input] array.string picture**

A non-empty array of non-empty equal-length strings.

Guaranteed constraints:
1 ≤ picture.length ≤ 100,
1 ≤ picture[i].length ≤ 100.

* **[output] array.string**

The same matrix of characters, framed with a border of asterisks of width 1.