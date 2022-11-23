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

# estrutura de repetição "infinita"
while True:
    item = input("digite o item da lista de compras: ")
    # controle para o usuário digitar X e sair do laço de repetição
    if item == "X":
        break
    # adiciona o item na lista
    lista.append(item)

#saida

print(f"lista de compras: {lista}")

# listando os itens um abaixo do outro
print("\nlistando um item abaixo do outro:")
for item in lista:
    print(item)

