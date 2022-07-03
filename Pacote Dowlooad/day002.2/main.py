#ARREDONDAR NUMEROS...
print (8/3) # da um numero com varias casas ex. 2.6666666666666665

# para arredondar de forma simples podemos transformar o resultado em um numero inteiro usando INT:
print (int(8/3)) 
# outra forma de transformar resultado de visão diretamente para inteiro é colocando //
print (8//3)

# o jeito melhor e mais certo é usar a função ROUND que é arredondar:  *ele irá arredondar para cima ou para baixo conforme a regra geral da matemática:
print (round(8/3))

# podemos definir quantas casas decimais queremos mostras após a virgula:
print (round(8/3, 2))

# somar ou diminuir o resultado de uma variavel é como no JS = +=, -=, *=:
resultado = 2+2
resultado += 2
print(resultado)

#FUNÇÃO F NAS STRINGS... JÁ APRENDIDO EM JS E ESQUECIDO:
#USAR A FUNÇÃO F PARA AGRUPAR STRINGS, NUMEROS, E VALORES BOLEANOS(TRUE E FALSE):
alt = 1.20
idade = 10
result = (alt >= 1.10)
print(result)
print(f"Você tem {alt} de altura e tem {idade} anos então isso é {result}!")
