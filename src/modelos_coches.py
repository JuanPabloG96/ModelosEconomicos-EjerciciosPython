import pandas as pd
from time import sleep
import os

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
        
        # Calcular promedios
        promedio_precio = df["Precio"].mean()
        promedio_potencia = df["Potencia"].mean()
        promedio_tecnologia = df["Tecnologia"].mean()
        promedio_popularidad = df["Popularidad"].mean()
        tipo_combustible_comun = df["Tipo_combustible"].mode()[0]
        
        # Filtrar coches cercanos a los promedios (±10)
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
        
        # Calcular promedio de ventas
        if len(df_filtrado) > 0:
            promedio_ventas = int(df_filtrado["Coches_vendidos"].mean())
        else:
            # Si no hay coches que cumplan, usar promedio general
            promedio_ventas = int(df["Coches_vendidos"].mean())
        
        # Clasificar potencial
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
        
        # Definir segmentos ajustados al dataset real
        deportivos = df[(df["Potencia"] >= 300) & (df["Torque"] >= 400)]
        ecologicos = df[(df["Consumo"] <= 12.0) & (df["Emisiones"] <= 150) & (df["Tecnologia"] >= 4)]
        familiares = df[(df["Potencia"] >= 180) & (df["Potencia"] <= 280) & 
                       (df["Consumo"] >= 10.0) & (df["Consumo"] <= 18.0) & 
                       (df["Tecnologia"] >= 3)]
        economicos = df[(df["Potencia"] < 180) & (df["Consumo"] <= 15.0) & (df["Emisiones"] <= 180)]
        
        # Imprimir resultados
        print("\nCLUSTERING DE COCHES SIMILARES\n")
        print(f"Segmento DEPORTIVOS: {len(deportivos)} coches")
        print(f"Segmento ECOLÓGICOS: {len(ecologicos)} coches")
        print(f"Segmento FAMILIARES: {len(familiares)} coches")
        print(f"Segmento ECONÓMICOS: {len(economicos)} coches")
        print(f"\nTotal de coches analizados: {len(df)}")
        print("\nBasado en análisis de Potencia, Torque, Consumo, Tecnología y Emisiones")
        
        # Mostrar ejemplos de cada segmento
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

def main ():
    ...

if __name__ == "__main__":
    main()
