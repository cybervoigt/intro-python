"""
Aula sobre Entrada, processamento e saída
Requisito: Faça um programa que leia dois números inteiros, calcule a soma deles e imprima o resultado na tela.
Autor Ricardo Voigt (https://github.com/cybervoigt)
Data 31/10/2022
Versão 0.0.1
"""

#entrada

print("**** Ola, programa que apresenta a soma de 2 números ****\n\n")
num01 = input("Digite o primeiro número inteiro: ")
num02 = input("Digite o segundo número inteiro: ")

#processamento

# converte os numeros para inteiro...
# (vai dar erro caso tenha sido digitado algum numero inválido.)
num01 = int(num01)
num02 = int(num02)

#somar
soma = num01 + num02

#saida

print(f"\n\nA soma de {num01} e {num02} é {soma}\n\n")
