# Criaremos um programa para substituir números por palavras em uma lista
# 1. Crie uma lista com 15 números
# 2. Crie um for loop para percorrer todos os elementos da lista
# 3. Crie uma estrutura condicional para verificar cada número da lista:
# 3.1 Caso o número seja divisível por 3, substitua-o por "Fizz"
# 3.2 Caso o número seja divisível por 5, substitua-o por "Buzz"
# 3.3 Caso o número seja divisível por 3 e 5, substitua-o por "FizzBuzz"

lista_numerica = list(range(15,31))
indice = 0
print (f'lista antes do processamento: {lista_numerica}')
for item_lista in lista_numerica:
  if (item_lista%3 == 0) and (item_lista%5 == 0):
    lista_numerica[indice] = 'FizzBuzz'
  elif (item_lista%3 == 0):
    lista_numerica[indice] = 'Fizz'
  elif (item_lista%5 == 0):
    lista_numerica[indice] = 'Buzz'
  else: 
    lista_numerica[indice] = item_lista
  indice += 1
print(f'lista depois do processo {lista_numerica}')
