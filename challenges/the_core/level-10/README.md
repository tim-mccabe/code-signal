# Overview of all Function

## Character Parity

Given a character, check if it represents an odd digit, an even digit or not a digit at all.

#### Example

* For `symbol = '5'`, the output should be
  `characterParity(symbol) = "odd"`;
* `For symbol = '8'`, the output should be
  `characterParity(symbol) = "even"`;
* For `symbol = 'q'`, the output should be
  `characterParity(symbol) = "not a digit"`.

#### Input/Output

* **[input] char symbol**

A symbol to check.

Guaranteed constraints:
symbol is guaranteed to be a UTF-8 symbol.

* **[output] string**

## Reflect String

Define an *alphabet reflection* as follows: `a` turns into `z`, `b` turns into `y`, `c` turns into `x`, ..., `n` turns into `m`, `m` turns into `n`, ..., `z` turns into `a`.

Define a *string reflection* as the result of applying the alphabet reflection to each of its characters.

Reflect the given string.

#### Example

For `inputString = "name"`, the output should be
`reflectString(inputString) = "mznv"`.

#### Input/Output

* **[input] string inputString**

A string of lowercase characters.

Guaranteed constraints:
3 ≤ inputString.length ≤ 1000.

* **[output] string**