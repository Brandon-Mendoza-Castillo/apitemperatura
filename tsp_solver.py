import math
import random

# Coordenadas de las ciudades
coord = {
    'Jiloyork': (19.916012, -99.580580),
    'Toluca': (19.289165, -99.655697),
    'Atlacomulco': (19.799520, -99.873844),
    'Guadalajara': (20.677754, -103.346253),
    'Monterrey': (25.691611, -100.321838),
    'QuintanaRoo': (21.163111, -86.802315),
    'Michohacan': (19.701400, -101.208296),
    'Aguascalientes': (21.876410, -102.264386),
    'CDMX': (19.432713, -99.133183),
    'QRO': (20.597194, -100.386670)
}

# Función de distancia Euclidiana
def distancia(coord1, coord2):
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    return math.sqrt((lat1 - lat2) ** 2 + (lon1 - lon2) ** 2)

# Calcular distancia total de una ruta
def evalua_ruta(ruta):
    total = 0
    for i in range(len(ruta) - 1):
        total += distancia(coord[ruta[i]], coord[ruta[i+1]])
    total += distancia(coord[ruta[-1]], coord[ruta[0]])  # Regreso al inicio
    return total

# Algoritmo de templado simulado
def simulated_annealing(ruta, T_INICIAL, T_MIN, VELOCIDAD_ENFRIAMIENTO):
    T = T_INICIAL
    while T > T_MIN:
        dist_actual = evalua_ruta(ruta)
        for _ in range(VELOCIDAD_ENFRIAMIENTO):
            i, j = random.sample(range(len(ruta)), 2)
            ruta_tmp = ruta[:]
            ruta_tmp[i], ruta_tmp[j] = ruta_tmp[j], ruta_tmp[i]
            nueva_dist = evalua_ruta(ruta_tmp)
            delta = dist_actual - nueva_dist
            if nueva_dist < dist_actual or random.random() < math.exp(delta / T):
                ruta = ruta_tmp
                dist_actual = nueva_dist
        T -= 0.005
    return ruta
