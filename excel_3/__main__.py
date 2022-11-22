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

Autor Ricardo Voigt  (https://github.com/cybervoigt)
Data 22/11/22
Versão 0.0.0.1
"""

import gravarplanilha


def main():

    valorsalario = float(input("Digite o seu salario: "))

    lista_despesas = ["alimentacao", "energia", "transporte"]

    # lista para guardar o valor de cada despesa
    valores_despesas = []

    # laço de repetição para o usuário digitar o valor de cada despesa
    for i in lista_despesas:
        valordespesa = float(input(f"Digite o valor da despesa [{i}] : "))
        valores_despesas.append(valordespesa)

    resultado = gravarplanilha.salvarplanilha(valorsalario,lista_despesas,valores_despesas)

    # 6. imprima na tela o resultado
    print("\nPlanliha salva com sucesso!")
    print(f" (+) valor salario = {valorsalario}")
    print(f"     lista despesas = {lista_despesas}")
    print(f" (-) valores despesas = {valores_despesas}")
    print(f"\n\n (=) Resultado = {resultado}")



if __name__ == "__main__":
    main()