# Runs all three rod cutting algorithms on the test cases and times them
# Noah, Ivy, Kohlby
# main,py

# import time and the 3 algorithms
import time
from solutions.recursive_rc import recursive_rc
from solutions.dp_rc import dp_rc
from solutions.greedy_rc import greedy_rc

# (prices, rod_length)  prices[i-1] is the price of length i
tests = [
    ([2, 5, 7, 8, 10], 5),                 # required instance
    ([1, 5, 8, 9], 4),                     # greedy counterexample
    ([1, 2, 3, 10], 4),                    # no cut
    ([1, 5, 8, 9, 10, 17, 17, 20], 8),     # multiple pieces
    ([1, 5, 8, 9], 1),                     # edge case n = 1
]

for prices, n in tests:
    print("n =", n)
    print("  recursive:", recursive_rc(prices, n))
    print("  dp:       ", dp_rc(prices, n))
    print("  greedy:   ", greedy_rc(prices, n))

# Timing
prices = list(range(1, 23))  # p[i] = i, lengths 1 to 22
for n in [5, 10, 15, 20, 22]:
    start = time.time()
    recursive_rc(prices, n)
    rec_time = time.time() - start

    start = time.time()
    dp_rc(prices, n)
    dp_time = time.time() - start

    print("n =", n, " recursive:", rec_time, "s  dp:", dp_time, "s")
