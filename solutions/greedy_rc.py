# Greedy heuristic algorithm for the Rod cutting problem
# 11/10/2026
# Noah B

from typing import List, Tuple  # for type hinting


def greedy_rc(prices: List[int], rod_length: int) -> Tuple[int, List[int]]:

    piece_density = []

    for i, price in enumerate(prices):
        length = i + 1
        density = price / length
        piece_density.append({'length': length, 'price': price, 'density': density})
    piece_density.sort(key=lambda p: p['density'], reverse=True)

    remaining = rod_length  # amt of rod left to be cut
    revenue = 0
    cuts = []  # piece lengths chosen

    '''
    Greedy choice is to take the best ratio piece that still can fit as many times as it can fit
    then move on to the next best ratio.. and repeat.
    '''

    for piece in piece_density:
        count = remaining // piece['length']  # how many of this one piece can fit?
        if count > 0:
            revenue += count * piece['price']
            cuts.extend([piece['length']] * count)
            remaining -= count * piece['length']
        if remaining == 0:
            break

    return revenue, cuts


if __name__ == "__main__":
    print(greedy_rc([2, 5, 7, 8, 10], 5))  # required
    print(greedy_rc([1, 5, 8, 9], 4))      # counterexample