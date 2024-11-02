def funciones_incorporadas():
    while True:
        try:
            opcion = int(input("""
Operaciones incorporadas:
1. Valor absoluto
2. Redondeo
3. Potenciación
4. Cociente y residuo de dividir dos números
5. Suma de los elementos de una colección
6. Devuelve el valor mínimo de un iterable
7. Devuelve el valor máximo de un iterable
8. Volver al menú principal
"""))

            if opcion == 8:
                return

            if opcion in [1, 2, 3, 4]:
                valor1 = float(input("Ingrese el primer número: "))

            if opcion in [3, 4]:
                valor2 = float(input("Ingrese el segundo número: "))

            if opcion == 1:
                resultado = abs(valor1)
            elif opcion == 2:
                resultado = round(valor1)
            elif opcion == 3:
                resultado = pow(valor1, valor2)
            elif opcion == 4:
                resultado = divmod(valor1, valor2)
            elif opcion == 5:
                iterable = list(map(float, input("Ingrese los números separados por espacios: ").split()))
                resultado = sum(iterable)
            elif opcion == 6:
                iterable = list(map(float, input("Ingrese los números separados por espacios: ").split()))
                resultado = min(iterable)
            elif opcion == 7:
                iterable = list(map(float, input("Ingrese los números separados por espacios: ").split()))
                resultado = max(iterable)
            else:
                print("Opción no válida, por favor intente de nuevo.")
                continue
            
            print("El resultado de la operación es:", resultado)

        except ValueError:
            print("Entrada inválida. Debe ingresar un número.")


