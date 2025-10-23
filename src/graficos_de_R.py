import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from typing import cast

def moda(serie):
    return serie.mode().iloc[0]

def calcular_estadisticas(df: pd.DataFrame) -> pd.DataFrame:
    aggs = {
        'Estatura': ['mean', 'median', 'std'],
        'Popularidad': ['mean', 'median', 'std'],
        'Vocal': ['mean', 'median', 'std']
    }
    
    resumen_df = df.groupby('Genero').agg(aggs)
    
    resumen_df.columns = ['_'.join(map(str, col)) for col in resumen_df.columns.values]
    
    resumen_df = cast(pd.DataFrame, resumen_df)

    resumen_df['Moda_Estatura'] = df.groupby('Genero')['Estatura'].apply(moda)
    resumen_df['Moda_Popularidad'] = df.groupby('Genero')['Popularidad'].apply(moda)
    resumen_df['Moda_Vocal'] = df.groupby('Genero')['Vocal'].apply(moda).round(2)

    mapeo_nombres = {
        'Estatura_mean': 'Media_Estatura',
        'Estatura_median': 'Mediana_Estatura',
        'Estatura_std': 'SD_Estatura',
        'Popularidad_mean': 'Media_Popularidad',
        'Popularidad_median': 'Mediana_Popularidad',
        'Popularidad_std': 'SD_Popularidad',
        'Vocal_mean': 'Media_Vocal',
        'Vocal_median': 'Mediana_Vocal',
        'Vocal_std': 'SD_Vocal',
        'Moda_Estatura': 'Moda_Estatura',
        'Moda_Popularidad': 'Moda_Popularidad',
        'Moda_Vocal': 'Moda_Vocal'
    }
    
    resumen_df = resumen_df.rename(columns=mapeo_nombres)

    cols_orden = [
        'Media_Estatura', 'Mediana_Estatura', 'Moda_Estatura', 'SD_Estatura',
        'Media_Popularidad', 'Mediana_Popularidad', 'Moda_Popularidad', 'SD_Popularidad',
        'Media_Vocal', 'Mediana_Vocal', 'Moda_Vocal', 'SD_Vocal'
    ]
    
    return resumen_df[cols_orden].round(2)

def generar_grafico(df: pd.DataFrame):
    sns.set_theme(style="whitegrid", rc={
        'figure.facecolor': '#0f1724',
        'axes.facecolor': '#0f1724',
        'text.color': 'white',
        'axes.labelcolor': 'white',
        'xtick.color': 'white',
        'ytick.color': 'white',
        'grid.color': '#334155'
    })
    
    plt.figure(figsize=(12, 8))
    palette = {"Hombre": "#3b82f6", "Mujer": "#f472b6"}
    
    sns.scatterplot(
        data=df,
        x='Popularidad',
        y='Vocal',
        size='Estatura', 
        hue='Genero',
        palette=palette,
        alpha=0.7,
        sizes=(100, 1000)
    )
    
    for i in range(len(df)):
        plt.text(
            df['Popularidad'].iloc[i], 
            df['Vocal'].iloc[i] + 0.05,
            df['Integrante'].iloc[i], 
            horizontalalignment='center', 
            size='small', 
            color='white'
        )
    
    plt.title("Timbiriche: Popularidad vs Desempeño Vocal", color='white', fontsize=16)
    plt.xlabel("Popularidad en el escenario", color='white', fontsize=12)
    plt.ylabel("Desempeño Vocal", color='white', fontsize=12)
    
    legend = plt.legend(title='Genero', loc='lower right', facecolor='#0f1724', edgecolor='white')
    plt.setp(legend.get_title(), color='white')
    plt.setp(legend.get_texts(), color='white')

    plt.tight_layout()
    plt.show()

def analizar_popularidad_por_estilo(df: pd.DataFrame):
    print("\n\n--- Análisis 1: Popularidad por Estilo ---")
    
    resumen_estilo = df.groupby('Estilo')['Popularidad'].mean().reset_index(name='Popularidad_prom')
    resumen_estilo = resumen_estilo.sort_values(by='Popularidad_prom', ascending=False)
    
    print("\nPopularidad Promedio por Estilo:")
    print(resumen_estilo.to_markdown(floatfmt=".2f"))

    plt.figure(figsize=(10, 6))
    estilos_ordenados = resumen_estilo['Estilo']
    
    sns.barplot(
        data=resumen_estilo,
        x='Popularidad_prom',
        y='Estilo',
        hue='Estilo', 
        palette='viridis',
        order=estilos_ordenados,
        legend=False
    ) 

    for index, row in resumen_estilo.iterrows():
        plt.text(
            row['Popularidad_prom'], 
            index, 
            f"{row['Popularidad_prom']:.2f}", 
            color='black', 
            ha="left", 
            va="center", 
            fontsize=10, 
            fontweight='bold'
        )

    plt.title("Popularidad promedio por estilo de interpretación", fontsize=14, fontweight='bold')
    plt.xlabel("Popularidad promedio")
    plt.ylabel("Estilo de interpretación")
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

def analizar_indice_musical_por_instrumento(df: pd.DataFrame):
    print("\n\n--- Análisis 2: Índice Musical por Instrumento ---")
    
    df['IndiceMusical'] = (df['Popularidad'] + df['Vocal']) / 2
    
    instrumentos = df['Instrumento'].unique()
    estilos = df['Estilo'].unique()
    
    palette = sns.color_palette("hsv", len(instrumentos))
    
    plt.figure(figsize=(12, 8))
    
    ax = sns.scatterplot(
        data=df,
        x='IndiceMusical',
        y='ID',
        hue='Instrumento',
        style='Estilo',
        s=200,
        palette=palette,
        markers=True
    )

    for i in range(len(df)):
        ax.text(
            df['IndiceMusical'].iloc[i] + 0.01,
            df['ID'].iloc[i],
            df['Integrante'].iloc[i],
            horizontalalignment='left',
            size='small',
            color='black'
        )

    plt.title("Gráfico de Integrantes por Índice Musical", fontsize=16)
    plt.xlabel("Índice Musical (Promedio Popularidad + Desempeño Vocal)")
    plt.ylabel("Integrante (ID)")
    plt.yticks(df['ID'], df['Integrante'])
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()

def analizar_vestuario_simulacion_3d(df: pd.DataFrame):
    print("\n\n--- Análisis 3: Vestuario y Simulación 3D ---")

    df['Precio_Final'] = df['Coste_Total'] * (1 + df['Norma_MX035'] / 10)
    df['Tamaño_Punto_Mpl'] = df['Precio_Final'] / 10
    
    plt.figure(figsize=(10, 7))
    colores_map = {"Hombre": "blue", "Mujer": "pink"}
    
    sns.scatterplot(
        data=df,
        x='Horas_Hombre',
        y='Huella_Carbono',
        hue='Genero',
        palette=colores_map,
        size='Tamaño_Punto_Mpl',
        sizes=(100, 800),
        alpha=0.8,
        legend='full'
    )
    
    plt.title("Simulación 3D: Precio Final del Vestuario representado por tamaño", fontsize=14)
    plt.xlabel("Horas Hombre")
    plt.ylabel("Huella de Carbono")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend(title='Género', loc='upper right')
    
    plt.tight_layout()
    plt.show()

    plt.show()

from datos.timbiriche import INFORMACION_TIMBIRICHE_EXTENDIDA

def main():
    data = pd.DataFrame(INFORMACION_TIMBIRICHE_EXTENDIDA)

    analizar_popularidad_por_estilo(data)
    analizar_indice_musical_por_instrumento(data)
    analizar_vestuario_simulacion_3d(data)

if __name__ == "__main__":
    main()
