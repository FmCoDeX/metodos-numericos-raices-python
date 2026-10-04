# Programa: Utilidades para funciones matemáticas
# Propósito: Convertir una expresión escrita por el usuario
#            en una función que pueda ser evaluada en Python.
# Autor: FmCoDeX
# Fecha: 04/10/2026

import math


# Función que convierte una expresión matemática en texto
# en una función evaluable.
# Parámetro:
# expresion: ecuación ingresada por el usuario, tipo str.
# Retorna una función de una variable x.
def crear_funcion(expresion):

    def funcion(x):

        variables_permitidas = {
            "x": x,
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "sqrt": math.sqrt,
            "exp": math.exp,
            "log": math.log,
            "pi": math.pi,
            "e": math.e
        }

        return eval(
            expresion,
            {"__builtins__": {}},
            variables_permitidas
        )

    return funcion
