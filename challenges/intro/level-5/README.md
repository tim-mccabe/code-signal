# Overview of all Functions

## Are Equally Strong

Call two arms equally strong if the heaviest weights they each are able to lift are equal.

Call two people equally strong if their strongest arms are equally strong (the strongest arm can be both the right and the left), and so are their weakest arms.

Given your and your friend's arms' lifting capabilities find out if you two are equally strong.

#### Example

* For yourLeft = 10, yourRight = 15, friendsLeft = 15, and friendsRight = 10, the output should be
  areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight) = true;
* For yourLeft = 15, yourRight = 10, friendsLeft = 15, and friendsRight = 10, the output should be
  areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight) = true;
* For yourLeft = 15, yourRight = 10, friendsLeft = 15, and friendsRight = 9, the output should be
  areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight) = false.
#### Input/Output

* **[input] integer yourLeft**

  A non-negative integer representing the heaviest weight you can lift with your left arm.

  Guaranteed constraints:
  0 ≤ yourLeft ≤ 20.

* **[input] integer yourRight**

  A non-negative integer representing the heaviest weight you can lift with your right arm.

  Guaranteed constraints:
  0 ≤ yourRight ≤ 20.

* **[input] integer friendsLeft**

  A non-negative integer representing the heaviest weight your friend can lift with his or her left arm.

  Guaranteed constraints:
  0 ≤ friendsLeft ≤ 20.

* **[input] integer friendsRight**

  A non-negative integer representing the heaviest weight your friend can lift with his or her right arm.

  Guaranteed constraints:
  0 ≤ friendsRight ≤ 20.

* **[output] boolean**

  true if you and your friend are equally strong, false otherwise.

## Array Maximal Adjacent Difference

Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.

#### Example

For inputArray = [2, 4, 1, 0], the output should be
arrayMaximalAdjacentDifference(inputArray) = 3.

#### Input/Output

* **[input] array.integer inputArray**

  Guaranteed constraints:
  3 ≤ inputArray.length ≤ 10,
  -15 ≤ inputArray[i] ≤ 15.

* **[output] integer**

  The maximal absolute difference.

## Is IPv4 Address

An IP address is a numerical label assigned to each device (e.g., computer, printer) participating in a computer network that uses the Internet Protocol for communication. There are two versions of the Internet protocol, and thus two versions of addresses. One of them is the IPv4 address.

Given a string, find out if it satisfies the IPv4 address naming rules.

#### Example

* For inputString = "172.16.254.1", the output should be
  isIPv4Address(inputString) = true;

* For inputString = "172.316.254.1", the output should be
  isIPv4Address(inputString) = false.

  316 is not in range [0, 255].

* For inputString = ".254.255.0", the output should be
  isIPv4Address(inputString) = false.

  There is no first number.

#### Input/Output

* **[input] string inputString**

  A string consisting of digits, full stops and lowercase English letters.

  Guaranteed constraints:
  1 ≤ inputString.length ≤ 30.

* **[output] boolean**

  true if inputString satisfies the IPv4 address naming rules, false otherwise.

## Avoid Obstacles

You are given an array of integers representing coordinates of obstacles situated on a straight line.

Assume that you are jumping from the point with coordinate 0 to the right. You are allowed only to make jumps of the same length represented by some integer.

Find the minimal length of the jump enough to avoid all the obstacles.

#### Example

For inputArray = [5, 3, 6, 7, 9], the output should be
avoidObstacles(inputArray) = 4.

Check out the image below for better understanding:

![obstacle](images/obstacle.png)

#### Input/Output

* **[input] array.integer inputArray**

Non-empty array of positive integers.

Guaranteed constraints:
2 ≤ inputArray.length ≤ 1000,
1 ≤ inputArray[i] ≤ 1000.

* **[output] integer**

The desired length.