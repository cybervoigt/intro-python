"""
organizando as funções de entrada
separadas em um módulo separado
"""



def entrada(lista_despesas):

    valorsalario = float(input("Digite o seu salario: "))

    # lista para guardar o valor de cada despesa
    valores_despesas = []

    # laço de repetição para o usuário digitar o valor de cada despesa
    for i in lista_despesas:
        valordespesa = float(input(f"Digite o valor da despesa [{i}] : "))
        valores_despesas.append(valordespesa)

    lista_result = [valorsalario,valores_despesas]

    return lista_result


def saida(lista_despesas,valorsalario,valores_despesas, resultado):
    print("\nPlanliha salva com sucesso!")
    print(f" (+) valor salario = {valorsalario}")
    print(f"     lista despesas = {lista_despesas}")
    print(f" (-) valores despesas = {valores_despesas}")
    print(f"\n\n (=) Resultado = {resultado}")
