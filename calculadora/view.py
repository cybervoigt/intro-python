"""
funções de entrada e saída do programa calculadora
'entrada()' retorna uma lista com 3 itens (numero 1, numero 2 e operacao)
e 'saida()' recebe uma lista com 4 itens (os mesmos 3 itens da entrada, e o resultado)
Autor: Ricardo Voigt (https://github.com/cybervoigt)
Data 21/11/2022
Versão 1.0.0.0
"""


def entrada():
    lista = []
    i = 0
    while i < 2:
        numero = input(f"Digite o numero [{i+1}] : ")
        numero = float(numero)
        lista.append(numero)
        i+=1

    operacao = input("""Operações Disponíveis:
    + Adição
    - Subtração
    * Multiplicação
    / Divisão
    Digite a operação desejada: """)
    lista.append(operacao)
    return lista


def saida(resultado):
    print(f"\n\nO resultado da operação '{resultado[0]}  {resultado[2]}  {resultado[1]}' é: {resultado[3]}\n\n")