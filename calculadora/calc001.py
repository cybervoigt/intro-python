"""
Programa calculadora, com "programação modular" (com vários arquivos PY)
Baseado nas aulas dos dias 09/11/2022 14/11/2022
Requisistos : ler 2 numeros digitados pelo usuario e a operação desejada (+-*/)
 e apresente o resultado na tela
Autor: Ricardo Voigt (https://github.com/cybervoigt)
Data 21/11/2022
Versão 1.0.0.1
 Organizei em funções e a função entrada retorna 
 uma lista com todos os dados digitados pelo usuario
"""

#importação de modulos externos (outros arquivos py)
import model
import view

def main():

    #input
    dados = view.entrada()

    #processing
    if dados[2] == "+":
        resultado = model.somar(dados[0],dados[1])
    elif dados[2] == "-":
        resultado = model.subtrair(dados[0], dados[1])
    elif dados[2] == "*":
        resultado = model.multiplicar(dados[0], dados[1])
    elif dados[2] == "/":
        resultado = model.dividir(dados[0], dados[1])
    else:
        resultado = "operação desconhecida"

    #pensei em adicionar o resultado como mais um item na lista 'dados'
    # e passar apenas a lista para a função de saída..
    dados.append(resultado)

    #output
    view.saida(dados)


if __name__ == "__main__":
    main()