# Overview of all Functions

## Fix Message

One of your friends has an awful writing style: he almost never starts a message with a capital letter, but adds uppercase letters in random places throughout the message. It makes chatting with him very difficult for you, so you decided to write a plugin that will change each `message` received from your friend into a more readable form.

Implement a function that will change the very first symbol of the given `message` to uppercase, and make all the other letters lowercase.

#### Example

For `message = "you'll NEVER believe what that 'FrIeNd' of mine did!!1"`,
the output should be
`fixMessage(message) = "You'll never believe what that 'friend' of mine did!!1"`.

#### Input/Output

* **[input] string message**

A string consisting of English letters, whitespace characters, digits and punctuation marks.

Guaranteed constraints:
1 ≤ message.length ≤ 65.

* **[output] string**

Fixed `message` with its first letter capitalized, and all other letters converted to lowercase.

## Cat Walk

You've been working on a particularly difficult algorithm all day, and finally decided to take a break and drink some coffee. To your horror, when you returned you found out that your cat decided to take a walk on the keyboard in your absence, and pressed a key or two. Your computer doesn't react to letters being pressed when an unauthorized action appears, but allows typing whitespace characters and moving the arrow keys, so now your masterpiece contains way too many whitespace characters.

To repair the damage, you need to start with implementing a function that will replace all multiple space characters in the given `line` of your code with single ones. In addition, all leading and trailing whitespaces should be removed.

#### Example

For
```
line = "def      m   e  gaDifficu     ltFun        ction(x):"
```
the output should be
`catWalk(line) = "def m e gaDifficu ltFun ction(x):"`.

#### Input/Output

* **[input] string line**

One line from your code containing way too many whitespace characters.

Guaranteed constraints:
5 ≤ line.length ≤ 125.

* **[output] string**

`line` with unnecessary whitespace characters removed.

## Convert Tabs

You found an awesome customizable Python IDE that has almost everything you'd like to see in your working environment. However, after a couple days of coding you discover that there is one important feature that this IDE lacks: it cannot convert tabs to spaces. Luckily, the IDE is easily customizable, so you decide to write a plugin that would convert all tabs in the code into the given number of whitespace characters.

Implement a function that, given a piece of `code` and a positive integer `x` will turn each tabulation character in `code` into `x` whitespace characters.

#### Example

For `code = "\treturn False"` and `x = 4`, the output should be
```
convertTabs(code, x) = "    return False"
```
#### Input/Output

* **[input] string code**

Your piece of code.

Guaranteed constraints:
0 ≤ code.length ≤ 1500.

* **[input] integer x**

The number of whitespace characters (`' '`) that should replace each occurrence of the tabulation character (`'\t'`).

Guaranteed constraints:
1 ≤ x ≤ 16.

* **[output] string**

The given `code` with tabulation characters expanded according to `x`.

## Feedback Review

You've launched a revolutionary service not long ago, and were busy improving it for the last couple of months. When you finally decided that the service is perfect, you remembered that you created a feedbacks page long time ago, which you never checked out since then. Now that you have nothing left to do, you would like to have a look at what the community thinks of your service.

Unfortunately it looks like the feedbacks page is far from perfect: each `feedback` is displayed as a one-line string, and if it's too long there's no way to see what it is about. Naturally, this horrible bug should be fixed. Implement a function that, given a `feedback` and the `size` of the screen, splits the `feedback` into lines so that:

* each token (i.e. sequence of non-whitespace characters) belongs to one of the lines entirely;
* each line is at most `size` characters long;
* no line has trailing or leading spaces;
* each line should have the maximum possible length, assuming that all lines before it were also the longest possible.

#### Example

For `feedback = "This is an example feedback"` and `size = 8`,
the output should be
```
feedbackReview(feedback, size) = ["This is", 
                                  "an", 
                                  "example", 
                                  "feedback"]
```
#### Input/Output

* **[input] string feedback**

A string containing a feedback. Each feedback is guaranteed to contain only letters, punctuation marks and whitespace characters (`' '`).

Guaranteed constraints:
0 ≤ feedback.length ≤ 100.

* **[input] integer size**

The size of the screen. It is guaranteed that it is not smaller than the longest token in the feedback.

Guaranteed constraints:
1 ≤ size ≤ 100.

* **[output] array.string**

Lines from the `feedback`, split as described above.

## Is Word Palindrome

Given a `word`, check whether it is a *palindrome* or not. A string is considered to be a *palindrome* if it reads the same in both directions.

#### Example

* For `word = "aibohphobia"`, the output should be
  `isWordPalindrome(word) = true`;

* For `word = "hehehehehe"`, the output should be
  `isWordPalindrome(word) = false`.

#### Input/Output

* **[input] string word**

A string containing lowercase English letters.

Guaranteed constraints:
1 ≤ word.length ≤ 20.

* **[output] boolean**

`true` if the given `word` is a *palindrome*, `false` otherwise.

## Permutation Cipher

You found your very first laptop in the attic, and decided to give in to nostalgia and turn it on. The laptop turned out to be password protected, but you know how to crack it: you have always used the same `password`, but encrypt it using *permutation ciphers* with various keys. The `key` to the cipher used to protect your old laptop very conveniently happened to be written on the laptop lid.

Here's how *permutation cipher* works: the `key` to it consists of all the letters of the alphabet written up in some order. All occurrences of letter `'a'` in the encrypted text are substituted with the first letter of the `key`, all occurrences of letter `'b'` are replaced with the second letter from the `key`, and so on, up to letter `'z'` replaced with the last symbol of the `key`.

Given the `password` you always use, your task is to encrypt it using the *permutation cipher* with the given `key`.

#### Example

For `password = "iamthebest"` and
`key = "zabcdefghijklmnopqrstuvwxy"`, the output should be
`permutationCipher(password, key) = "hzlsgdadrs"`.

Here's a table that can be used to encrypt the text:
```
abcdefghijklmnopqrstuvwxyz
||  |  ||   |     || 
vv  v  vv   v     vv
zabcdefghijklmnopqrstuvwxy
```
#### Input/Output

* **[input] string password**

The password you always use. It is guaranteed to consist only of lowercase English letters.
If you're using Python 2, note that the string is given as a unicode.

Guaranteed constraints:
1 ≤ password.length ≤ 26.

* **[input] string key**

The key to the permutation cipher. It is guaranteed to be a permutation of the plaintext alphabet.
If you're using Python 2, note that the string is given as a unicode.

Guaranteed constraints:
`key.length = 26`.

* **[output] string**

Your `password` encrypted by the *permutations cipher* with the given `key`.

