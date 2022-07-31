# Overview of all Functions

## Repeat Char

To make debug output more understandable, you often separate sets of logs by a single line of the same character. Since you use this method very often, you'd like to write a function that would handle printing the separator.

Implement a function that, given a character `ch` and the number of times it should be repeated `n`, returns a string of `n` characters `ch`.

#### Example

For `ch = '*'` and `n = 20`, the output should be
`solution(ch, n) = "********************"`.

#### Input/Output

* **[input] char ch**

The character that should be repeated.

* **[input] integer n**

The number of times the given character should be repeated.

Guaranteed constraints:
`1 ≤ n ≤ 100`.

**[output] string**

A string consisting of `n` characters `ch`.

## Get Points

A new scoring system was introduced in your university: from now on, each test will consist of the predefined list of questions, and for the `ith` (1-based) question a student either gets `i` points, or loses `p` points as a penalty.

Your task is to calculate the number of points a student got for some test. Implement a function that would calculate the number of points received for the test based on the given list of `answers`.

#### Example

For `answers = [true, true, false, true]` and `p = 2`, the output should be
`solution(answers, p) = 5`.

Here's why: `1 + 2 - 2 + 4 = 5`.

#### Input/Output

* **[input] array.boolean answers**

Array of student's answers. `answers[i]` is `true` if the student answered the `(i + 1)th` question correctly, and `false` otherwise.

Guaranteed constraints:
`1 ≤ answers.length ≤ 20`.

* **[input] integer p**

The number of points subtracted from the final score for each incorrect result.

Guaranteed constraints:
`0 ≤ p ≤ 10`.

* **[output] integer**

The number of points the student received for the test.

## Sort Students

You are given a list of `students` who want to apply to the internship at CodeSignal. For the `ith` student you know their full name `students[i]`, which can consist of up to `5` words (where a word is a set of consecutive letters). It is guaranteed that the surname is always the last name of student's full name.

Your task is to sort the students lexicographically by their surnames. If two students happen to have the same surname, their order in the result should be the same as in the original list.

#### Example

For
```
students = ["John Smith", "Jacky Mon Simonoff", 
            "Lucy Smith", "Angela Zimonova"]
```
the output should be
```
solution(students) = ["Jacky Mon Simonoff", "John Smith", 
                          "Lucy Smith", "Angela Zimonova"]
```
#### Input/Output

* **[input] array.string students**

Array of students, where each student is given by their full name consisting of at most `5` words. For each `i` `students[i]` consists of English letters and whitespace (`' '`) characters.

Guaranteed constraints:
`1 ≤ students.length ≤ 30`,
`1 ≤ students[i].length ≤ 50`.

* **[output] array.string**

Array of `students` sorted as described above.

## Is Test Solvable

You've been preparing all night for the upcoming test and entered the class certain that you will ace it. Now that you received the test questions, you died inside a little: looks like you prepared for the test on a completely different topic.

You're not even sure if you should bother to answer the questions. You still have some hope though: it is known that there's a glitch in the test preparing system, so that if the sum of digits of question ids is divisible by `k`, the answer to each question has a `90%` probability to be an A.

Given the list of question `ids`, determine if the sum of their digits is divisible by `k` to see if it's worth trying to pass the test.

#### Example

For `ids = [529665, 909767, 644200]` and `k = 3`, the output should be
`solution(ids, k) = true`.

The sum of digits is

`(5 + 2 + 9 + 6 + 6 + 5) + (9 + 0 + 9 + 7 + 6 + 7) + (6 + 4 + 4 + 2 + 0 + 0) = 87`
which is divisible by `3`. Today is your lucky day after all!

#### Input/Output

* **[input] array.integer ids**

Array of unique question ids.

Guaranteed constraints:
`1 ≤ ids.length ≤ 50`,
`0 ≤ ids[i] ≤ 106`.

* **[input] integer k**

The number that causes a glitch in the test preparing system.

Guaranteed constraints:
`2 ≤ k ≤ 10`.

* **[output] boolean**

`true` if the total sum of digits in `ids` is divisible by `k`, `false` otherwise.