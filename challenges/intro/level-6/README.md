# Overview of all Functions

## Array Replace

Given an array of integers, replace all the occurrences of elemToReplace with substitutionElem.

#### Example

For inputArray = [1, 2, 1], elemToReplace = 1, and substitutionElem = 3, the output should be
arrayReplace(inputArray, elemToReplace, substitutionElem) = [3, 2, 3].

Input/Output

* **[input] array.integer inputArray**

  Guaranteed constraints:
  0 ≤ inputArray.length ≤ 104,
  0 ≤ inputArray[i] ≤ 109.

* **[input] integer elemToReplace**

  Guaranteed constraints:
  0 ≤ elemToReplace ≤ 109.

* **[input] integer substitutionElem**

  Guaranteed constraints:
  0 ≤ substitutionElem ≤ 109.

* **[output] array.integer**

## Even Digits Only

Check if all digits of the given integer are even.

#### Example

* For n = 248622, the output should be
  evenDigitsOnly(n) = true;
* For n = 642386, the output should be
  evenDigitsOnly(n) = false.
#### Input/Output

* **[input] integer n**

  Guaranteed constraints:
  1 ≤ n ≤ 109.

* **[output] boolean**

  true if all digits of n are even, false otherwise.

## Variable Name

Correct variable names consist only of English letters, digits and underscores and they can't start with a digit.

Check if the given string is a correct variable name.

#### Example

* For name = "var_1__Int", the output should be
  variableName(name) = true;
* For name = "qq-q", the output should be
  variableName(name) = false;
* For name = "2w2", the output should be
  variableName(name) = false.
#### Input/Output

* **[input] string name**

  Guaranteed constraints:
  1 ≤ name.length ≤ 10.

* **[output] boolean**

  true if name is a correct variable name, false otherwise.