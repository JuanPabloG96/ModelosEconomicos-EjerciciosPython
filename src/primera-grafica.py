import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
   'Generation': ['Female generation z', 'Male generation z', 'Female generation y', 'Male generation y', 'Female generation x', 'Male generation x', 'Female generation w', 'Male generation w', 'Female generation y millenials', 'Male generation y millenials'] * 8,
   'Resource sharing': [5.88, 2.11, 3.67, 3.63, 3.54, 4.38, 5.25, 5.32, 2.84, 6.56] * 8,
   'Geographical distribution': [3.96, 5.44, 5.74, 3.38, 1.98, 4.65, 6.56, 4.03, 6.23, 6.99] * 8,
   'Resource heterogeneity': [5.73, 4.13, 3.37, 6.51, 5.21, 4.82, 4.65, 4.93, 4.49, 5.47] * 8,
   'Structure homogeneity': [3.82, 2.05, 4.08, 2.48, 2.39, 3.15, 3.73, 5.97, 2.22, 6.14] * 8,
   'Interoperability': [6.17, 2.46, 6.49, 3.98, 1.83, 1.17, 5.25, 6.22, 6.76, 2.85] * 8,
   'Capacity': [5.27, 5.58, 6.35, 6.22, 5.31, 1.43, 6.39, 6.17, 2.35, 3.13] * 8,
   'Distribution of workloads': [3.05, 3.39, 5.97, 6.84, 2.45, 5.38, 5.09, 4.22, 2.51, 3.39] * 8,
   'Virtualization support': [4.58, 3.16, 4.51, 3.77, 5.18, 1.41, 2.92, 2.01, 3.64, 3.53] * 8
}
df_long = pd.DataFrame(data)

# Usar melt para tener todas las métricas en una sola columna
df_melted = pd.melt(df_long, id_vars=['Generation'], var_name='Metric', value_name='Value')

# Crear el gráfico de dispersión tipo swarm plot
plt.figure(figsize=(12, 8))
sns.swarmplot(x='Generation', y='Value', hue='Generation', data=df_melted, dodge=False)
plt.title('Gráfico de Dispersión de Todas las Métricas por Generación')
plt.xlabel('Generación')
plt.ylabel('Valor de la Métrica')
plt.xticks(rotation=45, ha='right')
plt.legend(title='Generación', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.savefig('single_scatter_plot.png')
plt.show()
