"""
Módulo com a função que vai ajustar os titulos
 e totalizar as linhas e colunas da matriz...

"""


# função que soma o total de cada linha, e adiciona
#  mais uma coluna no final com esse valor total
def total_linhas(matriz):
    for i,linha in enumerate(matriz):
        soma = 0
        for j,item in enumerate(linha):
            soma+=item
        linha.append(soma)

# função que soma o total de cada coluna e adiciona
# mais uma linha ao final da matriz com esses totais
def total_colunas(matriz):
    # inicializa a lista vazia
    linhasoma = []

    for i,linha in enumerate(matriz):

        #inicializa os itens zerados na lista
        if len(linhasoma) == 0:
            for x in linha:
                linhasoma.append(0)

        for j,item in enumerate(linha):
            linhasoma[j]+=item

    matriz.append(linhasoma)


# adiciona o TÍTULO (posição zero=coluna A) em cada linha da matriz
def ajuste_titulo_coluna(matriz,linhas):
    for i,tipo in enumerate(linhas):
        matriz[i].insert(0,tipo)
