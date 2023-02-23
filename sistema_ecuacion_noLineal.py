"""
Se desea resolver el sistema de ecuaciones no lineales
x + y + z + p = r + s + q + w
x^2 + y^2 + z^2 + p^2 = r ^2 + s^2 + q^2+ w^2
"""

from functools import reduce
from itertools import combinations

def suma(expresion:list)->int:
    resultado = 0
    for termino in expresion:
        resultado += termino
    return resultado
def potencia(expresion:list)->int:
    resultado = 0
    for termino in expresion:
        resultado += termino**2
    return resultado

def ecuacion_lineal(expresion_izquierda:list, expresion_derecha:list)->bool:
    return suma(expresion_izquierda) == suma(expresion_derecha)


def ecuacion_cuadratica(expresion_izquierda:list, expresion_derecha:list)->bool:
    return potencia(expresion_izquierda) == potencia(expresion_derecha)

n = int(input("¿Hasta que valor n desea encontrar? desde 1 hasta n: "))
listado = list(combinations(range(1,n),4)) 

with open('listado.txt', 'w') as archivo:
    for i in range(len(listado)):
        for j in range(1,len(listado)):
            if len(set(listado[i]) & set(listado[j])) == 0:
                if ecuacion_lineal(listado[i],listado[j]) and listado[i]!=listado[j]:
                    if ecuacion_cuadratica(listado[i],listado[j]):
                        archivo.write(f"Listado valido {listado[i]} y {listado[j]}\n")
      
#refactorizado por chatgpt
from itertools import combinations

def suma_r(expresion):
    return sum(expresion)

def potencia_r(expresion):
    return sum([termino**2 for termino in expresion])

def ecuacion_lineal_r(expresion_izquierda, expresion_derecha):
    return suma_r(expresion_izquierda) == suma_r(expresion_derecha)

def ecuacion_cuadratica_r(expresion_izquierda, expresion_derecha):
    return potencia_r(expresion_izquierda) == potencia_r(expresion_derecha)

with open('listado_refactorizado.txt', 'w') as archivo:
    for i, expr1 in enumerate(listado):
        for expr2 in listado[i+1:]:
            if not set(expr1) & set(expr2):
                if ecuacion_lineal_r(expr1, expr2) and expr1 != expr2:
                    if ecuacion_cuadratica_r(expr1, expr2):
                        archivo.write(f"{listado[i]} y {listado[j]}\n")

