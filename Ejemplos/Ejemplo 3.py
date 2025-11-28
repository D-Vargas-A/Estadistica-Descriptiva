# ejemplo3_percentiles_boxplot.py
import numpy as np                        # numpy: operaciones numéricas vectorizadas
import pandas as pd                       # pandas: estructura DataFrame para resumen
import matplotlib.pyplot as plt           # matplotlib: visualización

# --- Datos ---
team_A = np.array([3.2,3.3,3.5,3.6,3.8,4.0,4.1,4.2,4.4,4.5,4.8,5.0])   # Equipo A
team_B = np.array([4.5,4.6,4.7,4.8,5.0,5.2,5.3,5.5,5.7,6.0,6.5,7.5])   # Equipo B
team_C = np.array([2.8,3.0,3.1,3.2,3.3,3.4,3.6,3.8,4.0,4.1,4.9,8.0])   # Equipo C

# combinado
all_data = np.concatenate([team_A, team_B, team_C])  # concatena los 3 equipos en un vector
n = len(all_data)                                    # tamaño total de la muestra

# --- Cálculo NumPy (método digital) ---
# Nota: en numpy moderno usar method='linear' en lugar de interpolation; aquí se mantiene por claridad.
q1_np = np.percentile(all_data, 25, interpolation='linear')   # primer cuartil (25%)
q2_np = np.percentile(all_data, 50, interpolation='linear')   # mediana (50%)
q3_np = np.percentile(all_data, 75, interpolation='linear')   # tercer cuartil (75%)
p90_np = np.percentile(all_data, 90, interpolation='linear')  # percentil 90
iqr_np = q3_np - q1_np                                        # IQR

# fences Tukey (regla 1.5*IQR para outliers)
lower_fence = q1_np - 1.5 * iqr_np
upper_fence = q3_np + 1.5 * iqr_np

# identificar outliers (valores fuera de fences)
outliers = all_data[(all_data < lower_fence) | (all_data > upper_fence)]

# Resumen en DataFrame para reporte
summary = pd.DataFrame({
    'N': [n],
    'Q1': [q1_np],
    'Q2_median': [q2_np],
    'Q3': [q3_np],
    'IQR': [iqr_np],
    'P90': [p90_np],
    'LowerFence': [lower_fence],
    'UpperFence': [upper_fence],
    'Outliers': [outliers.tolist()]
})

print(summary.T)   # transpuesto para lectura vertical en consola

# --- Boxplots comparativos por equipo ---
fig, ax = plt.subplots(figsize=(9,5))
ax.boxplot([team_A, team_B, team_C],
           labels=['Equipo A','Equipo B','Equipo C'],
           showmeans=True)   # showmeans dibuja un marcador para la media
ax.set_title('Comparativo Boxplot por Equipo (salarios, millones)')
ax.set_ylabel('Salario (millones)')

# Anotar outliers detectados (global)
# Atención: la x fija 3.05 está pensada para colocar la anotación cerca del tercer boxplot (ajustable)
for val in outliers:
    ax.annotate(f'Outlier {val:.2f}', xy=(3.05, val), xytext=(3.25, val+0.2),
                arrowprops=dict(arrowstyle='->', lw=0.8), fontsize=9)

plt.grid(axis='y', linestyle=':', alpha=0.5)
plt.tight_layout()
plt.show()

# --- Boxplot combinado con líneas de percentiles globales ---
fig2, ax2 = plt.subplots(figsize=(10,3))
ax2.boxplot(all_data, vert=False, showmeans=True, widths=0.6)  # boxplot horizontal
ax2.set_xlabel('Salario (millones)')
ax2.set_title('Boxplot combinado (global) con percentiles anotados')

# líneas verticales (percentiles y fence superior)
ax2.axvline(q1_np, color='C1', linestyle='--', label=f'Q1 {q1_np:.3f}')
ax2.axvline(q2_np, color='C2', linestyle='-.', label=f'Mediana {q2_np:.3f}')
ax2.axvline(q3_np, color='C3', linestyle=':', label=f'Q3 {q3_np:.3f}')
ax2.axvline(p90_np, color='k', linestyle='-', alpha=0.6, label=f'P90 {p90_np:.2f}')
ax2.axvline(upper_fence, color='r', linestyle='--', label=f'Upper fence {upper_fence:.3f}')
ax2.legend(loc='upper right')

plt.tight_layout()
plt.show()
