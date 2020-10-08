# Overview of all Functions

## Is Beautiful String

A string is said to be beautiful if each letter in the **string** appears at most as many times as **the previous letter in the alphabet within the string**; ie: b occurs no more times than a; c occurs no more times than b; etc.

Given a string, check whether it is *beautiful*.

#### Example

* For inputString = "bbbaacdafe", the output should be isBeautifulString(inputString) = true.

  This string contains 3 as, 3 bs, 1 c, 1 d, 1 e, and 1 f (and 0 of every other letter), so since there aren't any letters that appear more frequently than the previous letter, this string qualifies as beautiful.

* For inputString = "aabbb", the output should be isBeautifulString(inputString) = false.

  Since there are more bs than as, this string is not beautiful.

* For inputString = "bbc", the output should be isBeautifulString(inputString) = false.

  Although there are more bs than cs, this string is not beautiful because there are no as, so therefore there are more bs than as.

#### Input/Output

* **[input] string inputString**

A string of lowercase English letters.

Guaranteed constraints:
3 ≤ inputString.length ≤ 50.

* **[output] boolean**

Return true if the string is beautiful, false otherwise.

## Find Email Domain

An email address such as "John.Smith@example.com" is made up of a local part ("John.Smith"), an "@" symbol, then a domain part ("example.com").

The domain name part of an email address may only consist of letters, digits, hyphens and dots. The local part, however, also allows a lot of different special characters. Here you can look at several examples of correct and incorrect email addresses.

Given a valid email address, find its domain part.

#### Example

* For address = "prettyandsimple@example.com", the output should be
  findEmailDomain(address) = "example.com";
* For address = "fully-qualified-domain@codesignal.com", the output should be
  findEmailDomain(address) = "codesignal.com".
#### Input/Output

* **[input] string address**

Guaranteed constraints:
10 ≤ address.length ≤ 50.

* **[output] string**

## Build Palindrome

Given a string, find the shortest possible string which can be achieved by adding characters to the end of initial string to make it a palindrome.

#### Example

For st = "abcdc", the output should be
buildPalindrome(st) = "abcdcba".

#### Input/Output

* **[input] string st**

A string consisting of lowercase English letters.

Guaranteed constraints:
3 ≤ st.length ≤ 10.

* **[output] string**