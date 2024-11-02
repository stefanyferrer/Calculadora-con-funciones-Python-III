import math
def funciones_constantes():
    while True:
        try:
            opcion = int(input("""
Funciones de constantes:
1. Valor de Pi
2. Valor de la constante matemática e
3. Valor de la constante τ
4. Valor del infinito positivo
5. Valor NaN (Not a Number)
6. Volver al menú principal
"""))

            if opcion == 6:
                return

            if opcion == 1:
                resultado = math.pi
            elif opcion == 2:
                resultado = math.e
            elif opcion == 3:
                resultado = math.tau
            elif opcion == 4:
                resultado = math.inf
            elif opcion == 5:
                resultado = math.nan

            print("El valor de la constante solicitada es:", resultado)

        except ValueError:
            print("Entrada inválida. Debe ingresar un número.")
