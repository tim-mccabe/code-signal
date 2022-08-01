# Overview of all Functions

## Create Spiral Matrix

A spiral matrix is a square matrix of size `n × n`. It contains all the integers in range from `1` to `n * n` so that number `1` is written in the bottom right corner, and all other numbers are written in increasing order spirally in the counterclockwise direction.

Given the size of the matrix `n`, your task is to create a spiral matrix.

#### Example

For `n = 3`, the output should be
```
solution(n) = [[5, 4, 3],
               [6, 9, 2],
               [7, 8, 1]]
```
#### Input/Output

* **[input] integer n**

Matrix size, a positive integer.

Guaranteed constraints:
`3 ≤ n ≤ 75`.

* **[output] array.array.integer**

A spiral matrix of size `n`.

## Construct Shell

A 2D list `lst` of size `2 * n - 1` is called a *shell* if it is filled with zeros and has the following configuration:

* lst[0] contains one element;
* lst[1] contains two elements;
* ...
* lst[n - 2] contains n - 1 elements;
* lst[n - 1] contains n elements;
* lst[n] contains n - 1 elements;
* ...
* lst[2 * n - 3] contains two elements;
* lst[2 * n - 2] contains one element.

Given an integer `n`, return a shell list.

#### Example

For `n = 3`, the output should be
```
solution(n) = [[0],
               [0, 0],
               [0, 0, 0],
               [0, 0],
               [0]]
```
#### Input/Output

* **[input] integer n**

An integer defining the size of the shell.

Guaranteed constraints:
`1 ≤ n ≤ 30`.

* **[output] array.array.integer**

A *shell*.

## Word Power

You've heard somewhere that a word is more powerful than an action. You decided to put this statement at a test by assigning a *power* value to each action and each word. To begin somewhere, you defined a *power* of a `word` as the sum of *powers* of its characters, where power of a character is equal to its 1-based index in the plaintext alphabet.

Given a `word`, calculate its power.

#### Example

For `word = "hello"`, the output should be
`solution(word) = 52`.

Letters `'h'`, `'e'`, `'l'` and `'o'` have powers `8`, `5`, `12` and `15`, respectively. Thus, the total power of the `word` is `8 + 5 + 12 + 12 + 15 = 52`.

#### Input/Output

* **[input] string word**

A string consisting of lowercase English letters.

Guaranteed constraints:
`1 ≤ word.length ≤ 25`.

* **[output] integer**

*Power* of the given `word`.

## Cool Pairs

A pair of numbers is considered to be *cool* if their product is divisible by their sum. More formally, a pair `(i, j)` is cool if and only if `(i * j) % (i + j) = 0`.

Given two lists `a` and `b`, find cool pairs with the first number in the pair from `a`, and the second one from `b`. Return the number of different sums of elements in such pairs.

#### Example

For `a = [4, 5, 6, 7, 8]` and `b = [8, 9, 10, 11, 12]`,
the output should be
`solution(a, b) = 2`.

There are three cool pairs that can be formed from these arrays: `(4, 12)`, `(6, 12)` and `(8, 8)`. Their respective sums are `16`, `18` and `16`, which means that there are just `2` different sums: `16` and `18`. Thus, the output should be equal to `2`.

#### Input/Output

* **[input] array.integer a**

Array of distinct elements.

Guaranteed constraints:
`1 ≤ a.length ≤ 100`,
`1 ≤ a[i] ≤ 100`.

* **[input] array.integer b**

Array of distinct elements.

Guaranteed constraints:
`1 ≤ b.length ≤ 100`,
`1 ≤ b[i] ≤ 100`.

* **[output] integer**

The number of different sums of elements in cool pairs formed by elements from `a` and `b`.

## Multiplication Table

Looks like your little brother doesn't want to remember the multiplication table! Instead he wants to play videogames all day long. To teach him a lesson you'd like to write a virus that will pop up in the middle of the game and disappear only when the brother correctly solves several math questions.

To begin with, you need to construct a multiplication table. Given an integer `n`, return the multiplication table of size `n × n`.

#### Example

For `n = 5`, the output should be
```
solution(n) = [[1, 2,  3,  4,  5 ], 
               [2, 4,  6,  8,  10], 
               [3, 6,  9,  12, 15], 
               [4, 8,  12, 16, 20], 
               [5, 10, 15, 20, 25]]
```

#### Input/Output

* **[input] integer n**

The size of the multiplication table.

Guaranteed constraints:
`2 ≤ n ≤ 30`.

* **[output] array.array.integer**

Multiplication table of size `n × n`, i.e. a square matrix that has value `i * j` at the intersection of the `ith` row and the `jth` column (both 1-based).