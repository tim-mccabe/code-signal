# Overview of all Functions

## Growing Plant

Caring for a plant can be hard work, but since you tend to it regularly, you have a plant that grows consistently. Each day, its height increases by a fixed amount represented by the integer upSpeed. But due to lack of sunlight, the plant decreases in height every night, by an amount represented by downSpeed.

Since you grew the plant from a seed, it started at height 0 initially. Given an integer desiredHeight, your task is to find how many days it'll take for the plant to reach this height.

#### Example

For upSpeed = 100, downSpeed = 10, and desiredHeight = 910, the output should be
growingPlant(upSpeed, downSpeed, desiredHeight) = 10.

| # | Day | Night |
|---|---|---|
| 1 | 100 | 90 |
| 2 | 190 | 180 |
| 3 | 280 | 270 |
| 4 | 370 | 360 |
| 5 | 460 | 450 |
| 6 | 550 | 540 |
| 7 | 640 | 630 |
| 8 | 730 | 720 |
| 9 | 820 | 810 |
| 10 | 910 | 900 |
The plant first reaches a height of 910 on day 10.

#### Input/Output

* **[input] integer upSpeed**

A positive integer representing the daily growth of the plant.

Guaranteed constraints:
3 ≤ upSpeed ≤ 100.

* **[input] integer downSpeed**

A positive integer representing the nightly decline of the plant.

Guaranteed constraints:
2 ≤ downSpeed < upSpeed.

* **[input] integer desiredHeight**

A positive integer representing the goal height.

Guaranteed constraints:
4 ≤ desiredHeight ≤ 1000.

* **[output] integer**

The number of days that it will take for the plant to reach / pass desiredHeight.

## Knapsack Light

You found two items in a treasure chest! The first item weighs weight1 and is worth value1, and the second item weighs weight2 and is worth value2. What is the total maximum value of the items you can take with you, assuming that your max weight capacity is maxW and you can't come back for the items later?

**Note** that there are only two items and you can't bring more than one item of each type, i.e. you can't take two first items or two second items.

#### Example

* For value1 = 10, weight1 = 5, value2 = 6, weight2 = 4, and maxW = 8, the output should be
  knapsackLight(value1, weight1, value2, weight2, maxW) = 10.

  You can only carry the first item.

* For value1 = 10, weight1 = 5, value2 = 6, weight2 = 4, and maxW = 9, the output should be
  knapsackLight(value1, weight1, value2, weight2, maxW) = 16.

  You're strong enough to take both of the items with you.

* For value1 = 5, weight1 = 3, value2 = 7, weight2 = 4, and maxW = 6, the output should be
  knapsackLight(value1, weight1, value2, weight2, maxW) = 7.

  You can't take both items, but you can take any of them.

#### Input/Output

* **[input] integer value1**

Guaranteed constraints:
2 ≤ value1 ≤ 20.

* **[input] integer weight1**

Guaranteed constraints:
2 ≤ weight1 ≤ 10.

* **[input] integer value2**

Guaranteed constraints:
2 ≤ value2 ≤ 20.

* **[input] integer weight2**

Guaranteed constraints:
2 ≤ weight2 ≤ 10.

* **[input] integer maxW**

Guaranteed constraints:
1 ≤ maxW ≤ 20.

* **[output] integer**