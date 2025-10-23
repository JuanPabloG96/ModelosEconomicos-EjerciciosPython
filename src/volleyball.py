import matplotlib.pyplot as plt
import pandas as pd
from calculadoraBMI import bmi_metric
 
# Datos de los 37 países (ahora con la misma longitud en todas las listas)
data = {
    'País': ['Brasil', 'EE.UU.', 'Argentina', 'México', 'Canadá', 'Italia', 'Alemania', 'Francia', 'Australia', 'España', 
             'Rusia', 'Polonia', 'Noruega', 'Suecia', 'Japón', 'Tailandia', 'Corea del Sur', 'China', 'Chile', 'Colombia',
             'Venezuela', 'Perú', 'Puerto Rico', 'Cuba', 'Costa Rica', 'Ecuador', 'República Dominicana', 'Paraguay', 
             'Uruguay', 'Sudáfrica', 'Nueva Zelanda', 'Bélgica', 'Finlandia', 'Suiza', 'Holanda', 'Portugal', 'Wales', 
             'Serbia', 'Croacia', 'Bulgaria'],
    'Altura (m)': [1.94, 1.92, 1.91, 1.89, 1.90, 1.88, 1.87, 1.86, 1.85, 1.84, 1.92, 1.89, 1.91, 1.92, 1.90, 1.88, 1.85, 
                   1.86, 1.89, 1.91, 1.83, 1.80, 1.88, 1.85, 1.90, 1.87, 1.86, 1.80, 1.87, 1.82, 1.85, 1.88, 1.90, 1.92, 
                   1.91, 1.87, 1.89, 1.96, 1.98, 2.01],
    'Peso (kg)': [85, 92, 88, 83, 89, 87, 82, 80, 85, 79, 91, 84, 88, 86, 83, 85, 86, 80, 84, 85, 77, 75, 82, 85, 79, 
                  80, 74, 81, 79, 83, 88, 89, 91, 86, 84, 80, 78, 84, 91, 97]
}

# Calcular bmi
data['BMI'] = []

for i in range(len(data['País'])):
    bmi = bmi_metric(data['Peso (kg)'][i], data['Altura (m)'][i])
    data['BMI'].append(bmi) 

# Crear un DataFrame
df = pd.DataFrame(data)
 
# Crear la gráfica
fig, ax = plt.subplots(figsize=(12, 8))

# Colocar los puntos de los países seleccionados en azul
selected_countries = ['Brasil', 'EE.UU.', 'Argentina']  # Países de interés
df['Color'] = df['País'].apply(lambda x: 'blue' if x in selected_countries else 'green')

# Graficar todos los países
ax.scatter(df['Altura (m)'], df['Peso (kg)'], c=df['Color'], s=100)

# Etiquetas y título
ax.set_xlabel('Altura (m)')
ax.set_ylabel('Peso (kg)')
ax.set_title('Altura vs Peso de países en Voleibol de Playa (Hombres)')

# Añadir los nombres de los países
for i, row in df.iterrows():
    ax.text(row['Altura (m)'], row['Peso (kg)'], row['País'], fontsize=9)

plt.show()

