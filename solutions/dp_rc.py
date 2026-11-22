# Dynamic programming approach for the Rod cutting problem
# 11/10/2026
# Kohlby V

from typing import List, Tuple

def dp_rc(prices: List[int], rod_length: int) -> Tuple[int, List[int]]:

	# Initialize the revenue list values
	revenue = [0] * (rod_length + 1)

	for i in range(1, rod_length + 1):

		for j in range(1, min(i, len(prices)) + 1):
			
			# Compute the revenue using the previous prices
			if (prices[j - 1] + revenue[i - j] > revenue[i]):
				revenue[i] = prices[j - 1] + revenue[i - j]
	
	return (revenue[rod_length], revenue)