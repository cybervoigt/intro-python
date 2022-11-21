"""
Mesmo código do arquivo original calc001.py mas com a diferença que agora
 este programa roda passando apenas o nome da pasta, com esse comando "python calculadora"
Autor: Ricardo Voigt (https://github.com/cybervoigt)
Data 21/11/2022
Versão 1.0.0.0
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
