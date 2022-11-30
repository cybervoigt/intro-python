"""
https://openpyxl.readthedocs.io/en/stable/

Requisito: instalar pacote openpyxl
 Com o programa "Anaconda Powershell Prompt" é possível criar um
 ambiente virtual contendo bibliotecas de terceiros baixadas da internet.

# criar o ambiente com nome 'excel_X'
conda create -n excel_2 python=3.9

# ativar/entrar neste ambiente
conda activate excel_X

# instalar a biblioteca 'openpyxl' para manipular planilhas de excel
conda install openpyxl

"""

from openpyxl import Workbook



def salvar_planilha(cidade,linhas,colunas,matriz):

    arquivo = Workbook()

    # criar uma planilha/aba dentro do Workbook
    planilha = arquivo.active
    planilha.title = "Planilha"


    # agora insere os dados na planilha

    # Adiciona uma linha com o nome das colunas, que são os bairros.
    planilha.append( colunas )

    # função enumerate consigo pegar o indice de cada item ao mesmo tempo...
    for i,tipo in enumerate(linhas):
        planilha.append( matriz[i] )


    # cria o arquivo XLSX;
    nomearq = f"final_{cidade}.xlsx"
    arquivo.save(nomearq)
    return nomearq
