"""
módulo que vai encapsular a leitura do arquivo csv
e retornar uma lista dos dados desejados
baseado neste exemplo
https://www.hashtagtreinamentos.com/trabalhar-com-arquivos-csv-python
"""


# importar modulo 'csv' para ler arquivos CSV
import csv

nomearquivo = "ssp_dados.csv"

def lista_eixos(cidade):

    lista_tipos = []
    lista_bairros = []

    with open(nomearquivo,"r") as arquivo:
        arquivo_csv = csv.reader(arquivo,delimiter=';')
        for i, linha in enumerate(arquivo_csv):
            if i > 0:
                # variavel linha é uma lista
                # vou pegar apenas os itens que me interessam
                if linha[6] == cidade:

                    # Tipo Enquadramento
                    item_tipo = linha[4]

                    if not item_tipo in lista_tipos:
                        lista_tipos.append(item_tipo)

                    # Bairro -> converte para MAIÚSCULO
                    item_bairro = linha[8].upper()
                    if item_bairro == "":
                        item_bairro = "** NÃO INFORMADO **"

                    if not item_bairro in lista_bairros:
                        lista_bairros.append(item_bairro)

    # linhas e colunas...
    return [lista_tipos,lista_bairros]



# função que retorna a matriz tipos x bairros
def contar_dados(cidade,tipos,bairros):

    lista_result = []
    for tipo in tipos:
        item = []
        for bairro in bairros:
            item.append(0)
        lista_result.append(item)
            

    with open(nomearquivo,"r") as arquivo:
        arquivo_csv = csv.reader(arquivo,delimiter=';')
        for i, linha in enumerate(arquivo_csv):
            if i > 0:
                # variavel linha é uma lista
                if linha[6] == cidade:
                    # Tipo Enquadramento
                    item_tipo = linha[4]
                    # Bairro -> converte para MAIÚSCULO
                    item_bairro = linha[8].upper()
                    if item_bairro == "":
                        item_bairro = "** NÃO INFORMADO **"

                    lista_result[ tipos.index(item_tipo) ][ bairros.index(item_bairro) ] += 1

    return lista_result



# teste 1 - contar as linhas da cidade
def contador_cidade(cidade):

    #vamos começar contando quantas linhas tem no CSV 
    # da cidade informada...
    #lista_result = []
    contador = 0

    with open(nomearquivo,"r") as arquivo:
        arquivo_csv = csv.reader(arquivo,delimiter=';')
        for i, linha in enumerate(arquivo_csv):
            if i == 0:
                # cabecalho... no momento não preciso
                pass
            else:
                # variavel linha é uma lista
                # vou pegar apenas os itens que me interessam
                if linha[6] == cidade:
                    # Tipo Enquadramento
                    item_tipo = linha[4]
                    #lista_result.append(linha)
                    contador+=1
    return contador

