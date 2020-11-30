## Overview of all Functions

## Enclose In Brackets

Given a string, enclose it in round brackets.

#### Example

For `inputString = "abacaba"`, the output should be
`encloseInBrackets(inputString) = "(abacaba)"`.

#### Input/Output

* **[input] string inputString**

Guaranteed constraints:
0 ≤ inputString.length ≤ 10.

* **[output] string**

## Proper Noun Correction

*Proper nouns* always begin with a capital letter, followed by small letters.

Correct a given proper noun so that it fits this statement.

#### Example

* For `noun = "pARiS"`, the output should be
  `properNounCorrection(noun) = "Paris"`;
* For `noun = "John"`, the output should be
  `properNounCorrection(noun) = "John"`.

#### Input/Output

* **[input] string noun**

A string representing a proper noun with a mix of capital and small English letters.

Guaranteed constraints:
1 ≤ noun.length ≤ 10.

* **[output] string**

Corrected (if needed) noun.

## Is Tandem Repeat?

Determine whether the given string can be obtained by one concatenation of some string to itself.

#### Example

* For `inputString = "tandemtandem"`, the output should be
  `isTandemRepeat(inputString) = true`;
* For `inputString = "qqq"`, the output should be
  `isTandemRepeat(inputString) = false`;
* For `inputString = "2w2ww"`, the output should be
  `isTandemRepeat(inputString) = false`.

#### Input/Output

* **[input] string inputString**

Guaranteed constraints:
2 ≤ inputString.length ≤ 20.

* **[output] boolean**

`true` if `inputString` represents a string concatenated to itself, `false` otherwise.

## Is Case-Insensitive Palindrome?

Given a string, check if it can become a palindrome through a case change of some (possibly, none) letters.

#### Example

* `For inputString = "AaBaa"`, the output should be
  `isCaseInsensitivePalindrome(inputString) = true`.

  `"aabaa"` is a palindrome as well as `"AABAA"`, `"aaBaa"`, etc.

* For `inputString = "abac"`, the output should be
  `isCaseInsensitivePalindrome(inputString) = false`.

  All the strings which can be obtained via changing case of some group of letters, i.e. `"abac"`, `"Abac"`, `"aBAc"` and 13 more, are not palindromes.

#### Input/Output

* **[input] string inputString**

Non-empty string consisting of English letters.

Guaranteed constraints:
4 ≤ inputString.length ≤ 10.

* **[output] boolean**

## Find Email Domain

An email address such as `"John.Smith@example.com"` is made up of a local part (`"John.Smith"`), an `"@"` symbol, then a domain part (`"example.com"`).

The domain name part of an email address may only consist of letters, digits, hyphens and dots. The local part, however, also allows a lot of different special characters. Here you can look at several examples of correct and incorrect email addresses.

Given a valid email address, find its domain part.

#### Example

* For `address = "prettyandsimple@example.com"`, the output should be
  `findEmailDomain(address) = "example.com"`;
* For `address = "fully-qualified-domain@codesignal.com"`, the output should be
  `findEmailDomain(address) = "codesignal.com"`.

#### Input/Output

* **[input] string address**

Guaranteed constraints:
10 ≤ address.length ≤ 50.

* **[output] string**

## HTML End Tag By Start Tag

You are implementing your own HTML editor. To make it more comfortable for developers you would like to add an auto-completion feature to it.

Given the starting HTML tag, find the appropriate end tag which your editor should propose.

If you are not familiar with HTML, consult with this note.

#### Example

* For `startTag = "<button type='button' disabled>`", the output should be
  `htmlEndTagByStartTag(startTag) = "</button>"`;
* For `startTag = "<i>"`, the output should be
  `htmlEndTagByStartTag(startTag) = "</i>"`.

#### Input/Output

* **[input] string startTag**

Guaranteed constraints:
3 ≤ startTag.length ≤ 75.

* **[output] string**

## Is MAC48 Address?

A media access control address (MAC address) is a unique identifier assigned to network interfaces for communications on the physical network segment.

The standard (IEEE 802) format for printing MAC-48 addresses in human-friendly form is six groups of two hexadecimal digits (`0` to `9` or `A` to `F`), separated by hyphens (e.g. `01-23-45-67-89-AB`).

Your task is to check by given string `inputString` whether it corresponds to MAC-48 address or not.

#### Example

* For `inputString = "00-1B-63-84-45-E6"`, the output should be
  `isMAC48Address(inputString) = true`;
* For `inputString = "Z1-1B-63-84-45-E6"`, the output should be
  `isMAC48Address(inputString) = false`;
* For `inputString = "not a MAC-48 address"`, the output should be
  `isMAC48Address(inputString) = false`.

#### Input/Output

* **[input] string inputString**

Guaranteed constraints:
15 ≤ inputString.length ≤ 20.

* **[output] boolean**

`true` if `inputString` corresponds to MAC-48 address naming rules, `false` otherwise.

## Is Unstable Pair?

Some file managers sort filenames taking into account case of the letters, others compare strings as if all of the letters are of the same case. That may lead to different ways of filename ordering.

Call two filenames an *unstable* pair if their ordering depends on the case.

To compare two filenames `a` and `b`, find the first position `i` at which `a[i] ≠ b[i]`. If `a[i] < b[i]`, then `a < b`. Otherwise `a > b`. If such position doesn't exist, the shorter string goes first.

Given two filenames, check whether they form an unstable pair.

#### Example

* For `filename1 = "aa"` and `filename2 = "AAB"`, the output should be
  `isUnstablePair(filename1, filename2) = true`.

  Because `"AAB" < "aa"`, but `"AAB" > "AA"`.

* For `filename1 = "A"` and `filename2 = "z"`, the output should be
  `isUnstablePair(filename1, filename2) = false`.

  Both `"A" < "z"` and `"a" < "z"`.

#### Input/Output

* **[input] string filename1**

A non-empty string of English letters and digits.

Guaranteed constraints:
1 ≤ filename1.length ≤ 10.

* **[input] string filename2**

A non-empty string of English letters and digits. It's guaranteed that there is no ambiguity, i.e. even being considered in the same case strings are never equal.

Guaranteed constraints:
1 ≤ filename2.length ≤ 10.

* **[output] boolean**

`true` if `filename1` and `filename2` form an unstable pair, `false` otherwise.