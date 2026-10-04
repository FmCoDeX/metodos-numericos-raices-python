# Programa: Métodos Numéricos - Cálculo de raíces
# Propósito: Interfaz principal para ejecutar los métodos de Bisección
#            y Regla Falsa para aproximar raíces de una función.
# Autor: FmCoDeX
# Fecha: 04/10/2026

from metodos.biseccion import metodo_biseccion
from metodos.regla_falsa import metodo_regla_falsa
from utilidades.funciones import crear_funcion


# Función que muestra el menú principal de la aplicación.
# No recibe parámetros.
# No retorna valores.
def mostrar_menu():
    print("\n" + "=" * 55)
    print("        MÉTODOS NUMÉRICOS - CÁLCULO DE RAÍCES")
    print("=" * 55)
    print("1. Método de Bisección")
    print("2. Método de Regla Falsa")
    print("3. Salir")
    print("=" * 55)


# Función que solicita al usuario los datos necesarios para aplicar
# alguno de los métodos numéricos.
# Retorna la función matemática y los extremos a y b.
def solicitar_datos():

    print("\nEjemplo de función:")
    print("x**3 - x - 2")
    print("x**2 - 4")
    print("x**3 + 4*x**2 - 10")

    expresion = input("\nIngrese f(x): ")

    funcion = crear_funcion(expresion)

    a = float(input("Ingrese el valor de a: "))
    b = float(input("Ingrese el valor de b: "))

    return funcion, a, b


# Función principal que controla la ejecución del programa.
# No recibe parámetros.
# No retorna valores.
def main():

    while True:

        mostrar_menu()

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":

            try:

                funcion, a, b = solicitar_datos()

                metodo_biseccion(
                    funcion,
                    a,
                    b,
                    iteraciones=10
                )

            except Exception as error:

                print("\nError:", error)

        elif opcion == "2":

            try:

                funcion, a, b = solicitar_datos()

                metodo_regla_falsa(
                    funcion,
                    a,
                    b,
                    iteraciones=10
                )

            except Exception as error:

                print("\nError:", error)

        elif opcion == "3":

            print("\nPrograma finalizado.")
            print("Gracias por utilizar FmCoDeX 💙")

            break

        else:

            print("\nOpción no válida.")


if __name__ == "__main__":
    main()
