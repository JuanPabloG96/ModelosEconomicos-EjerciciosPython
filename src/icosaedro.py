import turtle
import time
import os

while True:
    side_length_str = input("Ingrese la longitud del lado del triángulo: ")
    line_color = input("Seleccione un color para la linea: ").lower()
    possible_colors = ["red", "green", "blue", "yellow", "purple", "orange", "black", "white"]

    try:
        side_length = int(side_length_str)
        if side_length <= 0:
            print("La longitud del lado debe ser un número positivo.")
            time.sleep(3)
            os.system("cls" if os.name == "nt" else "clear")
            continue
    except ValueError:
        print("El valor ingresado para la longitud del lado no es un número.")
        time.sleep(3)
        os.system("cls" if os.name == "nt" else "clear")
        continue

    if line_color not in possible_colors:
        print("Color no disponible. Los colores válidos son:")
        print(", ".join(possible_colors))
        time.sleep(3)
        os.system("cls" if os.name == "nt" else "clear")
        continue
    break
        

tina = turtle.Turtle()
tina.shape("turtle")
tina.width(3)
tina.penup()
tina.goto(0,60)
tina.pendown()
tina.color(line_color)

for i in range(3):
    tina.right(120)
    tina.forward(side_length)

tina.left(120)

for i in range(3):
    tina.forward(side_length)
    tina.left(120)
    tina.forward(side_length)

tina.right(90)
tina.forward(side_length * 0.6)
tina.right(120)

for i in range(6):
    if(i % 2 == 0):
        tina.right(60)
        tina.forward(side_length * 0.6)
        tina.right(180)
        tina.forward(side_length * 0.6)
        tina.right(120)
    tina.forward(side_length * 1.17)
    tina.right(60)

turtle.done()
