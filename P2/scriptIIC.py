import time
import matplotlib.pyplot as plt
from p2 import activity_selection, generate_activities

Nlist = [100, 500, 1000, 5000]

tiempos = []
seleccionadas = []
porcentajes = []

for n in Nlist:
    actividades = generate_activities(n, seed=42)
    
    # Repetimos 10 veces para un promedio estable
    Nrep = 10
    t1 = time.perf_counter()
    for _ in range(Nrep):
        res = activity_selection(actividades)
    t2 = time.perf_counter()
    
    tiempo_medio = (t2 - t1) / Nrep
    cant = len(res)
    pct = (cant / n) * 100
    
    tiempos.append(tiempo_medio)
    seleccionadas.append(cant)
    porcentajes.append(pct)

# Gráfica 1: Tiempo
plt.figure(figsize=(7, 4.5))
plt.plot(Nlist, tiempos, 'o-', linewidth=2)
plt.title("Gráfica 1: Tamaño de entrada (n) vs Tiempo de ejecución")
plt.xlabel("Número de actividades (n)")
plt.ylabel("Tiempo medio (s)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("grafica_ii_1_tiempo.png", dpi=300)
plt.show()

# Gráfica 2: Número de seleccionadas
plt.figure(figsize=(7, 4.5))
plt.plot(Nlist, seleccionadas, 's-', color='tab:green', linewidth=2)
plt.title("Gráfica 2: Tamaño de entrada (n) vs Actividades seleccionadas")
plt.xlabel("Número de actividades (n)")
plt.ylabel("Cantidad seleccionada")
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("grafica_ii_2_cantidad.png", dpi=300)
plt.show()

# Gráfica 3: Porcentaje seleccionado
plt.figure(figsize=(7, 4.5))
plt.plot(Nlist, porcentajes, '^--', color='tab:orange', linewidth=2)
plt.title("Gráfica 3: Tamaño de entrada (n) vs Porcentaje seleccionado")
plt.xlabel("Número de actividades (n)")
plt.ylabel("Porcentaje seleccionado (%)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("grafica_ii_3_porcentaje.png", dpi=300)
plt.show()