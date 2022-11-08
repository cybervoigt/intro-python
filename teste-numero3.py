"""
Pequeno teste relacionado a uma pergunta dos exercicios...
"""

#entrada
x = input("Digite o número 3 ")

#processamento

frase = "..."

if x == 3:
    frase = "nunca vai entrar aqui neste IF pq x contem uma string !"

elif x == "3":
    frase = "agora sim... O número digitado está correto"

#saida
print(frase)