import numpy as np
from typing import List, Dict, Tuple

#I.B.1 · optimal_change
def optimal_change(coins: List[int], amount: int) -> List[int] | None:
    if amount == 0:
        return [] 
    if not coins:
        return None

    D = {}
    
 
    c = sorted(coins, reverse=True)
   

    for i in range(len(c) + 1):
        for a in range(amount + 1):
            if i == 0 and a == 0:
                D[i, a] = 0

            elif i == 0 and a > 0:
                D[i, a] = float('inf')

            elif a == 0:
                D[i, a] = 0
           
            elif a < c[i-1]:
                D[i, a] = D[i-1, a]
            
            else:
                D[i, a] = min(D[i-1, a], 1 + D[i, a - c[i-1]])
    if D[len(c), amount] == float('inf'):
        return None
    
    result = []
    i = len(c)
    a = amount

    while a > 0 and i > 0:
        
        if a >= c[i-1] and D[i, a] == 1 + D[i, a - c[i-1]]:
            result.append(c[i-1])
            a -= c[i-1]
        else:
            i -= 1 
    
    return result
    

