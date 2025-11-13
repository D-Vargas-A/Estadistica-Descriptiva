# Librerías
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Datos
salarios = np.array([4.0,4.2,4.5,4.8,5.0,5.1,5.3,6.0,6.5,8.0])

# 1) Mediana (P50)
mediana = np.median(salarios)   # mediana por defecto

# 2) Percentiles con np.percentile (por defecto interpolación 'linear')
q1_np = np.percentile(salarios, 25)  # percentil 25
q3_np = np.percentile(salarios, 75)  # percentil 75
p90_np = np.percentile(salarios, 90) # percentil 90

# 3) IQR y boxplot
iqr = q3_np - q1_np

# Mostrar resultados
print("Mediana (np):", mediana)
print("Q1 (np.percentile):", q1_np)
print("Q3 (np.percentile):", q3_np)
print("IQR (np):", iqr)
print("P90 (np.percentile):", p90_np)

# 4) Gráfico boxplot
sns.boxplot(x=salarios)   # boxplot horizontal por defecto
plt.title("Boxplot de salarios (millones)")
plt.xlabel("Salario (millones)")
plt.show()