# Overview of all Functions

## Reach Next Level

You are playing an RPG game. Currently your experience points (XP) total is equal to experience. To reach the next level your XP should be at least at threshold. If you kill the monster in front of you, you will gain more experience points in the amount of the reward.

Given values experience, threshold and reward, check if you reach the next level after killing the monster.

#### Example

* For experience = 10, threshold = 15, and reward = 5, the output should be
  reachNextLevel(experience, threshold, reward) = true;
* For experience = 10, threshold = 15, and reward = 4, the output should be
  reachNextLevel(experience, threshold, reward) = false.
#### Input/Output

* **[input] integer experience**

Guaranteed constraints:
3 ≤ experience ≤ 250.

* **[input] integer threshold**

Guaranteed constraints:
5 ≤ threshold ≤ 300.

* **[input] integer reward**

Guaranteed constraints:
2 ≤ reward ≤ 65.

* **[output] boolean**

true if you reach the next level, false otherwise.

## Knapsack Light

You found two items in a treasure chest! The first item weighs weight1 and is worth value1, and the second item weighs weight2 and is worth value2. What is the total maximum value of the items you can take with you, assuming that your max weight capacity is maxW and you can't come back for the items later?

Note that there are only two items and you can't bring more than one item of each type, i.e. you can't take two first items or two second items.

#### Example

* For value1 = 10, weight1 = 5, value2 = 6, weight2 = 4, and maxW = 8, the output should be
  knapsackLight(value1, weight1, value2, weight2, maxW) = 10.

  You can only carry the first item.

* For value1 = 10, weight1 = 5, value2 = 6, weight2 = 4, and maxW = 9, the output should be
  knapsackLight(value1, weight1, value2, weight2, maxW) = 16.

  You're strong enough to take both of the items with you.

* For value1 = 5, weight1 = 3, value2 = 7, weight2 = 4, and maxW = 6, the output should be
  knapsackLight(value1, weight1, value2, weight2, maxW) = 7.

  You can't take both items, but you can take any of them.

#### Input/Output

* [input] integer value1

Guaranteed constraints:
2 ≤ value1 ≤ 20.

* [input] integer weight1

Guaranteed constraints:
2 ≤ weight1 ≤ 10.

* [input] integer value2

Guaranteed constraints:
2 ≤ value2 ≤ 20.

* [input] integer weight2

Guaranteed constraints:
2 ≤ weight2 ≤ 10.

* [input] integer maxW

Guaranteed constraints:
1 ≤ maxW ≤ 20.

* [output] integer

## Extra Number

You're given three integers, a, b and c. It is guaranteed that two of these integers are equal to each other. What is the value of the third integer?

#### Example

For a = 2, b = 7, and c = 2, the output should be
extraNumber(a, b, c) = 7.

The two equal numbers are a and c. The third number (b) equals 7, which is the answer.

#### Input/Output

* [input] integer a

Guaranteed constraints:
1 ≤ a ≤ 109.

* [input] integer b

Guaranteed constraints:
1 ≤ b ≤ 109.

* [input] integer c

Guaranteed constraints:
1 ≤ c ≤ 109.

* [output] integer

## Is Infinite Process?

Given integers a and b, determine whether the following pseudocode results in an infinite loop

  while a is not equal to b do
    increase a by 1
    decrease b by 1
Assume that the program is executed on a virtual machine which can store arbitrary long numbers and execute forever.

#### Example

* For a = 2 and b = 6, the output should be
  isInfiniteProcess(a, b) = false;
* For a = 2 and b = 3, the output should be
  isInfiniteProcess(a, b) = true.
#### Input/Output

* [input] integer a

Guaranteed constraints:
0 ≤ a ≤ 20.

* [input] integer b

Guaranteed constraints:
0 ≤ b ≤ 20.

* [output] boolean

true if the pseudocode will never stop, false otherwise.