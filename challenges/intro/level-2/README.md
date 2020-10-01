# Overview of all functions 

## Adjacent Elements Product

Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

#### Example

For inputArray = [3, 6, -2, -5, 7, 3], the output should be
adjacentElementsProduct(inputArray) = 21.

7 and 3 produce the largest product.

#### Input/Output

* **[execution time limit] 4 seconds (py3)**

* **[input] array.integer inputArray**

  An array of integers containing at least two elements.

  Guaranteed constraints:
  2 ≤ inputArray.length ≤ 10,
  -1000 ≤ inputArray[i] ≤ 1000.

* **[output] integer**

  The largest product of adjacent elements.

## Shape Area

Below we will define an n-interesting polygon. Your task is to find the area of a polygon for a given n.

A 1-interesting polygon is just a square with a side of length 1. An n-interesting polygon is obtained by taking the n - 1-interesting polygon and appending 1-interesting polygons to its rim, side by side. You can see the 1-, 2-, 3- and 4-interesting polygons in the picture below.

![area](images/area.png)

#### Example

* For n = 2, the output should be
  shapeArea(n) = 5;
* For n = 3, the output should be
  shapeArea(n) = 13.
#### Input/Output

* [execution time limit] 4 seconds (py3)

* [input] integer n

  Guaranteed constraints:
  1 ≤ n < 104.

* [output] integer

  The area of the n-interesting polygon.