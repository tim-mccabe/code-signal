# Overview of all Functions

## Remove K From List

Given a singly linked list of integers `l` and an integer `k`, remove all elements from list `l` that have a value equal to `k`.

#### Example

* For `l = [3, 1, 2, 3, 4, 5]` and `k = 3`, the output should be
  `removeKFromList(l, k) = [1, 2, 4, 5]`;
* For `l = [1, 2, 3, 4, 5, 6, 7]` and `k = 10`, the output should be
  `removeKFromList(l, k) = [1, 2, 3, 4, 5, 6, 7]`.

#### Input/Output

* **[input] linkedlist.integer l**

A singly linked list of integers.

Guaranteed constraints:
0 ≤ list size ≤ 105,
-1000 ≤ element value ≤ 1000.

* **[input] integer k**

An integer.

Guaranteed constraints:
-1000 ≤ k ≤ 1000.

* **[output] linkedlist.integer**

Return `l` with all the values equal to `k` removed.`

## Is List Palindrome

Given a singly linked list of integers, determine whether or not it's a palindrome.

*Note: in examples below and tests preview linked lists are presented as arrays just for simplicity of visualization: in real data you will be given a head node `l` of the linked list*

#### Example

* For `l = [0, 1, 0]`, the output should be
  `isListPalindrome(l) = true`;

* For `l = [1, 2, 2, 3]`, the output should be
  `isListPalindrome(l) = false`.

#### Input/Output

* **[input] linkedlist.integer l**

A singly linked list of integers.

Guaranteed constraints:
0 ≤ list size ≤ 5 · 105,
-109 ≤ element value ≤ 109.

* **[output] boolean**

Return `true` if `l` is a palindrome, otherwise return `false`.