# Overview of all functions 

## First Duplicate

Given an array `a` that contains only numbers in the range from `1` to `a.length`, find the first duplicate **number** for which the second occurrence has the minimal index. In other words, if there are more than 1 duplicated numbers, return the **number** for which the second occurrence has a smaller index than the second occurrence of the other number does. If there are no such elements, return `-1`.

#### Example

* For `a = [2, 1, 3, 5, 3, 2]`, the output should be `firstDuplicate(a) = 3`.

  There are `2` duplicates: numbers `2` and `3`. The second occurrence of `3` has a smaller index than the second occurrence of `2` does, so the answer is `3`.

* For `a = [2, 2]`, the output should be `firstDuplicate(a) = 2`;

* For `a = [2, 4, 3, 5, 1]`, the output should be `firstDuplicate(a) = -1`.

#### Input/Output

* **[input] array.integer a**

  Guaranteed constraints:
  1 ≤ a.length ≤ 105,
  1 ≤ a[i] ≤ a.length.

* **[output] integer**

The element in `a` that occurs in the array more than once and has the minimal index for its second occurrence. If there are no such elements, return `-1`.

## First Not Repeating Character

Given a string `s` consisting of small English letters, find and return the first instance of a non-repeating character in it. If there is no such character, return `'_'`.

#### Example

* For `s = "abacabad"`, the output should be
  `firstNotRepeatingCharacter(s) = 'c'`.

  There are `2` non-repeating characters in the string: `'c'` and `'d'`. Return `c` since it appears in the string first.

* For `s = "abacabaabacaba",` the output should be
  `firstNotRepeatingCharacter(s) = '_'`.

  There are no characters in this string that do not repeat.

#### Input/Output

* **[input] string s**

A string that contains only lowercase English letters.

Guaranteed constraints:
1 ≤ s.length ≤ 105.

* **[output] char**

The first non-repeating character in `s`, or `'_'` if there are no characters that do not repeat.

## Rotate Image

You are given an n x n 2D matrix that represents an image. Rotate the image by 90 degrees (clockwise).

#### Example

For
```
a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
```
the output should be
```
rotateImage(a) =
    [[7, 4, 1],
     [8, 5, 2],
     [9, 6, 3]]
```
#### Input/Output

* **[input] array.array.integer a**

Guaranteed constraints:
1 ≤ a.length ≤ 100,
a[i].length = a.length,
1 ≤ a[i][j] ≤ 104.

* **[output] array.array.integer**

## Sudoku2

*Sudoku* is a number-placement puzzle. The objective is to fill a `9 × 9` grid with numbers in such a way that each column, each row, and each of the nine `3 × 3` sub-grids that compose the grid *all* contain *all* of the numbers from `1` to `9` one time.

Implement an algorithm that will check whether the given `grid` of numbers represents a valid *Sudoku* puzzle according to the layout rules described above. Note that the puzzle represented by `grid` does not have to be solvable.

#### Example

* For
```
grid = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
        ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
        ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
        ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
        ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
        ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
        ['.', '.', '.', '5', '.', '.', '.', '7', '.']]
```

  the output should be
  `sudoku2(grid) = true`;

* For
```
grid = [['.', '.', '.', '.', '2', '.', '.', '9', '.'],
        ['.', '.', '.', '.', '6', '.', '.', '.', '.'],
        ['7', '1', '.', '.', '7', '5', '.', '.', '.'],
        ['.', '7', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '8', '3', '.', '.', '.'],
        ['.', '.', '8', '.', '.', '7', '.', '6', '.'],
        ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
        ['.', '1', '.', '2', '.', '.', '.', '.', '.'],
        ['.', '2', '.', '.', '3', '.', '.', '.', '.']]
```

  the output should be
  `sudoku2(grid) = false`.

  The given `grid` is not correct because there are two `1`s in the second column. Each column, each row, and each `3 × 3` subgrid can only contain the numbers `1` through `9` one time.

#### Input/Output

* **[input] array.array.char grid**

A `9 × 9` array of characters, in which each character is either a digit from `'1'` to `'9'` or a period `'.'`.

* **[output] boolean**

Return `true` if `grid` represents a valid *Sudoku* puzzle, otherwise return `false`.

## Is Crypt Solution

A *cryptarithm* is a mathematical puzzle for which the goal is to find the correspondence between letters and digits, such that the given arithmetic equation consisting of letters holds true when the letters are converted to digits.

You have an array of strings `crypt`, the *cryptarithm*, and an an array containing the mapping of letters and digits, `solution`. The array `crypt` will contain three non-empty strings that follow the structure: `[word1, word2, word3]`, which should be interpreted as the `word1 + word2 = word3` cryptarithm.

If `crypt`, when it is decoded by replacing all of the letters in the cryptarithm with digits using the mapping in `solution`, becomes a valid arithmetic equation containing no numbers with leading zeroes, the answer is `true`. If it does not become a valid arithmetic solution, the answer is `false`.

Note that number `0` doesn't contain leading zeroes (while for example `00` or `0123` do).

#### Example

For `crypt = ["SEND", "MORE", "MONEY"]` and
```
solution = [['O', '0'],
            ['M', '1'],
            ['Y', '2'],
            ['E', '5'],
            ['N', '6'],
            ['D', '7'],
            ['R', '8'],
            ['S', '9']]
```
the output should be
`isCryptSolution(crypt, solution) = true`.

When you decrypt `"SEND"`, `"MORE"`, and `"MONEY"` using the mapping given in `crypt`, you get `9567 + 1085 = 10652` which is correct and a valid arithmetic equation.

For `crypt = ["TEN", "TWO", "ONE"]` and
```
solution = [['O', '1'],
            ['T', '0'],
            ['W', '9'],
            ['E', '5'],
            ['N', '4']]
```
the output should be
`isCryptSolution(crypt, solution) = false`.

Even though `054 + 091 = 145`, `054` and `091` both contain leading zeroes, meaning that this is not a valid solution.

#### Input/Output

* **[input] array.string crypt**

An array of three non-empty strings containing only uppercase English letters.

Guaranteed constraints:
crypt.length = 3,
1 ≤ crypt[i].length ≤ 14.

* **[input] array.array.char solution**

An array consisting of pairs of characters that represent the correspondence between letters and numbers in the cryptarithm. The first character in the pair is an uppercase English letter, and the second one is a digit in the range from `0` to `9`.

It is guaranteed that `solution` only contains entries for the letters present in `crypt` and that different letters have different values.

Guaranteed constraints:
solution[i].length = 2,
'A' ≤ solution[i][0] ≤ 'Z',
'0' ≤ solution[i][1] ≤ '9',
solution[i][0] ≠ solution[j][0], i ≠ j,
solution[i][1] ≠ solution[j][1], i ≠ j.

* **[output] boolean**

Return `true` if the `solution` represents the correct solution to the cryptarithm `crypt`, otherwise return `false`.