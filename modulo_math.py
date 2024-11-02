import math

def funcion_modulo_math():
    while True:
        try:
            opcion = int(input("""
Operaciones modulo math:
1. Raiz cuadrada
2. Devuelve el valor de e a la potencia de x
3. Logaritmación en la base que usted desee
4. Logaritmo en base 10 del valor ingresado
5. Logaritmo en base 2 del valor ingresado
6. Factorial de un número entero
7. Máximo común divisor
8. Raíz cuadrada entera
9. Copia el signo del segundo número en el primero
10. Devuelve el valor absoluto de un número como decimal
11. Devuelve el menor entero mayor o igual a su número
12. Devuelve el mayor entero mayor o igual a su número
13. Elimina la parte decimal de su número
14. Devuelve el valor del módulo de la división de 2 números
15. Devuelve el resto de la división de x entre y, ajustado al múltiplo más cercano de y                              
16. Devuelve el producto de todos los elementos de una lista     
17. Volver al menú anterior                                                                                                                                                  
"""))
            
            if opcion == 17:
                return

            if opcion in [1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15]:
                valor1 = float(input("Ingrese un número: "))

            if opcion in [3, 7, 14]:
                valor2 = float(input("Ingrese el segundo número: "))

            if opcion == 1:
                resultado = math.sqrt(valor1)
            elif opcion == 2:
                resultado = math.exp(valor1)
            elif opcion == 3:
                base = float(input("Ingrese la base (presione Enter para logaritmo natural): ") or math.e)
                resultado = math.log(valor1, base)
            elif opcion == 4:
                resultado = math.log10(valor1)
            elif opcion == 5:
                resultado = math.log2(valor1)
            elif opcion == 6:
                resultado = math.factorial(int(valor1))
            elif opcion == 7:
                a = int(input("Ingrese el primer número: "))
                b = int(input("Ingrese el segundo número: "))
                resultado = math.gcd(a, b)
            elif opcion == 8:
                resultado = math.isqrt(int(valor1))
            elif opcion == 9:
                y = float(input("Ingrese el signo: "))
                resultado = math.copysign(valor1, y)
            elif opcion == 10:
                resultado = math.fabs(valor1)
            elif opcion == 11:
                resultado = math.ceil(valor1)
            elif opcion == 12:
                resultado = math.floor(valor1)
            elif opcion == 13:
                resultado = math.trunc(valor1)
            elif opcion == 14:
                resultado = math.fmod(valor1, valor2)
            elif opcion == 15:
                resultado = math.remainder(valor1, valor2)
            elif opcion == 16:
                iterable = list(map(float, input("Ingrese los números de la lista separados por espacios: ").split()))
                resultado = math.prod(iterable)
            else:
                print("Opción no válida, por favor intente de nuevo.")
                continue

            print("El resultado de la operación es:", resultado)

        except ValueError:
            print("Entrada inválida. Debe ingresar un número.")

