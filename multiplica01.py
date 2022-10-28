"""
programa multiplica
requisito: solicitar ao usuário 2 números e apresentar o resultado da multiplicação
autor Ricardo Voigt
data 27/10/2022
versão 1.0.0
"""

#entrada

print("este programa calcula o produto de 2 numeros digitados pelo Usuário.\n\n")

numero_1 = input("digite o fator 1: ")
numero_2 = input("digite o fator 2: ")

#processamento

numero_1 = float(numero_1)
numero_2 = float(numero_2)

multiplica = numero_1 * numero_2

#saida

print(f"a multiplicação de {numero_1} e {numero_2} é {multiplica} .")
