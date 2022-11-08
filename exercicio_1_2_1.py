"""
https://moodle.ufrgs.br/pluginfile.php/5532977/mod_resource/content/2/lista1Python.pdf

Leia um numero e imprima na tela o seu dobro se ele for menor do que 10.
Se o numero for de 10 ate 20, imprima a sua metade.
Em qualquer outro caso, imprima na tela que o numero nao e valido.

Autor Ricardo Voigt (https://github.com/cybervoigt)
Data 7/11/2022
Versao 1.0.0.0
"""

#entrada

numero = input("digite o numero : ")

#processamento

numero = int(numero)

if numero < 10:
    resultado = numero * 2
    frase = f"Dobro de {numero} eh {resultado}"
elif numero >= 10 and numero <= 20:
    resultado = numero / 2
    frase = f"Metade de {numero} eh {resultado}"
else:
    frase = "Numero nao eh valido..."


#saida

print(frase)
