# Overview of all Functions

## Longest Word

Define a word as a sequence of consecutive English letters. Find the longest word from the given string.

#### Example

For text = "Ready, steady, go!", the output should be
longestWord(text) = "steady".

#### Input/Output

* [input] string text

Guaranteed constraints:
4 ≤ text.length ≤ 50.

* [output] string

The longest word from text. It's guaranteed that there is a unique output.

## Valid Time

Check if the given string is a correct time representation of the 24-hour clock.

#### Example

* For time = "13:58", the output should be
  validTime(time) = true;
* For time = "25:51", the output should be
  validTime(time) = false;
* For time = "02:76", the output should be
  validTime(time) = false.
#### Input/Output

* [input] string time

A string representing time in HH:MM format. It is guaranteed that the first two characters, as well as the last two characters, are digits.

* [output] boolean

true if the given representation is correct, false otherwise.