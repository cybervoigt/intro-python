"""
Autor Ricardo Voigt (https://github.com/cybervoigt)

Exten3784: Turma I - Indicadores de Desempenho Institucional
MÓDULO 4 - AVALIANDO O SISTEMA DE MEDIÇÃO DE DESEMPENHO
Atividade de fixação: avaliação dos resultados

Pensei em abrir via Python a planilha que a professora disponibilizou
 e aplicar a regra via programação atualizando a coluna H (AVALIAÇÃO)
 conforme descrito abaixo, PORÉM eu não tenho certeza se entendi o exemplo:

Avaliação alcance das metas.xlsx

Na planilha em anexo, identifique se a meta foi ou não alcançada.
Importante estabelecer parâmetros para o alcance do aceitável.
Exemplo: Se a base é 20, a meta é 30 e se chegou a 25, como classificar?
Pode-se estabelecer parâmetros como:
 acima de 80% meta alcançada;
 60 a 79,99% meta aceitável
 e abaixo de 60% - meta não alcançada.

Biblioteca OpenPyXL
https://openpyxl.readthedocs.io/en/stable/

Requisito: instalar pacote openpyxl
 Com o programa "Anaconda Powershell Prompt" é possível criar um
 ambiente virtual contendo bibliotecas de terceiros baixadas da internet.

# criar o ambiente com nome 'excel_indicadores_1'
conda create -n excel_indicadores_1 python=3.9

# ativar/entrar neste ambiente
conda activate excel_indicadores_1

# instalar a biblioteca 'openpyxl' para manipular planilhas de excel
conda install openpyxl

# executar
python main.py
"""

from openpyxl import load_workbook

wb = load_workbook(filename = "Avaliação alcance das metas.xlsx")

planilha = wb['Planilha1']

planilha["I1"].value = "PARÂMETRO (%)"

# varre as linhas com dados, de 2 a 13
contador = 0
i = 2
while i <= 13:
    contador+= 1

    # entrada (dados da linha)
    #celD = f"D{i}" # VALOR BASE
    celE = f"E{i}" # META
    #celF = f"F{i}" # REGUA
    celG = f"G{i}" # RESULTADO 
    celH = f"H{i}" # AVALIAÇÃO (saída)
    celI = f"I{i}" # coluna nova, PARÂMETRO
    #valorbase = planilha[celD].value
    meta = planilha[celE].value
    #regua = planilha[celF].value
    resultado = planilha[celG].value

    # exibe na tela...
    #print(celD + " = "  + str(planilha[celD].value))

    # processamento
    # quanto % o resultado é da meta? só isso? 
    # aqui fiquei em dúvida, sobre o cálculo necessário...
    perc_resultado = (resultado * 100) / meta

    if perc_resultado >= 80:
        resultado = "1 - Alcançada"
    elif perc_resultado >= 60 :
        resultado = "2 - Aceitável"
    else:
        resultado = "3 - Não alcançada"

    # gambiarra para cortar e deixar só 2 casas decimais :-D
    corta = int(perc_resultado * 100)
    perc_resultado = corta / 100

    # saída
    planilha[celH].value = resultado
    planilha[celI].value = perc_resultado

    i+=1



wb.save("Avaliação alcance das metas FINAL.xlsx")
print(f"Quantidade de linhas atualizadas processadas: {contador}")
