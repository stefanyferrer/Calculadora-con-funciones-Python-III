import math
def funciones_hiperbolicas():
    while True:
        try:
            opcion = int(input("""
Funciones hiperbólicas:
1. Seno hiperbólico
2. Coseno hiperbólico
3. Tangente hiperbólica
4. Arco seno hiperbólico
5. Arco coseno hiperbólico
6. Arco tangente hiperbólico
7. Volver al menú principal
"""))

            if opcion == 7:
                return

            valor1 = float(input("Ingrese un número: "))

            if opcion == 1:
                resultado = math.sinh(valor1)
            elif opcion == 2:
                resultado = math.cosh(valor1)
            elif opcion == 3:
                resultado = math.tanh(valor1)
            elif opcion == 4:
                resultado = math.asinh(valor1)
            elif opcion == 5:
                resultado = math.acosh(valor1)
            elif opcion == 6:
                resultado = math.atanh(valor1)

            print("El resultado de la operación es:", resultado)

        except ValueError:
            print("Entrada inválida. Debe ingresar un número.")