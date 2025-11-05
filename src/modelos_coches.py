import os
from time import sleep
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def mostrar_categorias(categorias):
    for i, categoria in enumerate(categorias):
        print(f"{i+1}. {categoria}")

def clasificar_eficiencia_popularidad():
    dataset_file = "src/datasets/Modelos_Coches_Dataset.xlsx"
    
    BAJO_PRECIO = 30
    ALTO_PRECIO = 70
    BAJA_EMISION = 120
    POPULAR = 9.0
    POTENTE = 250
    POCO_VENDIDO = 1000

    categorias = [
        "Ecologico y popular",
        "Economico, pero poco vendido",
        "Potente y caro"
    ]
    
    try:
        df_completo = pd.read_excel(dataset_file, sheet_name=0)

        columnas_deseadas = ["Modelo", "Marca", "Precio", "Potencia", "Emisiones", "Popularidad", "Coches_vendidos"]
        df = df_completo[columnas_deseadas]   

        while True:
            mostrar_categorias(categorias)
            
            try:
                opcion = int(input("Selecciona una categoria: "))

                seleccion_categoria = {
                    1: df[(df["Emisiones"] <= BAJA_EMISION) & (df["Popularidad"] >= POPULAR)],
                    2: df[(df["Precio"] <= BAJO_PRECIO) & (df["Coches_vendidos"] <= POCO_VENDIDO)],
                    3: df[(df["Potencia"] >= POTENTE) & (df["Precio"] >= ALTO_PRECIO)]
                }

                return seleccion_categoria[opcion]

            except ValueError:
                print("Favor de ingresar un numero valido.")
                sleep(2)
                limpiar_pantalla()
        
    except FileNotFoundError:
        print(f"Error: El archivo no fue encontrado en la ruta: {dataset_file}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

def predecir_ventas():
    dataset_file = "src/datasets/Modelos_Coches_Dataset.xlsx"
    
    try:
        df_completo = pd.read_excel(dataset_file, sheet_name=0)
        columnas_deseadas = ["Modelo", "Marca", "Precio", "Potencia", "Tecnologia", "Popularidad", "Tipo_combustible", "Coches_vendidos"]
        df = df_completo[columnas_deseadas]
        
        promedio_precio = df["Precio"].mean()
        promedio_potencia = df["Potencia"].mean()
        promedio_tecnologia = df["Tecnologia"].mean()
        promedio_popularidad = df["Popularidad"].mean()
        tipo_combustible_comun = df["Tipo_combustible"].mode()[0]
        
        TOLERANCIA = 10
        df_filtrado = df[
            (df["Precio"] >= promedio_precio - TOLERANCIA) & 
            (df["Precio"] <= promedio_precio + TOLERANCIA) &
            (df["Potencia"] >= promedio_potencia - TOLERANCIA) & 
            (df["Potencia"] <= promedio_potencia + TOLERANCIA) &
            (df["Tecnologia"] >= promedio_tecnologia - TOLERANCIA) & 
            (df["Tecnologia"] <= promedio_tecnologia + TOLERANCIA) &
            (df["Popularidad"] >= promedio_popularidad - TOLERANCIA) & 
            (df["Popularidad"] <= promedio_popularidad + TOLERANCIA) &
            (df["Tipo_combustible"] == tipo_combustible_comun)
        ]
        
        if len(df_filtrado) > 0:
            promedio_ventas = int(df_filtrado["Coches_vendidos"].mean())
        else:
            promedio_ventas = int(df["Coches_vendidos"].mean())
        
        if promedio_ventas < 1000:
            clasificacion = "Bajo"
        elif promedio_ventas <= 3000:
            clasificacion = "Medio"
        else:
            clasificacion = "Alto"
        
        resultado = f"\nSegún las categorías de Precio, Potencia, Tecnología, Popularidad y Tipo_combustible hemos determinado que la cantidad de unidades que se venderán será de: {promedio_ventas:,}, lo que se considera un potencial de venta {clasificacion}."
        
        return resultado
        
    except FileNotFoundError:
        return f"Error: El archivo no fue encontrado en la ruta: {dataset_file}"
    except Exception as e:
        return f"Ocurrió un error: {e}"

def clustering_coches_similares():
    dataset_file = "src/datasets/Modelos_Coches_Dataset.xlsx"
    
    try:
        df_completo = pd.read_excel(dataset_file, sheet_name=0)
        columnas_deseadas = ["Modelo", "Marca", "Potencia", "Torque", "Consumo", "Tecnologia", "Emisiones"]
        df = df_completo[columnas_deseadas]
        
        deportivos = df[(df["Potencia"] >= 300) & (df["Torque"] >= 400)]
        ecologicos = df[(df["Consumo"] <= 12.0) & (df["Emisiones"] <= 150) & (df["Tecnologia"] >= 4)]
        familiares = df[(df["Potencia"] >= 180) & (df["Potencia"] <= 280) & 
                       (df["Consumo"] >= 10.0) & (df["Consumo"] <= 18.0) & 
                       (df["Tecnologia"] >= 3)]
        economicos = df[(df["Potencia"] < 180) & (df["Consumo"] <= 15.0) & (df["Emisiones"] <= 180)]
        
        print("\nCLUSTERING DE COCHES SIMILARES\n")
        print(f"Segmento DEPORTIVOS: {len(deportivos)} coches")
        print(f"Segmento ECOLÓGICOS: {len(ecologicos)} coches")
        print(f"Segmento FAMILIARES: {len(familiares)} coches")
        print(f"Segmento ECONÓMICOS: {len(economicos)} coches")
        print(f"\nTotal de coches analizados: {len(df)}")
        print("\nBasado en análisis de Potencia, Torque, Consumo, Tecnología y Emisiones")
        
        print("\nEjemplos por segmento\n")
        
        if len(deportivos) > 0:
            print("DEPORTIVOS:")
            for i, row in deportivos.head(3).iterrows():
                print(f"  - {row['Marca']} {row['Modelo']}")
        
        if len(ecologicos) > 0:
            print("\nECOLÓGICOS:")
            for i, row in ecologicos.head(3).iterrows():
                print(f"  - {row['Marca']} {row['Modelo']}")
        
        if len(familiares) > 0:
            print("\nFAMILIARES:")
            for i, row in familiares.head(3).iterrows():
                print(f"  - {row['Marca']} {row['Modelo']}")
        
        if len(economicos) > 0:
            print("\nECONÓMICOS:")
            for i, row in economicos.head(3).iterrows():
                print(f"  - {row['Marca']} {row['Modelo']}")
        
    except FileNotFoundError:
        print(f"Error: El archivo no fue encontrado en la ruta: {dataset_file}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

def visualizacion_seguridad_tecnologia():
    dataset_file = "src/datasets/Modelos_Coches_Dataset.xlsx"
    
    try:
        df_completo = pd.read_excel(dataset_file, sheet_name=0)
        columnas_deseadas = ["Marca", "Tipo_combustible", "Seguridad", "Tecnologia"]
        df = df_completo[columnas_deseadas]
        
        plt.figure(figsize=(12, 8))
        
        pivot_marca = df.groupby('Marca')[['Seguridad', 'Tecnologia']].mean()
        sns.heatmap(pivot_marca, annot=True, cmap='YlOrRd', fmt='.1f')
        plt.title('Heatmap: Seguridad vs Tecnología por Marca')
        plt.tight_layout()
        plt.show()
        
        plt.figure(figsize=(10, 6))
        pivot_combustible = df.groupby('Tipo_combustible')[['Seguridad', 'Tecnologia']].mean()
        sns.heatmap(pivot_combustible, annot=True, cmap='YlOrRd', fmt='.1f')
        plt.title('Heatmap: Seguridad vs Tecnología por Tipo de Combustible')
        plt.tight_layout()
        plt.show()
        
        print("\nVISUALIZACIÓN COMPLETADA")
        print("Se han generado heatmaps de Seguridad vs Tecnología por Marca y Tipo de Combustible")
        
    except FileNotFoundError:
        print(f"Error: El archivo no fue encontrado en la ruta: {dataset_file}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

def comparacion_rendimiento_combustible():
    dataset_file = "src/datasets/Modelos_Coches_Dataset.xlsx"
    
    try:
        df_completo = pd.read_excel(dataset_file, sheet_name=0)
        columnas_deseadas = ["Tipo_combustible", "Potencia", "Consumo"]
        df = df_completo[columnas_deseadas]
        
        # Filtrar solo los tipos de combustible principales
        combustibles_principales = ['Gasolina', 'Diésel', 'Eléctrico', 'Híbrido']
        df_filtrado = df[df['Tipo_combustible'].isin(combustibles_principales)]
        
        plt.figure(figsize=(15, 6))
        
        # Gráfico de Potencia
        plt.subplot(1, 2, 1)
        sns.boxplot(data=df_filtrado, x='Tipo_combustible', y='Potencia')
        plt.title('Potencia por Tipo de Combustible')
        plt.xlabel('Tipo de Combustible')
        plt.ylabel('Potencia (HP)')
        plt.xticks(rotation=45)
        
        # Gráfico de Consumo
        plt.subplot(1, 2, 2)
        sns.boxplot(data=df_filtrado, x='Tipo_combustible', y='Consumo')
        plt.title('Consumo por Tipo de Combustible')
        plt.xlabel('Tipo de Combustible')
        plt.ylabel('Consumo (100km)')
        plt.xticks(rotation=45)
        
        plt.tight_layout()
        plt.show()
        
        print("\nCOMPARACIÓN DE RENDIMIENTO")
        print("Se han generado boxplots de Potencia y Consumo por Tipo de Combustible")
        
        stats = df_filtrado.groupby('Tipo_combustible').agg({
            'Potencia': ['count', 'mean', 'median', 'std'],
            'Consumo': ['mean', 'median', 'std']
        }).round(1)
        
        print("\nESTADÍSTICAS POR TIPO DE COMBUSTIBLE:")
        print(stats)
        
    except FileNotFoundError:
        print(f"Error: El archivo no fue encontrado en la ruta: {dataset_file}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

def optimizacion_multicriterio():
    dataset_file = "src/datasets/Modelos_Coches_Dataset.xlsx"
    
    try:
        df_completo = pd.read_excel(dataset_file, sheet_name=0)
        columnas_deseadas = ["Modelo", "Marca", "Precio", "Consumo", "Tecnologia", "Popularidad"]
        df = df_completo[columnas_deseadas].copy()
        
        df_normalizado = df.copy()
        df_normalizado['Precio_norm'] = 1 - (df['Precio'] - df['Precio'].min()) / (df['Precio'].max() - df['Precio'].min())
        df_normalizado['Consumo_norm'] = 1 - (df['Consumo'] - df['Consumo'].min()) / (df['Consumo'].max() - df['Consumo'].min())
        df_normalizado['Tecnologia_norm'] = (df['Tecnologia'] - df['Tecnologia'].min()) / (df['Tecnologia'].max() - df['Tecnologia'].min())
        df_normalizado['Popularidad_norm'] = (df['Popularidad'] - df['Popularidad'].min()) / (df['Popularidad'].max() - df['Popularidad'].min())
        
        df_normalizado['Puntuacion_ideal'] = (
            df_normalizado['Consumo_norm'] * 0.4 +
            df_normalizado['Tecnologia_norm'] * 0.3 +
            df_normalizado['Precio_norm'] * 0.2 +
            df_normalizado['Popularidad_norm'] * 0.1
        )
        
        top_5 = df_normalizado.nlargest(5, 'Puntuacion_ideal')[['Modelo', 'Marca', 'Precio', 'Consumo', 'Tecnologia', 'Popularidad', 'Puntuacion_ideal']]
        
        print("\nTOP 5 COCHES IDEALES (Menor consumo, Mayor tecnología, Menor precio, Más popularidad)")
        print("=" * 80)
        
        for i, (idx, row) in enumerate(top_5.iterrows(), 1):
            print(f"{i}. {row['Marca']} {row['Modelo']}")
            print(f"   Precio: ${row['Precio']:,.2f}K | Consumo: {row['Consumo']:.1f} L/100km")
            print(f"   Tecnología: {row['Tecnologia']}/5 | Popularidad: {row['Popularidad']}/10")
            print(f"   Puntuación ideal: {row['Puntuacion_ideal']:.3f}\n")
        
        return top_5
        
    except FileNotFoundError:
        print(f"Error: El archivo no fue encontrado en la ruta: {dataset_file}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

def analisis_tendencias_color():
    dataset_file = "src/datasets/Modelos_Coches_Dataset.xlsx"
    
    try:
        df_completo = pd.read_excel(dataset_file, sheet_name=0)
        columnas_deseadas = ["Color", "Coches_vendidos", "Precio", "Tipo_combustible", "Popularidad"]
        df = df_completo[columnas_deseadas]
        
        print("\nANÁLISIS DE TENDENCIAS DE COLOR")
        print("=" * 50)
        
        ventas_por_color = df.groupby('Color').agg({
            'Coches_vendidos': 'sum',
            'Precio': 'mean',
            'Popularidad': 'mean',
            'Tipo_combustible': lambda x: x.mode()[0] if len(x.mode()) > 0 else 'N/A'
        }).sort_values('Coches_vendidos', ascending=False)
        
        ventas_por_color['Coches_vendidos'] = ventas_por_color['Coches_vendidos'].astype(int)
        color = ['blue', 'black', 'yellow', 'green', 'gray', 'silver', 'red']
        
        print("\nVENTAS Y CARACTERÍSTICAS POR COLOR:")
        print(ventas_por_color.round(2))
        
        plt.figure(figsize=(12, 8))
        
        plt.subplot(2, 2, 1)
        ventas_por_color['Coches_vendidos'].plot(kind='bar', color=color)
        plt.title('Ventas Totales por Color')
        plt.ylabel('Coches Vendidos')
        plt.xticks(rotation=45)
        
        plt.subplot(2, 2, 2)
        ventas_por_color['Precio'].plot(kind='bar', color=color)
        plt.title('Precio Promedio por Color')
        plt.ylabel('Precio')
        plt.xticks(rotation=45)
        
        plt.subplot(2, 2, 3)
        ventas_por_color['Popularidad'].plot(kind='bar', color=color)
        plt.title('Popularidad Promedio por Color')
        plt.ylabel('Popularidad (1-10)')
        plt.xticks(rotation=45)
        
        plt.tight_layout()
        plt.show()
        
        color_mas_vendido = ventas_por_color.index[0]
        ventas_color_mas_vendido = ventas_por_color.iloc[0]['Coches_vendidos']
        
        print(f"\nCONCLUSIÓN: El color más vendido es '{color_mas_vendido}' con {ventas_color_mas_vendido:,} unidades")
        
    except FileNotFoundError:
        print(f"Error: El archivo no fue encontrado en la ruta: {dataset_file}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

def menu():
    print("SISTEMA DE ANÁLISIS DE VEHÍCULOS")
    print("1. Clasificar por eficiencia y popularidad")
    print("2. Predecir ventas")
    print("3. Clustering de coches similares")
    print("4. Visualización seguridad vs tecnología")
    print("5. Comparación rendimiento por combustible")
    print("6. Optimización multi-criterio")
    print("7. Análisis tendencias de color")
    print("8. Salir")
    
    try:
        opcion = int(input("\nSelecciona una opción (1-8): "))
        return opcion
    except ValueError:
        print("Error: Por favor ingresa un número válido.")
        sleep(2)
        return -1

def main():
    funciones = {
        1: lambda: print("\n", clasificar_eficiencia_popularidad()),
        2: lambda: print("\n", predecir_ventas()),
        3: lambda: clustering_coches_similares(),
        4: lambda: visualizacion_seguridad_tecnologia(),
        5: lambda: comparacion_rendimiento_combustible(),
        6: lambda: optimizacion_multicriterio(),
        7: lambda: analisis_tendencias_color(),
        8: lambda: exit()
    }
    
    while True:
        limpiar_pantalla()
        opcion = menu()
        
        if opcion in funciones:
            limpiar_pantalla()
            titulos = {
                1: "CLASIFICACIÓN POR EFICIENCIA Y POPULARIDAD",
                2: "PREDICCIÓN DE VENTAS", 
                3: "CLUSTERING DE COCHES SIMILARES",
                4: "VISUALIZACIÓN SEGURIDAD VS TECNOLOGÍA",
                5: "COMPARACIÓN RENDIMIENTO POR COMBUSTIBLE",
                6: "OPTIMIZACIÓN MULTI-CRITERIO",
                7: "ANÁLISIS TENDENCIAS DE COLOR"
            }
            if opcion in titulos:
                print(titulos[opcion])
            funciones[opcion]()
            if opcion != 8:
                input("\nPresiona Enter para continuar...")
        else:
            print("Opción no válida. Por favor selecciona una opción entre 1 y 8.")
            sleep(2)

if __name__ == "__main__":
    main()
