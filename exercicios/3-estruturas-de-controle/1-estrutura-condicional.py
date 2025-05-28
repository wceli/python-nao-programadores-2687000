# Declare 4 variáveis do tipo numérica
x = 5
y = 30
z = 10
w = 3

# Crie uma estrutura condicional para comparar dois números
if x > y:
  print(f'o valor de {x} é maior que {y}')
elif x < y:
  print(f'o valor de {x} é menor que {y}')
else:
  print(f'Na verdade {y} é o maior número.')

# Se a condição for verdadeira, imprima na tela uma mensagem informando que a condição foi cumprida e informando o número de maior valor


# Se a condição não for cumprida, imprima na tela uma mensagem informando que a condição é negativa e informe o número de maior valor


# Insira outras condições na estrutura condicional usando o elif


# Incremente a estrutura condicional já existente com expressões lógicas utilizando "and" ou "or"


# Crie uma estrutura condicional onde mais de uma condição seja verdadeira, e use apenas a palavra reservada "if"
x = int(input('valor x: '))
y = int(input('valor y: '))
div = x%2

if (x > y) and (div == 0):
  print(f'{x} é maior que {y} e é um número par.')
else:
  if div != 0:
   print(f'{x} não é um número par')
  elif x<y:
    print(f'{x} na verdade é menor que {y}')