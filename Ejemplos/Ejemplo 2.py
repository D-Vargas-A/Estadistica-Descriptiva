# Librerías
import numpy as np
import pandas as pd

# Definir marcas de clase y frecuencias
marcas = np.array([2.2, 2.6, 3.0, 3.4])  # puntos medios de intervalos
f = np.array([8, 15, 5, 2])              # frecuencias correspondientes

# Cálculo de N (total de observaciones)
N = f.sum()                              # suma de frecuencias = 30

# Media agrupada
mean_agr = (marcas * f).sum() / N        # suma(f_i * x_i) / N

# Varianza muestral aproximada (usando n-1)
numerador = (f * (marcas - mean_agr)**2).sum()  # sum f_i * (x_i - mean)^2
var_agr = numerador / (N - 1)                  # dividir por N-1
std_agr = np.sqrt(var_agr)                      # desviación estándar

# Mostrar
print("N:", N)
print("Media agrupada:", mean_agr)
print("Varianza agrupada (muestral):", var_agr)
print("Desviación estándar agrupada:", std_agr)
