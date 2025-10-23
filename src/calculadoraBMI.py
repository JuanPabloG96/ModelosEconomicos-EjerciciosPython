def bmi_metric(weight_kg: float, height_m: float) -> float:
    if height_m <= 0 or weight_kg <= 0:
        raise ValueError("Altura y peso deben ser mayores que 0.")
    return weight_kg / (height_m ** 2)
 
def bmi_imperial(weight_lb: float, height_in: float) -> float:
    if height_in <= 0 or weight_lb <= 0:
        raise ValueError("Altura y peso deben ser mayores que 0.")
    return 703.0 * weight_lb / (height_in ** 2)
 
def bmi_category(bmi: float) -> str:
    if bmi < 18.5:
        return "Bajo peso"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Sobrepeso"
    elif bmi < 35:
        return "Obesidad I"
    elif bmi < 40:
        return "Obesidad II"
    else:
        return "Obesidad III"
 
def main():
    print("Calculadora de IMC (BMI)")
    print("1) Sistema Métrico (kg, m)")
    print("2) Sistema Imperial (lb, in)")
    choice = input("Elige sistema [1/2]: ").strip()
 
    try:
        if choice == "1":
            w = float(input("Peso (kg): ").strip())
            h = float(input("Altura (m): ").strip())
            bmi = bmi_metric(w, h)
        elif choice == "2":
            w = float(input("Peso (lb): ").strip())
            h = float(input("Altura (in): ").strip())
            bmi = bmi_imperial(w, h)
        else:
            print("Opción no válida.")
            return
 
        cat = bmi_category(bmi)
        print(f"\nTu BMI es: {bmi:.2f}")
        print(f"Categoría (OMS): {cat}")
    except ValueError as e:
        print(f"Error: {e}")
 
if __name__ == "__main__":
    main()
