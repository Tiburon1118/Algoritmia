# Práctica 3: Programación Dinámica - Algoritmos Recursivos - Monte Carlo
# Algoritmia y Estructuras de Datos Avanzadas - Curso 2026-2027

import math
import random

# =============================================================================
# I. Alineamiento de Proteínas
# =============================================================================

# I.A Alineamiento Global: Needleman-Wunsch

def needleman_wunsch_matrix(seq1: str, seq2: str, match: int = 2, mismatch: int = -1, gap: int = -1) -> list[list[int]]:
    """
    Construye y devuelve la matriz completa de programación dinámica para el 
    alineamiento global de dos secuencias mediante el algoritmo Needleman-Wunsch.

    La matriz resultante tiene dimensiones (len(seq2) + 1) x (len(seq1) + 1), 
    donde seq1 se desarrolla a lo largo de las columnas y seq2 a lo largo de las filas.

    :param seq1: Primera secuencia a alinear (desarrollada en columnas).
    :param seq2: Segunda secuencia a alinear (desarrollada en filas).
    :param match: Puntuación acordada para una coincidencia de caracteres.
    :param mismatch: Penalización por diferencia de caracteres.
    :param gap: Penalización por introducción de hueco (gap).
    :return: Matriz de programación dinámica (lista de listas de enteros).
    """
    pass

def needleman_wunsch_backtracking(matrix: list[list[int]], seq1: str, seq2: str, match: int = 2, mismatch: int = -1, gap: int = -1) -> tuple[str, str, int]:
    i = len(seq2)
    j = len(seq1)
    total_score = matrix[i][j]

    aligned_1 = []
    aligned_2 = []

    while i > 0 or j > 0:
        current_val = matrix[i][j]

        if i > 0 and j > 0:
            score_diag = match if seq1[j - 1] == seq2[i - 1] else mismatch
            if current_val == matrix[i - 1][j - 1] + score_diag:
                aligned_1.append(seq1[j - 1])
                aligned_2.append(seq2[i - 1])
                i -= 1
                j -= 1
                continue

        if i > 0 and current_val == matrix[i - 1][j] + gap:
            aligned_1.append("-")
            aligned_2.append(seq2[i - 1])
            i -= 1
            continue

        if j > 0 and current_val == matrix[i][j - 1] + gap:
            aligned_1.append(seq1[j - 1])
            aligned_2.append("-")
            j -= 1
            continue

    return "".join(reversed(aligned_1)), "".join(reversed(aligned_2)), total_score

# I.B Alineamiento Local: Smith-Waterman

def smith_waterman_matrix(seq1: str, seq2: str, match: int = 2, mismatch: int = -1, gap: int = -1) -> list[list[int]]:
    """
    Construye y devuelve la matriz de programación dinámica para el alineamiento 
    local de dos secuencias mediante el algoritmo Smith-Waterman.

    Aplica inicialización a ceros en los bordes (primera fila y primera columna) 
    y truncamiento a cero en cada celda para evitar valores negativos. 
    La matriz tiene dimensiones (len(seq2) + 1) x (len(seq1) + 1), donde seq1 se 
    desarrolla a lo largo de las columnas y seq2 a lo largo de las filas.

    :param seq1: Primera secuencia a alinear (desarrollada en columnas).
    :param seq2: Segunda secuencia a alinear (desarrollada en filas).
    :param match: Puntuación por coincidencia.
    :param mismatch: Penalización por diferencia.
    :param gap: Penalización por hueco.
    :return: Matriz de programación dinámica local (lista de listas de enteros).
    """
    pass

def smith_waterman_backtracking(matrix: list[list[int]], seq1: str, seq2: str, match: int = 2, mismatch: int = -1, gap: int = -1) -> tuple[str, str, int]:
    rows = len(seq2) + 1
    cols = len(seq1) + 1

    # Localizar el primer máximo global recorriendo la matriz en orden de construcción
    max_score = 0
    max_i, max_j = 0, 0
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] > max_score:
                max_score = matrix[r][c]
                max_i, max_j = r, c

    i, j = max_i, max_j
    sub_1 = []
    sub_2 = []

    while i > 0 and j > 0 and matrix[i][j] > 0:
        current_val = matrix[i][j]

        score_diag = match if seq1[j - 1] == seq2[i - 1] else mismatch
        if current_val == matrix[i - 1][j - 1] + score_diag:
            sub_1.append(seq1[j - 1])
            sub_2.append(seq2[i - 1])
            i -= 1
            j -= 1
            continue

        if current_val == matrix[i - 1][j] + gap:
            sub_1.append("-")
            sub_2.append(seq2[i - 1])
            i -= 1
            continue

        if current_val == matrix[i][j - 1] + gap:
            sub_1.append(seq1[j - 1])
            sub_2.append("-")
            j -= 1
            continue

    return "".join(reversed(sub_1)), "".join(reversed(sub_2)), max_score

# =============================================================================
# II. Optimización de Rutas en una Cuadrícula
# =============================================================================

# II.A Recursividad Ingenua (Enfoque de Fuerza Bruta)

def min_path_recursive(grid: list[list[int]], i: int, j: int) -> int:

    if i == 0 and j == 0:
        return grid[0][0]
    
    if i == 0:
        return grid[0][j] + min_path_recursive(grid, 0, j - 1)
    
    if j == 0:
        return grid[i][0] + min_path_recursive(grid, i - 1, 0)
    
    return grid[i][j] + min(
        min_path_recursive(grid, i - 1, j),
        min_path_recursive(grid, i, j - 1)
    )

# II.B Programación Dinámica (Enfoque Bottom-Up)

def min_path_dp(grid: list[list[int]]) -> tuple[int, list[list[int]]]:
    """
    Calcula el coste mínimo para ir desde la celda (0, 0) hasta (N-1, M-1) 
    mediante programación dinámica ascendente (bottom-up).

    :param grid: Matriz de costes de dimensiones N x M.
    :return: Tupla con el coste mínimo global (int) y la matriz dp de costes acumulados.
    """
    pass

# II.C Reconstrucción de la Ruta Óptima
def get_optimal_path(grid: list[list[int]]) -> tuple[int, list[tuple[int, int]]]:
    min_cost, dp = min_path_dp(grid)
    
    n = len(grid)
    m = len(grid[0])
    
    i = n - 1
    j = m - 1
    path = []
    
    while i > 0 or j > 0:
        path.append((i, j))
        
        if i == 0:
            j -= 1
        elif j == 0:
            i -= 1
        else:
            if dp[i - 1][j] < dp[i][j - 1]:
                i -= 1
            else:
                j -= 1
                
    path.append((0, 0))
    path.reverse()
    
    return min_cost, path

# =============================================================================
# III. Simulación de Movimiento y Difusión mediante Caminata Aleatoria (Random Walk)
# =============================================================================

# III.A El comportamiento de una partícula individual

def simulate_single_walk(steps: int) -> tuple[float, float, float]:
    if steps == 0:
        return (0.0, 0.0, 0.0)

    x = 0.0
    y = 0.0

    for _ in range(steps):
        theta = random.uniform(0, 2 * math.pi)
        x += math.cos(theta)
        y += math.sin(theta)

    distance = math.hypot(x, y)
    return (x, y, distance)

# III.B El enfoque de Monte Carlo y la Ley de Difusión

def monte_carlo_diffusion_simulation(num_particles: int, num_steps: int) -> float:
    total_sq_dist = 0.0

    for _ in range(num_particles):
        _, _, dist = simulate_single_walk(num_steps)
        total_sq_dist += dist ** 2

    return total_sq_dist / num_particles

# III.C Confinamiento y barreras absorbentes

def simulate_particle_with_barrier(steps: int, max_radius: float) -> bool:
    """
    Simula la caminata paso a paso de una partícula evaluando en cada paso si supera 
    un radio límite (barrera absorbente).

    :param steps: Número máximo de pasos.
    :param max_radius: Radio límite de la barrera desde el origen.
    :return: True si la partícula cruza la barrera en algún paso, False en caso contrario.
    """
    pass

def calculate_escape_probability(num_particles: int, num_steps: int, max_radius: float) -> float:
    """
    Estima la probabilidad de escape de un conjunto de partículas en presencia 
    de una barrera absorbente mediante el método de Monte Carlo.

    :param num_particles: Número de partículas a simular.
    :param num_steps: Número máximo de pasos por partícula.
    :param max_radius: Radio de la barrera absorbente.
    :return: Probabilidad de escape expresada en el intervalo [0.0, 1.0].
    """
    pass