"""
Programa calculadora, com "programação modular" (com vários arquivos PY)
Baseado nas aulas dos dias 09/11/2022 14/11/2022
Requisistos : ler 2 numeros digitados pelo usuario e a operação desejada (+-*/)
 e apresente o resultado na tela
Autor Ricardo Voigt (https://github.com/cybervoigt)
Data 21/11/2022
Versão 1.0.0.0
"""

#print(__name__)

#ENTRADA

numero_1 = input("Digite o primeiro numero: ")
numero_2 = input("Digite o segundo numero: ")
operacao = input("Digite a operacao desejada: ")


#PROCESSAMENTO

numero_1 = float(numero_1)
numero_2 = float(numero_2)

if operacao == "+":
    resultado = numero_1 + numero_2
elif operacao == "-":
    resultado = numero_1 - numero_2
elif operacao == "*":
    resultado = numero_1 * numero_2
elif operacao == "/":
    if numero_2 == 0:
        resultado = "Não é possível dividir por zero"
    else:
        resultado = numero_1 / numero_2
else:
    resultado = "operação desconhecida"


#SAÍDA

print(f"Resultado : {resultado}")
