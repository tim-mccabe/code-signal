# Overview of all Functions

# Circle of Numbers

Consider integer numbers from 0 to n - 1 written down along the circle in such a way that the distance between any two neighboring numbers is equal (note that 0 and n - 1 are neighboring, too).

Given n and firstNumber, find the number which is written in the radially opposite position to firstNumber.

#### Example

For n = 10 and firstNumber = 2, the output should be
circleOfNumbers(n, firstNumber) = 7.

![circle](images/circle_or_numbers.png)

#### Input/Output

* **[input] integer n**

A positive even integer.

Guaranteed constraints:
4 ≤ n ≤ 20.

* **[input] integer firstNumber**

Guaranteed constraints:
0 ≤ firstNumber ≤ n - 1.

* **[output] integer**

## Deposit Profit

You have deposited a specific amount of money into your bank account. Each year your balance increases at the same growth rate. With the assumption that you don't make any additional deposits, find out how long it would take for your balance to pass a specific threshold.

#### Example

For deposit = 100, rate = 20, and threshold = 170, the output should be
depositProfit(deposit, rate, threshold) = 3.

Each year the amount of money in your account increases by 20%. So throughout the years, your balance would be:

* year 0: 100;
* year 1: 120;
* year 2: 144;
* year 3: 172.8.
Thus, it will take 3 years for your balance to pass the threshold, so the answer is 3.

#### Input/Output

* **[input] integer deposit**

The initial deposit, guaranteed to be a positive integer.

Guaranteed constraints:
1 ≤ deposit ≤ 100.

* **[input] integer rate**

The rate of increase. Each year the balance increases by the rate percent of the current sum.

Guaranteed constraints:
1 ≤ rate ≤ 100.

* **[input] integer threshold**

The target balance.

Guaranteed constraints:
deposit < threshold ≤ 200.

* **[output] integer**

The number of years it would take to hit the threshold.