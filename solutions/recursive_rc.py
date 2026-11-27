# Recursive algorithm for the Rod cutting problem
# 11/10/2026
# Ivy S

from typing import List


def recursive_rc(prices: List[int], rod_length: int) -> int:
    """Return the maximum revenue for a rod of length rod_length.

    prices[i - 1] is the price of a piece of length i.

    Recurrence (with p[i] = prices[i - 1]):
        R(0) = 0
        R(n) = max over 1 <= i <= n of { p[i] + R(n - i) }

    i         = length of the FIRST piece we cut off
    p[i]      = money we get for that first piece
    R(n - i)  = best money we can get from the remaining rod
    """
    if rod_length == 0:                     # base case: empty rod earns nothing
        return 0

    best = float("-inf")
    for i in range(1, rod_length + 1):      # try every possible first piece length
        best = max(best, prices[i - 1] + recursive_rc(prices, rod_length - i))
    return best


if __name__ == "__main__":
    print(recursive_rc([2, 5, 7, 8, 10], 5))  # required instance, expect 12
    print(recursive_rc([1, 5, 8, 9], 4))      # counterexample, expect 10
    print(recursive_rc([1, 3, 10], 3))        # no cut, expect 10
    print(recursive_rc([4], 1))               # edge case n = 1, expect 4
