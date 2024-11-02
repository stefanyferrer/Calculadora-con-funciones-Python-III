import math
def funciones_avanzadas():
    while True:
        try:
            opcion = int(input("""
Otras funciones avanzadas:
1. Convertir un ángulo de radianes a grados
2. Convertir un ángulo de grados a radianes
3. Distancia euclidiana
4. Función de error gaussiana
5. Función complementaria de error
6. Función gamma
7. Logaritmo natural de la función gamma 
8. Volver al menú principal
"""))

            if opcion == 8:
                return

            if opcion in [1, 2]:
                valor1 = float(input("Ingrese un ángulo: "))

            if opcion == 3:
                p = tuple(map(float, input("Ingrese las coordenadas del punto p (x, y) separadas por espacios: ").split()))
                q = tuple(map(float, input("Ingrese las coordenadas del punto q (x, y) separadas por espacios: ").split()))

            if opcion == 1:
                resultado = math.degrees(valor1)
            elif opcion == 2:
                resultado = math.radians(valor1)
            elif opcion == 3:
                resultado = math.dist(p, q)
            elif opcion == 4:
                resultado = math.erf(valor1)
            elif opcion == 5:
                resultado = math.erfc(valor1)
            elif opcion == 6:
                resultado = math.gamma(valor1)
            elif opcion == 7:
                resultado = math.lgamma(valor1)

            print("El resultado de la operación es:", resultado)

        except ValueError:
            print("Entrada inválida. Debe ingresar un número.")