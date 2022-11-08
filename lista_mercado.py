"""
Videoaula 02/11/2022 - 02/11/2022
Ler uma lista de compras digitada pelo usuario, e imprimir na tela
Autor Ricardo Voigt (https://github.com/cybervoigt)
Data 08/11
Versão 1.0.0.0
"""


#entrada

lista = []

#processamento

while True:
    item = input("digite o item da lista de compras: ")
    if item == "X":
        break
    lista.append(item)

#saida

print(f"lista de compras: {lista}")

