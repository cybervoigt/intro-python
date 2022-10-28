"""
Programa Divide
requisito: solicitar ao usuário para digitar 2 números e apresentar o resultado da divisão do numerador pelo denominador
Autor Ricardo Voigt
Data 27/10/2022
versão 1.0.0
"""

#entrada

print("Programa de divisão - informe 2 números\n\n")

numerador1 = input("digite o numerador: ")
denominador1 = input("digite o denominador: ")


resultado = ""


#processamento

numerador1 = float(numerador1)
denominador1 = float(denominador1)

if (denominador1 == 0):
    razao = 0
    resultado = "denominador NÃO pode ser zero!"
else:
    razao = numerador1 / denominador1
    resultado = f"A razão de {numerador1} por {denominador1} é {razao}"

#saída

print(resultado)
