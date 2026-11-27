# CS411-Final

Rod cutting: comparing recursive, dynamic programming, and greedy algorithms.
CS 411 Fall 2026 semester project by Noah Bush, Kohlby Vierthaler, and Ivy Swenson at the University of Alaska Fairbanks. Contains source code for algorithms in \solutions and a report analyzing the correctness, time complexity, and differing approaches of each.

## Language

Python 3.9 or later. Standard library only, no packages to install.

## Project structure

```
main.py                    runs all three algorithms on the test cases and times them
solutions/recursive_rc.py  direct recursive algorithm
solutions/dp_rc.py         bottom-up dynamic programming with cut reconstruction
solutions/greedy_rc.py     greedy heuristic (best price per unit length)
report/                    final write-up (PDF)
```

## How to run

From the project folder:

```
python3 main.py
```

The whole run takes about 3 seconds; most of it is the recursive algorithm at n = 24.

## Input format

Each algorithm takes a price list and a rod length:

```
recursive_rc(prices, rod_length)  -> revenue
dp_rc(prices, rod_length)         -> (revenue, list of piece lengths)
greedy_rc(prices, rod_length)     -> (revenue, list of piece lengths)
```

`prices[i - 1]` is the price of a piece of length `i`, so `prices = [2, 5, 7, 8, 10]` means length 1 sells for 2, length 2 for 5, and so on. `prices` must have at least `rod_length` entries.

The test cases are defined in the `tests` list at the top of `main.py`, as `(description, prices, rod_length)`. To try your own input, add a line there, for example:

```
("my test", [3, 5, 8, 9, 10], 5),
```

The timing experiment uses one fixed price table for lengths 1 to 24, generated with random seed 411 so the results are reproducible.

## Sample output

```
Test cases
case                     n   rec    dp  greedy  dp plan       greedy plan   greedy optimal?
-------------------------------------------------------------------------------------------
required instance        5    12    12      12  [1, 2, 2]     [2, 2, 1]     yes
greedy counterexample    4    10    10       9  [2, 2]        [3, 1]        NO
no cut                   4    10    10      10  [4]           [4]           yes
multiple pieces          8    22    22      22  [2, 6]        [6, 2]        yes
edge case n = 1          1     1     1       1  [1]           [1]           yes

Timing (same price table, same machine)
prices for lengths 1..24 = [2, 4, 7, 7, 14, 13, 13, 12, 26, 25, 29, 32, 34, 26, 43, 39, 43, 46, 50, 48, 33, 59, 55, 56]
   n  rec rev  dp rev  greedy rev   rec time (s)   dp time (s)    rec/dp
------------------------------------------------------------------------
   5       14      14          14       0.000004    0.00000143        3x
  10       28      28          28       0.000123    0.00000358       34x
  15       43      43          42       0.004035    0.00000662      610x
  18       52      52          52       0.032260    0.00000906     3562x
  20       57      57          56       0.128607    0.00001065    12075x
  22       61      61          61       0.512404    0.00001251    40949x
  24       69      69          68       2.037084    0.00001468   138788x
```

Revenues and cutting plans are always the same. Running times depend on the machine.
