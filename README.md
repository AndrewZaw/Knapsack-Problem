# Knapsack-Problem
Iterative algorithm solution for the knapsack problem

From Wikipedia, the [knapsack problem](https://en.wikipedia.org/wiki/Knapsack_problem) or rucksack problem is a problem in combinatorial optimization: Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible. 

In this specific algorithm, it is assumed the total value we are looking to maximize is found by multiplying the value of each item in the knapsack. It can be easily modified for a simpler version which involves adding the values instead. 

## Usage

```
C = int
S = []
V = []

maxProductWrapper(C,S,V)
```

C is an int that represents the size (or weight) of the knapsack.
S is an array containing each respective items' size (or weight).
V is an array containing each respective items' value.

Each element in S directly correponds to an element in V respectively. 

## Examples

```
C = 12
S = [3,7,4,6,5]
V = [5,12,6,9,7]

maxProductWrapper(C,S,V)
```
returns [648, 6, 7, 4].

C indicates the knapsack can hold a weight of up to 12. Each element in S corresponds to the respective item's size (weight), while each element in V corresponds to the respective item's value. Thus item 1 is of size "3" and value "5". Item 2 is of size "7" and value "12" and so on.

The first returned value, 648, represents the maximum value found. The remaining values represent the size of the items chosen. Thus for the largest value for the knapsack, items of size 6, 7 and 4 will yield the highest value. Their respective values (9,12,6) multiplied equal 648. 

## Built with

Python
