"""
Projeto: Manipulando Planilhas Excel
Escreva um programa Python modularizado que faca o seguinte:
1. crie um arquivo chamado orcamento.xlsx;
2. crie uma planilha chamada Novembro;
OBS 1: fiz o programa pedir para o usuário digitar os dados abaixo :-)
3. crie uma coluna chamada Receitas e registre o seu salario;
4. crie uma coluna chamada Despesas ao lado a coluna Receitas e registre
seu gasto com alimentacao, energia e transporte, e
5. crie uma coluna chamada Resultado e registre nela a diferenca entre receitas e despesas, e
6. imprima na tela o resultado.

OBS 2: Por causa da dependencia com a biblioteca openpyxl, 
    este programa NÃO rodou aqui direto no Terminal do Visual Studio Code,
    só conseugui rodar ele dentro do Anaconda Powershell Prompt.
OBS 3: Eu movi código de entrada e saida para módulo view.

Autor Ricardo Voigt  (https://github.com/cybervoigt)
Data 22/11/22
Versão 0.0.0.2
"""

import view
import gravarplanilha


def main():

    lista_despesas = ["alimentacao", "energia", "transporte"]

    # entrada
    dados_entrada    = view.entrada(lista_despesas)

    # processamento
    valorsalario     = dados_entrada[0]
    valores_despesas = dados_entrada[1]
    resultado        = gravarplanilha.salvarplanilha(lista_despesas,valorsalario,valores_despesas)

    # saida
    # 6. imprima na tela o resultado
    view.saida(lista_despesas,valorsalario,valores_despesas, resultado)



if __name__ == "__main__":
    main()