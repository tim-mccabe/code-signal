# Overview of all Functions

Determine if the given character is a digit or not.

#### Example

* For symbol = '0', the output should be
  isDigit(symbol) = true;
* For symbol = '-', the output should be
  isDigit(symbol) = false.
#### Input/Output

* **[input] char symbol**

A character which is either a digit or not.

Guaranteed constraints:
Given symbol is from ASCII table.

* **[output] boolean**

true if symbol is a digit, false otherwise.

## Line Encoding

Given a string, return its encoding defined as follows:

* First, the string is divided into the least possible number of disjoint substrings consisting of identical characters
  for example, "aabbbc" is divided into ["aa", "bbb", "c"]
* Next, each substring with length greater than one is replaced with a concatenation of its length and the repeating character
  for example, substring "bbb" is replaced by "3b"
* Finally, all the new strings are concatenated together in the same order and a new string is returned.
#### Example

For s = "aabbbc", the output should be
lineEncoding(s) = "2a3bc".

#### Input/Output

* **[input] string s**

String consisting of lowercase English letters.

Guaranteed constraints:
4 ≤ s.length ≤ 15.

* **[output] string**

Encoded version of s.

## Chess Knight

Given a position of a knight on the standard chessboard, find the number of different moves the knight can perform.

The knight can move to a square that is two squares horizontally and one square vertically, or two squares vertically and one square horizontally away from it. The complete move therefore looks like the letter L. Check out the image below to see all valid moves for a knight piece that is placed on one of the central squares.

![chess_1](images/chess_1.png)

#### Example

* For cell = "a1", the output should be
  chessKnight(cell) = 2.

  ![chess_2](images/chess_2.png)

* For cell = "c2", the output should be
  chessKnight(cell) = 6.

  ![chess_3](images/chess_3.png)

#### Input/Output

* **[input] string cell**

String consisting of 2 letters - coordinates of the knight on an 8 × 8 chessboard in chess notation.

Guaranteed constraints:
cell.length = 2,
'a' ≤ cell[0] ≤ 'h',
1 ≤ cell[1] ≤ 8.

* **[output] integer**