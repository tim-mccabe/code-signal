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