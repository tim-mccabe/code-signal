# Overview of all Functions

## House Numbers Sum

A boy is walking a long way from school to his home. To make the walk more fun he decides to add up all the numbers of the houses that he passes by during his walk. Unfortunately, not all of the houses have numbers written on them, and on top of that the boy is regularly taking turns to change streets, so the numbers don't appear to him in any particular order.

At some point during the walk the boy encounters a house with number `0` written on it, which surprises him so much that he stops adding numbers to his total right after seeing that house.

For the given sequence of houses determine the sum that the boy will get. It is guaranteed that there will always be at least one `0` house on the path.

#### Example

For `inputArray = [5, 1, 2, 3, 0, 1, 5, 0, 2]`, the output should be
`houseNumbersSum(inputArray) = 11`.

The answer was obtained as `5 + 1 + 2 + 3 = 11`.

#### Input/Output

* **[input] array.integer inputArray**

Guaranteed constraints:
5 ≤ inputArray.length ≤ 10,
0 ≤ inputArray[i] ≤ 10.

* **[output] integer**

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

## House of Cats

There are some people and cats in a house. You are given the number of legs they have all together. Your task is to return an array containing every possible number of people that could be in the house sorted in *ascending order*. It's guaranteed that each person has `2` legs and each cat has `4` legs.

#### Example

* For `legs = 6`, the output should be
  `houseOfCats(legs) = [1, 3]`.

  There could be either `1` cat and `1` person (`4 + 2 = 6`) or `3` people (`2 * 3 = 6`).

* For `legs = 2`, the output should be
  `houseOfCats(legs) = [1]`.

  There can be only 1 person.

#### Input/Output

* **[input] integer legs**

The total number of legs in the house. It's guaranteed,that this number is even.

Guaranteed constraints:
0 ≤ legs < 50.

* **[output] array.integer**

Every possible number of people that can be in the house.