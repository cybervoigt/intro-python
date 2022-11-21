"""
funções de processamento do programa calculadora...
"""


def somar(a,b):
    return a + b

def subtrair(a,b):
    return a - b

def multiplicar(a,b):
    return a * b

def dividir(a,b):
    if b == 0:
        return "Não é possível dividir por zero"
    else:
        return a / b
