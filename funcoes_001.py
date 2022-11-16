"""
Exercicio com exemplos de funções...
Autor Ricardo Voigt (https://github.com/cybervoigt)
Data 10/11/22
Versao 1.0.0.1
"""

#entrada
def entrada():
    digitado = input("Digite um numero qualquer no teclado: ")
    numero = converte_strtofloat(digitado)
    return numero

#processamento
def dobro(num):
    return num + num

def converte_strtofloat(texto):
    return float(texto)

#saida
def saida(num,res):
    print(f"o dobro do número {num} é {res}")


#funcao principal

def main():

    valor = entrada()
    #print(f"o numero digitado foi {valor}")

    resultado = dobro(valor)

    saida(valor,resultado)


#execucao da funcao principal

# preparando para a "programação modular"
# quando um projeto terá vários arquivos PY
if __name__ == "__main__":
    main()

