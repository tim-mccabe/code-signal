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

## Alphabet Subsequence

Check whether the given string is a subsequence of the plaintext alphabet.

#### Example

* For `s = "effg"`, the output should be
  `alphabetSubsequence(s) = false`;
* For `s = "cdce"`, the output should be
  `alphabetSubsequence(s) = false`;
* For `s = "ace"`, the output should be
  `alphabetSubsequence(s) = true`;
* For `s = "bxz"`, the output should be
  `alphabetSubsequence(s) = true`.

#### Input/Output

* **[input] string s**

Guaranteed constraints:
2 ≤ s.length ≤ 15.

* **[output] boolean**

`true` if the given string is a *subsequence* of the alphabet, `false` otherwise.

## Minimal Number of Coins

You find yourself in Bananaland trying to buy a banana. You are super rich so you have an unlimited supply of banana-coins, but you are trying to use as few coins as possible.

The coin values available in Bananaland are stored in a sorted array `coins`. `coins[0] = 1`, and for each `i (0 < i < coins.length)` `coins[i]` is divisible by `coins[i - 1]`. Find the minimal number of banana-coins you'll have to spend to buy a banana given the banana's `price`.

#### Example

For `coins = [1, 2, 10]` and `price = 28`, the output should be
`minimalNumberOfCoins(coins, price) = 6`.

You have to use `10` twice, and `2` four times.

#### Input/Output

* **[input] array.integer coins**

The coin values available in Bananaland.

Guaranteed constraints:
1 ≤ coins.length ≤ 5,
1 ≤ coins[i] ≤ 120.

* **[input] integer price**

A positive integer representing the price of the banana.

Guaranteed constraints:
8 ≤ price ≤ 250.

* **[output] integer**

The minimal number of coins you can use to buy the banana.

## Add Border

Given a rectangular matrix of characters, add a border of asterisks(`*`) to it.

#### Example

For

picture = 
```
           ["abc",
           "ded"]
```
the output should be

addBorder(picture) = 
```
                      ["*****",
                      "*abc*",
                      "*ded*",
                      "*****"]
```
#### Input/Output

* **[input] array.string picture**

A non-empty array of non-empty equal-length strings.

Guaranteed constraints:
1 ≤ picture.length ≤ 100,
1 ≤ picture[i].length ≤ 100.

* **[output] array.string**

The same matrix of characters, framed with a border of asterisks of width `1`.

## Switch Lights

`N` candles are placed in a row, some of them are initially lit. For each candle from the `1st` to the `Nth` the following algorithm is applied: if the observed candle is lit then states of this candle and all candles before it are changed to the opposite. Which candles will remain lit after applying the algorithm to all candles in the order they are placed in the line?

#### Example

* For `a = [1, 1, 1, 1, 1]`, the output should be
  `switchLights(a) = [0, 1, 0, 1, 0]`.

  Check out the image below for better understanding:

![candels](images/candels.png)

* For `a = [0, 0]`, the output should be
  `switchLights(a) = [0, 0]`.

The candles are not initially lit, so their states are not altered by the algorithm.

#### Input/Output

* **[input] array.integer a**

Initial situation - array of zeros and ones of length N, 1 means that the corresponding candle is lit.

Guaranteed constraints:
2 ≤ a.length ≤ 5000.

* **[output] array.integer**

Situation after applying the algorithm - array in the same format as input with the same length.

## Timed Reading

Timed Reading is an educational tool used in many schools to improve and advance reading skills. A young elementary student has just finished his very first timed reading exercise. Unfortunately he's not a very good reader yet, so whenever he encountered a word longer than `maxLength`, he simply skipped it and read on.

Help the teacher figure out how many words the boy has read by calculating the number of words in the `text` he has read, no longer than `maxLength`.
Formally, a word is a substring consisting of English letters, such that characters to the left of the leftmost letter and to the right of the rightmost letter are not letters.

#### Example

For `maxLength = 4` and
`text = "The Fox asked the stork, 'How is the soup?'"`,
the output should be
`timedReading(maxLength, text) = 7`.

The boy has read the following words: `"The", "Fox", "the", "How", "is", "the", "soup"`.

#### Input/Output

* **[input] integer maxLength**

A positive integer, the maximum length of the word the boy can read.

Guaranteed constraints:
1 ≤ maxLength ≤ 10.

* **[input] string text**

A non-empty string of English letters and punctuation marks.

Guaranteed constraints:
3 ≤ text.length ≤ 110.

* **[output] integer**

The number of words the boy has read.