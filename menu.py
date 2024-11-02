import Incorporadas
import modulo_math
import trigonometricas
import hiperbolicas
import constantes
import avanzadas

def menu():
    #Inicio del programa mostrando el menù principal
    print("¡Bienvenido a su calculadora con funciones avanzadas!")
    opcion=None
    while True:
            try:
                print("\nMenú principal:")
                print("1. Funciones incorporadas")
                print("2. Funciones del módulo math")
                print("3. Funciones trigonométricas")
                print("4. Funciones hiperbólicas")
                print("5. Funciones de constantes")
                print("6. Otras funciones avanzadas")
                print("0. Salir")

                opcion = input("Seleccione una opción: ")

                if opcion == '1':
                    Incorporadas.funciones_incorporadas()
                elif opcion == '2':
                    modulo_math.funcion_modulo_math()
                elif opcion == '3':
                    trigonometricas.funciones_trigonometricas()
                elif opcion == '4':
                    hiperbolicas.funciones_hiperbolicas()
                elif opcion == '5':
                    constantes.funciones_constantes()
                elif opcion == '6':
                    avanzadas.funciones_avanzadas()
                elif opcion == '0':
                    print("Saliendo...")
                    break
                else:
                    print("Opción no válida, por favor intente de nuevo.")
            except ValueError:
                print("Entrada inválida. Debe ingresar un número.")
menu()