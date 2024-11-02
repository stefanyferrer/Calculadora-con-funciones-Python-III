import math
def funciones_trigonometricas():
    while True:
        try:
            opcion = int(input("""
Funciones trigonométricas:
1. Seno en radianes
2. Coseno en radianes
3. Tangente en radianes
4. Arco seno en radianes
5. Arco coseno en radianes
6. Arco tangente en radianes
7. Arco tangente de uno de los valores, teniendo en cuenta los signos para seleccionar el cuadrante correcto
8. Hipotenusa de un triángulo rectángulo
9. Volver al menú principal
"""))

            if opcion == 9:
                return

            if opcion in [1, 2, 3, 4, 5, 6, 7, 8]:
                if opcion in [1, 2, 3]:
                    valor1 = float(input("Ingrese un ángulo en radianes: "))
                elif opcion in [4, 5]:
                    valor1 = float(input("Ingrese un número en el rango [-1, 1]: "))
                elif opcion == 7:
                    y = float(input("Ingrese el valor de y: "))
                    x = float(input("Ingrese el valor de x: "))
                    resultado = math.atan2(y, x)
                    print("El resultado de la operación es:", resultado)
                    continue
                else:
                    x = float(input("Ingrese la longitud del lado x: "))
                    y = float(input("Ingrese la longitud del lado y: "))
                    resultado = math.hypot(x, y)

            if opcion == 1:
                resultado = math.sin(valor1)
            elif opcion == 2:
                resultado = math.cos(valor1)
            elif opcion == 3:
                resultado = math.tan(valor1)
            elif opcion == 4:
                resultado = math.asin(valor1)
            elif opcion == 5:
                resultado = math.acos(valor1)
            elif opcion == 6:
                resultado = math.atan(valor1)

            print("El resultado de la operación es:", resultado)

        except ValueError:
            print("Entrada inválida. Debe ingresar un número.")