import numpy as np
from typing import List, Dict, Tuple

def greedy_change(coins: List[int], amount: int) -> Tuple[List[int], int]:

    sorted_coins = sorted(coins, reverse=True)
    selected = []
    remainder = amount
    for coin in sorted_coins:
        while remainder >= coin:
            selected.append(coin)
            remainder -= coin

    return (selected, remainder)

    
def compare_change(coins: List[int], max_amount: int) -> Dict[str, List[int]]:
    result = {
    "optimal": [],
    "suboptimal": [],
    "greedy_failed": [],
    "impossible": []
    }

    for amount in range(1, max_amount + 1):
        greedy_coins, remainder = greedy_change(coins, amount)
        opt_coins = optimal_change(coins, amount)
        if opt_coins == None:
            result["impossible"].append(amount)
        elif remainder > 0:
            result["greedy_failed"].append(amount)
        elif remainder == 0 and len(greedy_coins) > len(opt_coins):
            result["suboptimal"].append(amount)
        elif remainder == 0 and len(greedy_coins) == len(opt_coins):
            result["optimal"].append(amount)

        