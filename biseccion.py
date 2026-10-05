# Programa: Método de Bisección
# Propósito: Aproximar una raíz utilizando el método numérico
#            de Bisección.
# Autor: FmCoDeX
# Fecha: 04/10/2026


# Función que aplica el método de Bisección.
# Parámetros:
# funcion: función matemática ingresada por el usuario.
# a: extremo izquierdo del intervalo, tipo float.
# b: extremo derecho del intervalo, tipo float.
# iteraciones: cantidad de iteraciones, tipo int.
# Retorna la última aproximación de la raíz.
def metodo_biseccion(funcion, a, b, iteraciones=10):

    if funcion(a) * funcion(b) >= 0:

        raise ValueError(
            "El intervalo no cumple con f(a) * f(b) < 0."
        )

    print("\n")
    print("=" * 105)
    print("MÉTODO DE BISECCIÓN")
    print("=" * 105)

    encabezado = (
        f"{'k':<4}"
        f"{'a':<12}"
        f"{'b':<12}"
        f"{'f(a)':<12}"
        f"{'f(b)':<12}"
        f"{'x':<12}"
        f"{'f(x)':<12}"
        f"{'B - A':<12}"
    )

    print(encabezado)
    print("-" * 105)

    x = 0

    for k in range(1, iteraciones + 1):

        fa = funcion(a)
        fb = funcion(b)

        x = (a + b) / 2

        fx = funcion(x)

        diferencia = b - a

        print(
            f"{k:<4}"
            f"{a:<12.6f}"
            f"{b:<12.6f}"
            f"{fa:<12.6f}"
            f"{fb:<12.6f}"
            f"{x:<12.6f}"
            f"{fx:<12.6f}"
            f"{diferencia:<12.6f}"
        )

        if fa * fx < 0:

            b = x

        else:

            a = x

    print("-" * 105)

    print(
        f"\nRaíz aproximada después de "
        f"{iteraciones} iteraciones: {x:.8f}"
    )

    return x
