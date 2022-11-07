"""
Programa de calcular passagem
Requisito: Faça um programa que calcule o valor gasto 
com passagem de ônibus de um grupo de 20 pessoas,
sabendo que o preço unitário da passagem é R$ 7,30.
Autor Ricardo Voigt (https://github.com/cybervoigt)
Data 31/10/2022
Versão 0.0.2
Funcionalidade: solicita ao usuário digitar a quantidade de passageiros.
"""

#entrada

precounitario = 7.3
qtdepassageiros = input("Digite a quantidade de passageiros: ")

#processamento

qtdepassageiros = int(qtdepassageiros)

valortotal = precounitario * qtdepassageiros

#saída

print(f"Valor unitario da passagem: {precounitario}")
print(f"Para a quantidade de passagens {qtdepassageiros}, o valor total das passagens é: R$ {valortotal}")
