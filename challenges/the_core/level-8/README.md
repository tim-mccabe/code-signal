# Overview of all Functions

## String Construction

Given two strings `a` and `b`, both consisting only of lowercase English letters, your task is to calculate how many strings equal to `a` can be constructed using only letters from the string `b`? Each letter can be used only once and in one string only.

#### Example

* For `a = "abc"` and `b = "abccba"`, the output should be `stringsConstruction(a, b) = 2`.

  We can construct `2` strings `a = "abc"` using only letters from the string `b`.

* For `a = "ab"` and `b = "abcbcb"`, the output should be `stringsConstruction(a, b) = 1`.

#### Input/Output

* **[input] string a**

String to construct, containing only lowercase English letters.

Guaranteed constraints:
1 ≤ a.length ≤ 105.

* **[input] string b**

String containing needed letters, containing only lowercase English letters.

Guaranteed constraints:
1 ≤ b.length ≤ 105.

* **[output] integer**

The number of strings `a` that can be constructed from the string `b`.

## Is Substitution Cipher?

A *ciphertext alphabet* is obtained from the plaintext alphabet by means of rearranging some characters. For example `"bacdef...xyz"` will be a simple ciphertext alphabet where `a` and `b` are rearranged.

A *substitution cipher* is a method of encoding where each letter of the *plaintext alphabet* is replaced with the corresponding (i.e. having the same index) letter of some *ciphertext alphabet*.

Given two strings, check whether it is possible to obtain them from each other using some (possibly, different) *substitution ciphers*.

#### Example

* For `string1 = "aacb"` and `string2 = "aabc"`, the output should be
  `isSubstitutionCipher(string1, string2) = true`.

  Any *ciphertext alphabet* that starts with `acb...` would make this transformation possible.

* For `string1 = "aa"` and `string2 = "bc"`, the output should be
  `isSubstitutionCipher(string1, string2) = false`.

#### Input/Output

* **[input] string string1**

A string consisting of lowercase English characters.

Guaranteed constraints:
1 ≤ string1.length ≤ 10.

* **[input] string string2**

A string consisting of lowercase English characters of the same length as `string1`.

Guaranteed constraints:
`string2.length = string1.length`.

[output] boolean