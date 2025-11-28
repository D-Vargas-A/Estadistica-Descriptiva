import numpy as np                 # operaciones numéricas eficientes (arrays, sqrt, cumsum, linspace)
import matplotlib.pyplot as plt    # generación de gráficos

# --- Entrada: datos agrupados por clases ---
intervalos = [(1.0,1.4),(1.4,1.8),(1.8,2.2),(2.2,2.6),(2.6,3.0),(3.0,3.4)]
marcas = np.array([1.2,1.6,2.0,2.4,2.8,3.2])  # marca de clase (punto medio de cada intervalo)
f = np.array([12,30,54,60,28,10])             # frecuencias absolutas por clase
N = f.sum()                                   # tamaño total de la muestra (suma de frecuencias)
h = intervalos[0][1] - intervalos[0][0]       # ancho de clase (se asume constante)

# --- Estadísticos agrupados (media, varianza, desviación) ---
mean_agr = (marcas * f).sum() / N             # media por marcas: sum(x_i * f_i) / N
var_num = (f * (marcas - mean_agr)**2).sum()  # numerador varianza agrupada
var_muestral = var_num / (N - 1)              # varianza muestral (n-1): estimador insesgado
std_muestral = np.sqrt(var_muestral)          # desviación estándar muestral

# --- Mediana por interpolación en clase ---
pos_med = N / 2                               # posición de la mediana en frecuencia acumulada
cumf = np.cumsum(f)                           # frecuencia acumulada por clases
med_class_idx = np.searchsorted(cumf, pos_med) # índice de la clase mediana (primera cumf >= N/2)
L_med = intervalos[med_class_idx][0]          # límite inferior de la clase mediana
F_b = cumf[med_class_idx-1] if med_class_idx > 0 else 0  # frecuencia acumulada previa (F_{b})
f_m = f[med_class_idx]                        # frecuencia de la clase mediana
median_interp = L_med + ((pos_med - F_b) / f_m) * h  # interpolación lineal dentro de la clase

# --- Moda por interpolación (fórmula triangular) ---
modal_idx = np.argmax(f)                      # índice de la clase modal (máxima frecuencia)
L_mod = intervalos[modal_idx][0]              # límite inferior de la clase modal
f_prev = f[modal_idx-1] if modal_idx-1 >= 0 else 0   # frecuencia de la clase anterior (f_{i-1})
f_next = f[modal_idx+1] if modal_idx+1 < len(f) else 0 # frecuencia de la clase siguiente (f_{i+1})
mode_interp = L_mod + ((f[modal_idx] - f_prev) / (2*f[modal_idx] - f_prev - f_next)) * h

# --- Coeficiente de variación y sesgo (Pearson) ---
cv = std_muestral / mean_agr                  # coeficiente de variación (relativo)
skew_pearson = 3 * (mean_agr - median_interp) / std_muestral  # fórmula de Pearson (asimetría aproximada)

# --- Resumen impreso ---
print(f"N = {N}")
print(f"Media agrupada = {mean_agr:.6f} s")
print(f"Varianza muestral = {var_muestral:.6f} s^2")
print(f"Desviación estándar = {std_muestral:.6f} s")
print(f"Mediana interpolada = {median_interp:.6f} s")
print(f"Moda interpolada = {mode_interp:.6f} s")
print(f"CV = {cv:.4f} ({cv*100:.1f}%)")
print(f"Skewness (Pearson) = {skew_pearson:.3f}")

# --- Gráficos ---
# 1) Histograma por clases (barras por frecuencia) + marcas y líneas centrales
fig, ax = plt.subplots(figsize=(9,4))
left_edges = [iv[0] for iv in intervalos]    # límites inferiores para ubicar barras
right_edges = [iv[1] for iv in intervalos]   # límites superiores (no usados directamente en bar)
widths = [r-l for l,r in intervalos]         # anchos de cada clase

# barras (frecuencia absoluta)
ax.bar(left_edges, f, width=widths, align='edge', alpha=0.6, edgecolor='black')
ax.set_xlabel('Tiempo de respuesta (s)')
ax.set_ylabel('Frecuencia absoluta')
ax.set_title('Histograma por clases - tiempos de respuesta (API)')

# anotar media, mediana, moda
ax.axvline(mean_agr, color='k', linestyle='--', linewidth=1.3, label=f"Media {mean_agr:.3f}s")
ax.axvline(median_interp, color='C1', linestyle='-.', linewidth=1.3, label=f"Mediana {median_interp:.3f}s")
ax.axvline(mode_interp, color='C2', linestyle=':', linewidth=1.3, label=f"Moda {mode_interp:.3f}s")
ax.legend()

# 2) Polígono de frecuencias y ogiva en figura aparte
fig2, (ax1, ax2) = plt.subplots(1,2, figsize=(12,4))

# Polígono: puntos en marcas conectados
ax1.plot(marcas, f, marker='o', linestyle='-', linewidth=1.5)
ax1.set_xlabel('Marca de clase (s)')
ax1.set_ylabel('Frecuencia')
ax1.set_title('Polígono de frecuencias')

# Ogiva (frecuencia acumulada) — step en límites superiores
cum_rel = np.cumsum(f)
ax2.step([iv[1] for iv in intervalos], cum_rel, where='post', linewidth=1.5)
ax2.set_xlabel('Límite superior de clase (s)')
ax2.set_ylabel('Frecuencia acumulada')
ax2.set_title('Ogiva (frecuencia acumulada)')
ax2.axhline(N/2, color='gray', linestyle='--', linewidth=1)  # referencia horizontal N/2
ax2.axvline(median_interp, color='C1', linestyle='-.', linewidth=1)  # marca la mediana interpolada

plt.tight_layout()
plt.show()
