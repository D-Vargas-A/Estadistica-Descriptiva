import numpy as np                 # 1: numpy — arrays y utilidades numéricas
import pandas as pd                # 2: pandas — estructuras tabulares (DataFrame)
import seaborn as sns              # 3: seaborn — visualización estadística de alto nivel
import matplotlib.pyplot as plt    # 4: matplotlib — backend de gráficos
from scipy.stats import norm, mode # 5: norm para la PDF Normal; mode para la moda

# 1) Datos: 20 mediciones no agrupadas
data = [                          # 6: lista Python con las 20 observaciones (tiempos en s)
    12.1, 11.7, 12.4, 13.0, 12.8, 11.9, 12.2, 12.5,
    12.7, 12.6, 13.1, 12.9, 11.8, 12.3, 12.4, 12.5,
    12.2, 12.1, 12.0, 12.8
]

df = pd.DataFrame({"tiempo": data})  # 7: convierto la lista en DataFrame con columna "tiempo"

# 2) Cálculos estadísticos
media = df["tiempo"].mean()          # 8: media aritmética (E[X]) — indicador central
mediana = df["tiempo"].median()      # 9: mediana (50%) — robusta frente a outliers

# scipy.stats.mode devuelve un array, tomamos solo el valor
moda_valor = mode(df["tiempo"], keepdims=True).mode[0]  # 10: moda (valor más frecuente)

var_poblacional = df["tiempo"].var(ddof=0)  # 11: varianza poblacional (n en el denominador)
var_muestral = df["tiempo"].var(ddof=1)     # 12: varianza muestral (n-1 en denom — estimador insesgado)

desv_poblacional = df["tiempo"].std(ddof=0) # 13: desviación estándar poblacional
desv_muestral = df["tiempo"].std(ddof=1)    # 14: desviación estándar muestral

# 15-21: impresión de resultados clave en consola para control operativo
print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda_valor)
print("Varianza poblacional:", var_poblacional)
print("Varianza muestral:", var_muestral)
print("Desv. estándar poblacional:", desv_poblacional)
print("Desv. estándar muestral:", desv_muestral)

#  Gráfico: Ajuste tipo Normal (curva teórica)
plt.figure(figsize=(12, 6))              # 22: tamaño del lienzo — formato apaisado para presentación

# Histograma base
sns.histplot(df["tiempo"], kde=False, color="lightgray", stat="density", bins=10)  # 23:
# - histograma de densidad: muestra la distribución empírica
# - stat="density": normaliza área a 1 para superponer PDF teórica

# Rango de valores
x = np.linspace(min(data), max(data), 200)  # 24: vector x continuo entre min y max con 200 puntos

# Curva normal con parámetros estimados
pdf = norm.pdf(x, media, desv_muestral)     # 25: calculo la PDF normal usando media y desviación muestral
plt.plot(x, pdf, color="blue", linewidth=2, label="Curva Normal estimada")  # 26: dibujo la curva

# Líneas de referencia estadísticas
plt.axvline(media, color="red", linestyle="--", label=f"Media = {media:.2f}")     # 27: media
plt.axvline(mediana, color="green", linestyle="-.", label=f"Mediana = {mediana:.2f}") # 28: mediana
plt.axvline(moda_valor, color="purple", linestyle=":", label=f"Moda = {moda_valor:.2f}") # 29: moda

plt.title("Ajuste Normal a los tiempos de calibración\nInterpretación visual del comportamiento del proceso") # 30
plt.xlabel("Tiempo (s)")                   # 31: etiqueta eje X
plt.ylabel("Densidad")                     # 32: etiqueta eje Y (densidad porque usamos stat='density')
plt.legend()                               # 33: leyenda con líneas de referencia
plt.show()                                 # 34: renderizo gráfica en pantalla
