import time # Para la función time_measure. Entender código dado.
import matplotlib.pyplot as plt # Para imprimir gráficas. Entender código dado.
import random # Puede usarse random.randint(n, m) para generar listas aleatorias de enteros en las funciones dataprep.
import numpy as np #Sirve para poder usar los arrays
from typing import List, Dict #Sirve para poder usar los List y Dict

# I.A.1 Medición de tiempos de ejecución
def time_measure(f, dataprep, Nlist, Nrep=1000, Nstat=100):
    """Mide la media y varianza del tiempo de ejecución de la función f
    para cada tamaño n presente en Nlist.
    """
    res = []
    for n in Nlist:
        partial = []
        for _ in range(Nstat):
            data = dataprep(n)
            t1 = time.perf_counter()
            for _ in range(Nrep):
                f(data)
            t2 = time.perf_counter()
            t_elem = (t2 - t1) / float(Nrep)
            partial.append(t_elem)

        mean_val = sum(partial) / float(Nstat)
        var_val = sum((x - mean_val) ** 2 for x in partial) / float(Nstat)
        res.append((mean_val, var_val))
    return res

def dataprep_sum_pair_hit(n):
    """Genera un caso donde SÍ existe un par que suma target.
    Devuelve una tupla (lista, target)
    """
    if n < 2:
        n = 2 

    lst = [random.randint(1, 100) for _ in range(n)]
    
    n1, n2 = random.sample(range(n), 2)
    target = lst[n1] + lst[n2]

    return (lst, target)


def dataprep_sum_pair_miss(n):
    """Genera un caso donde NO existe ningún par (Caso peor).
    Devuelve una tupla (lista, target)
    """
    lst = [random.randint(1, 100) for _ in range(n)]
    target = 205 + n
    return (lst, target)

def dataprep_rle(n):
    """Genera una lista con rachas repetidas de dimensión n.
    Devuelve una lista.
    """
    lst =[]

    while len(lst) < n:
        elem = random.randint(1,100)
        tam_racha = random.randint(2, 5)
        tam_racha = min(tam_racha, n - len(lst))
        lst.extend([elem] * tam_racha)
    return lst

# I.A.2 Búsqueda de duplicados manteniendo orden de aparición
def find_duplicates(lst):
    """Devuelve los elementos que aparecen más de una vez en lst,
    preservando el orden de su primera repetición y sin duplicados.
    """
    vistos = set()
    añadidos = set()
    duplicados = []
    
    for num in lst:
        if num in vistos:
            if num not in añadidos:
                duplicados.append(num)
                añadidos.add(num)
        else:
            vistos.add(num)
            
    return duplicados

# I.A.3 evalúa si existen dos elementos en posiciones distintasde la lista lst cuya suma sea igual a target
def has_sum_pair(par):
    """Dada una tupla (lst, target), devuelve True si existen dos elementos
    distintos en lst que sumen target; de lo contrario devuelve False.
    """
    lst, target = par
    vistos = set()
    
    for num in lst:
        find = target - num
        if find in vistos:
            return True
        vistos.add(num)
        
    return False

# I.B.1 RLE Naive / Ingenuo
def rle_encode_naive(lst):
    """Codificación RLE utilizando operador + concatenador de listas."""
    if not lst:
        return[]
    
    cod = []
    count = 1
    anterior = lst[0]

    for num in lst[1:]:
        
        if num == anterior:
            count +=1
        else:
            cod = cod + [(anterior, count)]
            count = 1
            anterior = num
    cod = cod + [(anterior, count)]
    return cod

# I.B.2 RLE Optimized / Óptimo
def rle_encode_optimized(lst):
    """Codificación RLE optimizada usando append in-place."""
    if not lst:
        return []
    cod = []
    count = 1
    anterior = lst[0]

    for num in lst[1:]:
        
        if num == anterior:
            count +=1
        else:
            cod.append((anterior, count))
            count = 1
            anterior = num
    cod.append((anterior, count))
    return cod

# Función auxiliar para generar una gráfica de una serie de datos.
def plot_single_curve(
    x,
    y,
    title="Gráfica de Datos",
    xlabel="Eje X",
    ylabel="Eje Y",
    label=None,
    style="o-",
    color="b",
    grid=True,
    filename=None,
    figsize=(8, 5),
):
    """Genera y muestra/guarda una gráfica limpia para una única serie de datos."""
    plt.figure(figsize=figsize)  # Crea la figura con el tamaño indicado

    # Dibuja la curva
    plt.plot(x, y, style, color=color, label=label)

    # Personalización básica de ejes y título
    plt.title(title)  # Asigna el título
    plt.xlabel(xlabel)  # Etiqueta X
    plt.ylabel(ylabel)  # Etiqueta Y

    if grid:
        plt.grid(True, linestyle="--", alpha=0.6)

    if label:
        plt.legend(
            loc="best"
        )  # Muestra la leyenda si se definió una etiqueta

    plt.tight_layout()

    # Guarda la gráfica en un fichero si se especifica un nombre
    if filename:
        plt.savefig(
            filename, format=filename.split(".")[-1], dpi=300
        )  #

    plt.show()  # Muestra la figura

# II.A.1 devuelve un array con valores -1 en las posiciones {0, 1, ..., n-1}.
def init_cd(n: int) ->  np.ndarray:
    if n <= 0:
        return np.array([], dtype=int)
    return np.full(n, -1, dtype=int)

# II.A.2 devuelve el representante del conjunto obtenido como la unión por rangos de 
# los representados por los índicesrep_1, rep_2 en el CD almacenado en el array p_cd.

def union(rep_1: int, rep_2: int, p_cd: np.ndarray)-> int:

    x = find(rep_1, p_cd)
    y = find(rep_2, p_cd)

    if x == y:
        return x
    elif p_cd[x] < p_cd[y]:
        p_cd[y] = x
        
        return x

    elif p_cd[x] > p_cd[y]:
        p_cd[x] = y
        return y
    else:
        p_cd[x] = y
        p_cd[y] -= 1
        return y
# II.A.3 devuelve el representante del índice ind en el CD almacenado en p_cd realizando compresión de caminos.
def find(ind: int, p_cd: np.ndarray)-> int:
    
    if p_cd[ind] < 0:
        return ind
    
    p_cd[ind] = find(p_cd[ind], p_cd)
    return p_cd[ind]
#II.A.4 devuelve un diccionario cuyas claves sean los representantes de los subconjuntos del CD 
# y donde el valor de la clave u del dict sea una lista con los miembros del subconjunto representado por u
def cd_2_dict(p_cd: np.ndarray)-> Dict:
    res = {}
    n = len(p_cd)
       
    for i in range(n):
        rep = find(i, p_cd)
           
        if rep not in res:
            res[rep] = []
               
        res[rep].append(i)
           
    return res
#II.B.1 devuelve las componentes conexas de un tal grafo
def ccs(n: int, l: List)-> Dict:
    if n <= 0:
        return {}
        
    p_cd = init_cd(n)
    for a, b in l:
        if 0 <= a < n and 0 <= b < n:
            x = find(a, p_cd)
            y = find(b, p_cd)

            if(y != x):
                union(x, y, p_cd)

    d = cd_2_dict(p_cd)

    return d
