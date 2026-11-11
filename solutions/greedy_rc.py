# Greedy heuristic algorithm for the Rod cutting problem
# 11/10/2026
# Noah B & Kohlby V

from typing import List # for type hinting

def greedy_rc(prices: List[int], rod_length: int) -> int:

	piece_density = []

	for i, price in enumerate(prices):
		len = i + 1
		density = price/len
		piece_density.append({'length' : len, 'price': price, 'density': density})
	piece_density.sort(key=lambda p: p['density'], reverse=True)
 
   
   
