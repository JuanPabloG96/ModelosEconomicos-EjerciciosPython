import numpy as np
import matplotlib.pyplot as plt
 
# Datos iniciales
valor_inicial = 500000  # Valor inicial del brazo robótico en pesos
años = 10                # Periodo de depreciación
tasa_depreciacion = 0.15 # 15% anual de depreciación
np.random.seed(42)       # Para reproducibilidad
 
# Listas para almacenar valores
valores = []
valores_fluctuados = []
 
# Cálculo de la depreciación anual con fluctuaciones
for año in range(años + 1):
    valor = valor_inicial * ((1 - tasa_depreciacion) ** año)
    fluct = np.random.normal(0, valor * 0.03)  # Fluctuaciones del 3% alrededor del valor
    valor_con_fluctuacion = valor + fluct
    valores.append(valor)
    valores_fluctuados.append(valor_con_fluctuacion)
 
# Generar el gráfico
plt.figure(figsize=(10,6))
plt.plot(range(años + 1), valores, marker='o', linestyle='-', color='blue', label='Depreciación Lineal')
plt.plot(range(años + 1), valores_fluctuados, marker='x', linestyle='--', color='red', label='Valor con Fluctuaciones')
plt.title('Fluctuaciones Financieras de un Brazo Robótico')
plt.xlabel('Años')
plt.ylabel('Valor (MXN)')
plt.grid(True)
plt.legend()
plt.show()
