# Overview of all Functions

## Longest Word

Define a word as a sequence of consecutive English letters. Find the longest word from the given string.

#### Example

For text = "Ready, steady, go!", the output should be
longestWord(text) = "steady".

#### Input/Output

* [input] string text

Guaranteed constraints:
4 ≤ text.length ≤ 50.

* [output] string

The longest word from text. It's guaranteed that there is a unique output.

## Valid Time

Check if the given string is a correct time representation of the 24-hour clock.

#### Example

* For time = "13:58", the output should be
  validTime(time) = true;
* For time = "25:51", the output should be
  validTime(time) = false;
* For time = "02:76", the output should be
  validTime(time) = false.
#### Input/Output

* [input] string time

A string representing time in HH:MM format. It is guaranteed that the first two characters, as well as the last two characters, are digits.

* [output] boolean

true if the given representation is correct, false otherwise.

## Sum Up Numbers

CodeMaster has just returned from shopping. He scanned the check of the items he bought and gave the resulting string to Ratiorg to figure out the total number of purchased items. Since Ratiorg is a bot he is definitely going to automate it, so he needs a program that sums up all the numbers which appear in the given input.

Help Ratiorg by writing a function that returns the sum of numbers that appear in the given inputString.

#### Example

For inputString = "2 apples, 12 oranges", the output should be
sumUpNumbers(inputString) = 14.

#### Input/Output

* [input] string inputString

Guaranteed constraints:
0 ≤ inputString.length ≤ 105.

* [output] integer

## Different Squares

Given a rectangular matrix containing only digits, calculate the number of different 2 × 2 squares in it.

#### Example

For

matrix = [[1, 2, 1],
          [2, 2, 2],
          [2, 2, 2],
          [1, 2, 3],
          [2, 2, 1]]
the output should be
differentSquares(matrix) = 6.

Here are all 6 different 2 × 2 squares:

* 1 2
  2 2
* 2 1
  2 2
* 2 2
  2 2
* 2 2
  1 2
* 2 2
  2 3
* 2 3
  2 1
#### Input/Output

* [input] array.array.integer matrix

Guaranteed constraints:
1 ≤ matrix.length ≤ 100,
1 ≤ matrix[i].length ≤ 100,
0 ≤ matrix[i][j] ≤ 9.

* [output] integer

The number of different 2 × 2 squares in matrix.

## Digits Product

Given an integer product, find the smallest positive (i.e. greater than 0) integer the product of whose digits is equal to product. If there is no such integer, return -1 instead.

#### Example

* For product = 12, the output should be
  digitsProduct(product) = 26;
* For product = 19, the output should be
  digitsProduct(product) = -1.
#### Input/Output

* [input] integer product

Guaranteed constraints:
0 ≤ product ≤ 600.

* [output] integer

## File Naming

You are given an array of desired filenames in the order of their creation. Since two files cannot have equal names, the one which comes later will have an addition to its name in a form of (k), where k is the smallest positive integer such that the obtained name is not used yet.

Return an array of names that will be given to the files.

#### Example

For names = ["doc", "doc", "image", "doc(1)", "doc"], the output should be
fileNaming(names) = ["doc", "doc(1)", "image", "doc(1)(1)", "doc(2)"].

#### Input/Output

* [input] array.string names

Guaranteed constraints:
5 ≤ names.length ≤ 1000,
1 ≤ names[i].length ≤ 15.

* [output] array.string