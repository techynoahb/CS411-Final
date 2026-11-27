# Dynamic programming approach for the Rod cutting problem
# 11/10/2026
# Kohlby V

from typing import List, Tuple

def dp_rc(prices: List[int], rod_length: int) -> Tuple[int, List[int]]:

	# Initialize the revenue and reconstructed cutting list values
	revenue = [0] * (rod_length + 1)
	first_cut = [0] * (rod_length + 1)

	for i in range(1, rod_length + 1):
	
		for j in range(1, min(i, len(prices)) + 1):
			
			# Compute the revenue using the previous prices
			if (prices[j - 1] + revenue[i - j] > revenue[i]):
				revenue[i] = prices[j - 1] + revenue[i - j]
				first_cut[i] = j
	
	# Reconstruct the optimal cutting plan
	cutting_plan: List[int] = []
	remaining = rod_length
	
	while remaining > 0:
		piece = first_cut[remaining]
		cutting_plan.append(piece)
		remaining -= piece

	return (revenue[rod_length], cutting_plan)