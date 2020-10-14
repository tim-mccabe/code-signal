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

## Arithmetic Expression

Consider an arithmetic expression of the form a#b=c. Check whether it is possible to replace # with one of the four signs: +, -, * or / to obtain a correct expression.

#### Example

* For a = 2, b = 3, and c = 5, the output should be
  arithmeticExpression(a, b, c) = true.

  We can replace # with a + to obtain 2 + 3 = 5, so the answer is true.

* For a = 8, b = 2, and c = 4, the output should be
  arithmeticExpression(a, b, c) = true.

  We can replace # with a / to obtain 8 / 2 = 4, so the answer is true.

* For a = 8, b = 3, and c = 2, the output should be
  arithmeticExpression(a, b, c) = false.

  * 8 + 3 = 11 ≠ 2;
  * 8 - 3 = 5 ≠ 2;
  * 8 * 3 = 24 ≠ 2;
  * 8 / 3 = 2.(6) ≠ 2.
  So the answer is false.

#### Input/Output

* [input] integer a

Guaranteed constraints:
1 ≤ a ≤ 20.

* [input] integer b

Guaranteed constraints:
1 ≤ b ≤ 20.

* [input] integer c

Guaranteed constraints:
0 ≤ c ≤ 20.

* [output] boolean

true if the desired replacement is possible, false otherwise.

## Tennis Set

In tennis, the winner of a set is based on how many games each player wins. The first player to win 6 games is declared the winner **unless** their opponent had already won 5 games, in which case the set continues until one of the players has won 7 games.

Given two integers score1 and score2, your task is to determine if it is possible for a tennis set to be finished with a final score of score1 : score2.

#### Example

* For score1 = 3 and score2 = 6, the output should be
  tennisSet(score1, score2) = true.

  Since player 1 hadn't reached 5 wins, the set ends once player 2 has won 6 games.

* For score1 = 8 and score2 = 5, the output should be
  tennisSet(score1, score2) = false.

  Since both players won at least 5 games, the set would've ended once one of them won the 7th one.

* For score1 = 6 and score2 = 5, the output should be
  tennisSet(score1, score2) = false.

  This set will continue until one of these players wins their 7th game, so this can't be the final score.

#### Input/Output

* [input] integer score1

Number of games won by the 1st player, non-negative integer.

Guaranteed constraints:
0 ≤ score1 ≤ 10.

* [input] integer score2

Number of games won by the 2nd player, non-negative integer.

Guaranteed constraints:
0 ≤ score2 ≤ 10.

* [output] boolean

true if score1 : score2 represents a possible score for an ended set, false otherwise.

## Will You?

Once Mary heard a famous song, and a line from it stuck in her head. That line was "Will you still love me when I'm no longer young and beautiful?". Mary believes that a person is loved if and only if he/she is both young and beautiful, but this is quite a depressing thought, so she wants to put her belief to the test.

Knowing whether a person is young, beautiful and loved, find out if they contradict Mary's belief.

A person contradicts Mary's belief if one of the following statements is true:

* they are young and beautiful but not loved;
* they are loved but not young or not beautiful.
#### Example

* For young = true, beautiful = true, and loved = true, the output should be
  willYou(young, beautiful, loved) = false.

  Young and beautiful people are loved according to Mary's belief.

* For young = true, beautiful = false, and loved = true, the output should be
  willYou(young, beautiful, loved) = true.

  Mary doesn't believe that not beautiful people can be loved.

#### Input/Output

* [input] boolean young

* [input] boolean beautiful

* [input] boolean loved

* [output] boolean

true if the person contradicts Mary's belief, false otherwise.

