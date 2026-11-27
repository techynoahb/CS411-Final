# Runs all three rod cutting algorithms on the test cases and times them
# Noah, Ivy, Kohlby
# main.py

# import time, random and the 3 algorithms
import random
import time
from solutions.recursive_rc import recursive_rc
from solutions.dp_rc import dp_rc
from solutions.greedy_rc import greedy_rc

# (description, prices, rod_length)  prices[i-1] is the price of length i
tests = [
    ("required instance",     [2, 5, 7, 8, 10], 5),
    ("greedy counterexample", [1, 5, 8, 9], 4),
    ("no cut",                [1, 2, 3, 10], 4),
    ("multiple pieces",       [1, 5, 8, 9, 10, 17, 17, 20], 8),
    ("edge case n = 1",       [1, 5, 8, 9], 1),
]


def plan_revenue(prices, pieces):
    """Total price of a cutting plan (list of piece lengths)."""
    return sum(prices[c - 1] for c in pieces)


# ---------------------------------------------------------------------------
# Part 1: test cases -- compare the revenue of all three algorithms
# ---------------------------------------------------------------------------
print("Test cases")
header = "{:<23}{:>3}{:>6}{:>6}{:>8}  {:<14}{:<14}{}".format(
    "case", "n", "rec", "dp", "greedy", "dp plan", "greedy plan", "greedy optimal?")
print(header)
print("-" * len(header))

for desc, prices, n in tests:
    rec = recursive_rc(prices, n)
    dp_rev, dp_plan = dp_rc(prices, n)
    gr_rev, gr_plan = greedy_rc(prices, n)

    # check: pieces add up to n and their prices add up to the reported revenue
    assert sum(dp_plan) == n and plan_revenue(prices, dp_plan) == dp_rev, desc
    assert sum(gr_plan) == n and plan_revenue(prices, gr_plan) == gr_rev, desc
    assert rec == dp_rev, "recursive and dp disagree on " + desc

    print("{:<23}{:>3}{:>6}{:>6}{:>8}  {:<14}{:<14}{}".format(
        desc, n, rec, dp_rev, gr_rev, str(dp_plan), str(gr_plan),
        "yes" if gr_rev == dp_rev else "NO"))
print()


# ---------------------------------------------------------------------------
# Part 2: running time on increasing rod lengths
# One fixed price table for every n, so all algorithms see the same data.
# Prices grow with length (about 1.5 - 3 per unit) with some randomness;
# the fixed seed makes the results reproducible.
# ---------------------------------------------------------------------------
def time_call(func, prices, n, repeats):
    """Average wall-clock time (seconds) of func(prices, n) over `repeats` runs."""
    start = time.perf_counter()
    for _ in range(repeats):
        result = func(prices, n)
    return result, (time.perf_counter() - start) / repeats


sizes = [5, 10, 15, 18, 20, 22, 24]
rng = random.Random(411)
prices = [round(length * rng.uniform(1.5, 3.0)) for length in range(1, max(sizes) + 1)]

print("Timing (same price table, same machine)")
print("prices for lengths 1..{} = {}".format(max(sizes), prices))
header = "{:>4}{:>9}{:>8}{:>12}{:>15}{:>14}{:>10}".format(
    "n", "rec rev", "dp rev", "greedy rev", "rec time (s)", "dp time (s)", "rec/dp")
print(header)
print("-" * len(header))

for n in sizes:
    # recursive is exponential: repeat a few times for small n, once for big n
    rec, rec_t = time_call(recursive_rc, prices, n, 5 if n <= 15 else 1)
    (dp_rev, _), dp_t = time_call(dp_rc, prices, n, 1000)
    gr_rev, _ = greedy_rc(prices, n)
    print("{:>4}{:>9}{:>8}{:>12}{:>15.6f}{:>14.8f}{:>9.0f}x".format(
        n, rec, dp_rev, gr_rev, rec_t, dp_t, rec_t / dp_t))
