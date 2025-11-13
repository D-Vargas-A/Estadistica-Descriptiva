# Librerías necesarias
import numpy as np               # operaciones numéricas y arrays
import pandas as pd              # manejo tabular (opcional)
import matplotlib.pyplot as plt  # gráficos básicos
import seaborn as sns            # visualizaciones (opcional)

# 1) Definir los datos
datos = np.array([2.1, 2.3, 1.9, 2.5, 2.2])   # array NumPy con las observaciones

# 2) Calcular medidas básicas
mean = datos.mean()             # calcula la media aritmética (sum(datos)/n)
median = np.median(datos)       # calcula la mediana
mode = pd.Series(datos).mode()  # devuelve la(s) moda(s) como Serie pandas
var_sample = datos.var(ddof=1)  # varianza muestral (ddof=1 -> n-1)
std_sample = datos.std(ddof=1)  # desviación estándar muestral

# 3) Mostrar resultados
print("Media:", mean)
print("Mediana:", median)
print("Moda(s):", mode.tolist())
print("Varianza muestral:", var_sample)
print("Desviación estándar muestral:", std_sample)

# 4) Visualización rápida
sns.histplot(datos, bins=5, kde=False)  # histograma con seaborn
plt.title("Histograma: tiempos de carga")
plt.xlabel("Tiempo (s)")
plt.ylabel("Frecuencia")

plt.show()
