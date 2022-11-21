"""
exemplos de operações com lista
Autor Ricardo Voigt (https://github.com/cybervoigt)
Data 16/11/2022
Versão 1.0.0.0
"""


#entrada (criar uma lista)
lista = []


#processamento (incluir itens na lista e fazer operações)

while True:
    item = input("digite alguma coisa: ")
    if item == "X":
        break
    lista.append(item)


lista2 = sorted(lista)

#saida (apresentar resultado na tela...)

print(f"lista original: {lista}")
print(f"lista ordenada: {lista2}")

