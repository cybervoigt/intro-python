"""
Autor Ricardo Voigt  (https://github.com/cybervoigt)
Data 22/11/22
Versão 0.0.0.1

módulo Python que encapsula rotinas 
de escrita da planilha, da biblioteca openpyxl
"""

from openpyxl import Workbook



def salvarplanilha(valor_salario,lista_despesas,valores_despesas):

    resultado = valor_salario


    arquivo = Workbook()

    # crie uma planilha chamada Novembro;
    Novembro = arquivo.active
    Novembro.title = "Novembro"

    # crie uma coluna chamada Receitas e registre o seu salario;
    Novembro["A1"] = "Receitas"
    Novembro["A2"] = valor_salario



    # crie uma coluna chamada Despesas ao lado a coluna Receitas
    # e registre seu gasto com despesas

    # nas linhas 1 e 2 vai o título e total de despesas
    linha = 3

    contador = 0
    total_despesas = 0
    for despesa in lista_despesas:

        valor_despesa  = valores_despesas[contador]
        contador+=1

        total_despesas+= valor_despesa
        resultado     -= valor_despesa

        Novembro[f"B{linha}"] = despesa
        Novembro[f"C{linha}"] = valor_despesa
        linha+=1

    Novembro["C1"] = "Despesas"
    Novembro["C2"] = total_despesas
    # alternativa, se eu quisesse que o Excell calculasse a soma
    # OBS: testei e não deu muito certo, pelo menos aqui no LibreOffice... :-(
    #Novembro["C2"] = f"=SOMA(C3:C{linha-1})"



    # crie uma coluna chamada Resultado e registre nela a diferenca entre receitas e despesas
    Novembro["D1"] = "Resultado"
    Novembro["D2"] = resultado
    # abaixo, a alternativa se eu quisesse colocar a formula da diferença dentro da planilha
    #Novembro["D2"] = "=A2-B2"


    # crie um arquivo chamado orcamento.xlsx;
    arquivo.save('orcamento.xlsx')

    return resultado
