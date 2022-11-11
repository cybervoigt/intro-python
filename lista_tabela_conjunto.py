"""
Diferença entre listas, tabelas/dicionarios e conjuntos/tuplas

"tuplas são listas que não podem ser alteradas, e contém itens únicos, que não se repetem"

Autor Ricardo Voigt (https://github.com/cybervoigt)
Data 08/11/22
Versão 1.0.0.0

"""

#entrada

print("incluindo um item nas listas")

# <class 'list'>
lista1 = []

# <class 'dict'>
lista2 = {}

# <class 'tuple'>
lista3 = ()



#processamento

contador = 0
while True:

    item = input("digite o item: ")
    if item == "X":
        break

    # adicionar o item na lista1
    lista1.append(item)

    # adicionar o item na lista2
    lista2[contador] = item

    # adicionar o item na lista3
    #lista3[contador] = item  # 'tuple' object does not support item assignment

    # teste criando outra lista simples e depois convertendo de volta para lista3
    listatemp = list(lista3) # desse jeito os itens da lista3 são inseridos na nova listatemp
    #listatemp = [lista3]     # desse jeito a lista3 é inserida como um item na nova listatemp
    listatemp.insert(contador, item)
    #listatemp.append(item)
    lista3 = tuple(listatemp)

    contador+=1
#atenção na identação, o bloco while vem até aqui na linha do contador+=1


#saida

print("\n\nTipo de cada lista:")
print("lista1 = " + str(type(lista1)) + " | quantidade de itens = " + str(len(lista1)))
print("lista2 = " + str(type(lista2)) + " | quantidade de itens = " + str(len(lista2)))
print("lista3 = " + str(type(lista3)) + " | quantidade de itens = " + str(len(lista3)))

print("\n\n")
itemlista1 = lista1[ 0 ]
itemlista2 = lista2[ 0 ]
itemlista3 = lista3[ 0 ]

print(f"item1 da lista1 = {itemlista1}")
print(f"item1 da lista2 = {itemlista2}")
print(f"item1 da lista3 = {itemlista3}")

print("\nconteudo das listas:")
print(f"lista1 = {lista1}")
print(f"lista2 = {lista2}")
print(f"lista3 = {lista3}")

