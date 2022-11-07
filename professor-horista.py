"""
calcule o salario de um professor horista na Universidade XYZ.
O programa deve perguntar o numero de horas trabalhadas, calcular e imprimir na tela o valor do salario bruto,
do salario liquido e do total de descontos, sabendo que o desconto do imposto e 30% e que o valor da hora-aula e R$ 40,00.
Data 06/11/2022
Autor Ricardo Voigt (http://github.com/cybervoigt)
Versão 1.0.0.0
"""

#entrada

qtde_horas = input("Digite a quantidade de horas trabalhadas: ")

valor_hoaraula = 40.0

taxa_imposto = 0.3

#processamento

qtde_horas = int(qtde_horas)

valor_salario_bruto = qtde_horas * valor_hoaraula

valor_imposto = valor_salario_bruto * taxa_imposto

valor_salario_liquido = valor_salario_bruto - valor_imposto

#saida

print(f"Quantidade de horas: {qtde_horas}")
print(f"Valor hora-aula    : R$ {valor_hoaraula}")
print(f"Salario Bruto      : R$ {valor_salario_bruto}")
print(f"Taxa Imposto       : {taxa_imposto*100}%")
print(f"Valor Imposto      : R$ {valor_imposto}")
print(f"Salario Liquido    : R$ {valor_salario_liquido}")
