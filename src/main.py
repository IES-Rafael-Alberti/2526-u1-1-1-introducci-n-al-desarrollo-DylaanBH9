# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi():
    edad = 0
    nombre = input("¿Cual es tu nombre?: ")
    año_nacimiento = int(input("¿En que año naciste?: "))
    lenguaje = "Python"
    año_actual = 2025
    edad = año_actual - año_nacimiento
    print(f"Hola {nombre}, tienes {edad} años. Este programa está hecho en el lenguaje de programación: {lenguaje}")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
