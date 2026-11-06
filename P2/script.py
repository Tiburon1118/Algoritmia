import time
import matplotlib.pyplot as plt
from p2 import greedy_change, optimal_change

# Rango de cantidades objetivo (amounts) a evaluar
# Nota: optimal_change con programación dinámica crece en O(A * m), 
# por lo que puedes ajustar los valores según lo que tarde en ejecutarse.
AmountList = [50, 100, 200, 500, 1000]

greedy_tiempos = []
optimal_tiempos = []

# Sistema de monedas de prueba
coins = [25, 10, 4, 1]

for amount in AmountList:
    Nrep = 50  # Repetimos varias veces para promediar y evitar ruido temporal
    
    # 1. Medir tiempo de greedy_change
    t1 = time.perf_counter()
    for _ in range(Nrep):
        _ = greedy_change(coins, amount)
    t2 = time.perf_counter()
    greedy_tiempo_medio = (t2 - t1) / Nrep
    
    # 2. Medir tiempo de optimal_change (Programación Dinámica)
    t1 = time.perf_counter()
    for _ in range(Nrep):
        _ = optimal_change(coins, amount)
    t2 = time.perf_counter()
    optimal_tiempo_medio = (t2 - t1) / Nrep
    
    greedy_tiempos.append(greedy_tiempo_medio)
    optimal_tiempos.append(optimal_tiempo_medio)

# Gráfica: Comparación de Tiempos (Greedy vs Optimal)
plt.figure(figsize=(7, 4.5))
plt.plot(AmountList, greedy_tiempos, 'o-', label="Greedy Change O(m log m + k)", linewidth=2, color='tab:blue')
plt.plot(AmountList, optimal_tiempos, 's--', label="Optimal Change (DP) O(A · m)", linewidth=2, color='tab:red')

plt.title("Comparación Temporal: Greedy Change vs Optimal Change")
plt.xlabel("Cantidad objetivo (amount)")
plt.ylabel("Tiempo medio (s)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend(fontsize=10)
plt.tight_layout()
plt.savefig("grafica_cambio_comparacion_tiempos.png", dpi=300)
plt.show()