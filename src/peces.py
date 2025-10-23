import pandas as pd

def encontrar_peces_rentables(data):
    # Criterio 1: Peces premium (alto valor y fertilidad)
    peces_premium = data[
        (data['Valuation'] > 20) &
        (data['Fertility rate'] > 5) &
        (data['Socialization'] >= 4)
    ].copy()
    
    # Criterio 2: Peces estándar (buen balance costo-beneficio)
    peces_estandar = data[
        (data['Socialization'] >= 4) &
        (data['Cost of food'] <= 0.80) &
        (data['Maintenance'] <= 0.80) &
        (data['Growing time'] <= 0.80) &
        (data['Fertility rate'] >= 0.4) &
        (data['Valuation'] >= 15) &
        ~data.index.isin(peces_premium.index)  # Excluir los que ya están en premium
    ].copy()
    
    # Combinar ambos grupos
    peces_filtrados = pd.concat([peces_premium, peces_estandar])
    
    print(f"Peces premium (alto valor/fertilidad): {len(peces_premium)}")
    if len(peces_premium) > 0:
        print("PECES PREMIUM")
        print(peces_premium[['Instance', 'Crappie', 'Socialization', 'Valuation', 'Fertility rate', 'Cost of food', 'Maintenance']])
    
    print(f"\nPeces estándar (balanceado): {len(peces_estandar)}")
    if len(peces_estandar) > 0:
        print("PECES ESTÁNDAR")
        print(peces_estandar[['Instance', 'Crappie', 'Socialization', 'Valuation', 'Fertility rate', 'Cost of food', 'Maintenance']])
    
    print(f"\nTotal de peces que cumplen los criterios: {len(peces_filtrados)}")
    
    return peces_filtrados

def main():
    print("ANÁLISIS DE PECES RENTABLES\n")
    
    try:
        # Cargar datos
        file_path = "src/datasets/peces_dataset.xlsx"
        data = pd.read_excel(file_path, sheet_name=0)
        
        print(f"Total de peces en dataset: {len(data)}")
        
        # Encontrar peces rentables
        encontrar_peces_rentables(data)
            
    except FileNotFoundError:
        print("Error: No se pudo encontrar el archivo Excel")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()
