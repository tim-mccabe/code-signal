# Overview of all functions 

### Add

Write a function that returns the sum of two numbers.

#### Example

For param1 = 1 and param2 = 2, the output should be
add(param1, param2) = 3.

#### Input/Output

* **[execution time limit] 4 seconds (py3)**

* **[input] integer param1**

 Guaranteed constraints:
 -1000 ≤ param1 ≤ 1000.

* **[input] integer param2**

  Guaranteed constraints:
  -1000 ≤ param2 ≤ 1000.

* **[output] integer**

  The sum of the two inputs.

 ## Century from Year

Given a year, return the century it is in. The first century spans from the year 1 up to and including the year 100, 
the second - from the year 101 up to and including the year 200, etc.

#### Example

* For year = 1905, the output should be
  centuryFromYear(year) = 20;
* For year = 1700, the output should be
  centuryFromYear(year) = 17.
#### Input/Output

* **[execution time limit] 4 seconds (py3)**

* **[input] integer year**

  A positive integer, designating the year.

  Guaranteed constraints:
  1 ≤ year ≤ 2005.

* **[output] integer**

  The number of the century the year is in.

## Check if Palindrome

 Given the string, check if it is a palindrome.

#### Example

* For inputString = "aabaa", the output should be
  checkPalindrome(inputString) = true;
* For inputString = "abac", the output should be
  checkPalindrome(inputString) = false;
* For inputString = "a", the output should be
  checkPalindrome(inputString) = true.
#### Input/Output

* **[execution time limit] 4 seconds (py3)**

* **[input] string inputString**

  A non-empty string consisting of lowercase characters.

  Guaranteed constraints:
  1 ≤ inputString.length ≤ 105.

* **[output] boolean**

  true if inputString is a palindrome, false otherwise.