import numpy as np
from typing import List, Tuple, Dict, Optional
import random

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
    


# =============================================================================
# II. Selección de actividades
# =============================================================================

def activity_selection(activities: List[Tuple[str, int, int]]) -> List[Tuple[str, int, int]]:
    """
    Selecciona el máximo número posible de actividades compatibles.
    Ordena por tiempo de finalización ascendente, y en caso de empate por inicio e identificador.
    """
    order = sorted(activities, key= lambda x: x[2])

    selecionadas = [order[0]]

    u_hora = selecionadas[0][2]

    for i in range(1,len(order)):
        if order[i][1] >= u_hora:
            selecionadas.append(order[i])
            u_hora = order[i][2]
    return selecionadas


def generate_activities(n: int, seed: int = 42) -> List[Tuple[str, int, int]]:
    """
    Genera n actividades aleatorias reproducibles.
    start en [0, 10000], duration en [1, 100], end = start + duration.
    """
    random.seed(seed)

    activities=[]

    for i in range(n):
        act_id = f"A{i}"
        act_start = random.randint(0, 10000)
        act_duration = random.randint(1, 100)
        act_end = act_start + act_duration
        activities.append((act_id, act_start, act_end))

    return activities

# =============================================================================
# III. Planificación de tareas con fechas límite
# =============================================================================

def job_scheduling(jobs: List[Tuple[str, int, int]]) -> Tuple[List[Optional[Tuple[str, int, int]]], int]:
    """
    Planificación de tareas de duración unitaria con fecha límite (deadline).
    Devuelve la secuencia de tareas asignadas (con None para intervalos vacíos) y el beneficio total.
    """

    if not jobs :
        return ([], 0)
    
    sorted_jobs = sorted(jobs, key=lambda x: (-x[1], x[2], x[0]))
    
    max_d = max(job[2] for job in jobs)
    schedule = [None] *max_d

    total_profit=0

    for job in sorted_jobs:
        job_id, profit, deadline = job

        for slot in range(deadline - 1, -1, -1):
            if schedule[slot] is None:
                schedule[slot] = job        
                total_profit += profit      
                break                       

    return (schedule,total_profit)


def generate_jobs(n: int, seed: int = 42) -> List[Tuple[str, int, int]]:
    """
    Genera n tareas aleatorias con fecha límite reproducibles.
    profit en [1, 1000], deadline en [1, max(1, n // 10)].
    """
    pass
