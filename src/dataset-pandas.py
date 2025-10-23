import os
import time
import pandas as pd

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def consultar_por_marca(data):
    marca = input("Ingrese la marca del vehículo: ").capitalize()
    resultados = data[data['Make'] == marca]

    if len(resultados) == 0:
        print(f"No se encontraron resultados para la marca '{marca}'.")
    else:
        print(f"Resultados para la marca '{marca}':")
        print(resultados)

    input("\nPresiona Enter para continuar...")
    clear_screen()

def consultar_por_precio(data):
    try:
        data_copia = data.copy()
        data_copia['MSRP_numerico'] = data_copia['MSRP'].str.replace('$', '', regex=False).str.replace(',', '', regex=False).astype(float)

        precio_str = input("Ingrese el precio de venta (MSRP): ")
        precio_limpio = precio_str.replace('$', '').replace(',', '')
        precio = float(precio_limpio)

        resultados = data_copia[data_copia['MSRP_numerico'] <= precio]
        resultados.drop(columns=['MSRP_numerico'], inplace=True)

        if len(resultados) == 0:
            print(f"No se encontraron resultados para el precio '{precio_str}'.")
        else:
            print(f"Resultados para el precio '{precio_str}':")
            print(resultados)

        input("\nPresiona Enter para continuar...")
        clear_screen()

    except ValueError:
        print("Entrada inválida. Por favor, ingresa un valor numérico.")
        time.sleep(2)
        clear_screen()

def consultar_por_tipo_de_traccion(data):
    traccion = input("Ingrese el tipo de tracción (Front, Rear, All): ").capitalize()
    resultados = data[data['DriveTrain'] == traccion]

    if len(resultados) == 0:
        print(f"No se encontraron resultados para la tracción '{traccion}'.")
    else:
        print(f"Resultados para la tracción '{traccion}':")
        print(resultados)
    
    input("\nPresiona Enter para continuar...")
    clear_screen()

def ordenar_por_potencia(data):
    print("Ordenando vehículos por Potencia (Horsepower)...")
    while True:
        orden = input("¿Deseas ordenar de forma ascendente (asc) o descendente (desc)? ").lower()
        if orden not in ['asc', 'desc']:
            print("Opción inválida. Por favor, ingresa 'asc' o 'desc'.")
            continue
        else:
            break
    
    ascendente = (orden == 'asc')
    resultados = data.sort_values(by='Horsepower', ascending=ascendente)
    
    print("\nVehículos ordenados por potencia:")
    print(resultados[['Make', 'Model', 'Horsepower']])
    
    input("\nPresiona Enter para continuar...")

def consultar_por_peso(data):
    try:
        peso = float(input("Ingrese un peso en libras para buscar (ej. 3500): "))
        condicion = input("¿Deseas ver vehículos más ligeros (<) o más pesados (>) que ese peso? ")

        if condicion == '<':
            resultados = data[data['Weight'] < peso]
        elif condicion == '>':
            resultados = data[data['Weight'] > peso]
        else:
            print("Condición inválida. Por favor, usa '<' o '>'.")
            return

        if len(resultados) == 0:
            print(f"No se encontraron resultados para la condición especificada.")
        else:
            print(f"Resultados para vehículos {condicion} a {peso} lbs:")
            print(resultados[['Make', 'Model', 'Weight']])

        input("\nPresiona Enter para continuar...")
        clear_screen()

    except ValueError:
        print("Entrada inválida. Por favor, ingresa un valor numérico.")
        time.sleep(2)
        clear_screen()
    

def menu():
    print("Consultar datos de un conjunto de datos en formato CSV")
    print("""
    1. Consultar por marca
    2. Consultar por precio (MSRP)
    3. Consultar por tipo de tracción
    4. Ordenar por potencia
    5. Consultar por peso
    6. Salir
    """)

if __name__ == '__main__':
    data = pd.read_csv('src/datasets/car_dataset.csv', encoding='latin1')
        
    while True:
        menu()
        
        seleccion = int(input("Elige una opción del menú (1-6): "))

        opciones = {
            1: lambda: consultar_por_marca(data),
            2: lambda: consultar_por_precio(data),
            3: lambda: consultar_por_tipo_de_traccion(data),
            4: lambda: ordenar_por_potencia(data),
            5: lambda: consultar_por_peso(data),
            6: exit
        }
        opciones[seleccion]()
