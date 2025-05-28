# Nesse desafio você verificará dentro de uma lista se o item estar contido nela, caso verdadeiro deverá imprimir na tela essa informação, além disso deverá solicitar avaliação para o item e armazená-la em um dicionário.
# 1. Crie uma lista com 5 diferentes cursos do LinkedIn Learning
# 2. Crie 3 variáveis do tipo string e associe 1 curso a cada uma delas
# 3. Crie um dicionário vazio para armazenar a nota do curso
# 4. Crie uma estrutura condicional para verificar se cada variável está contida na lista
# 5. Se o curso estiver na lista, solicite uma nota para avaliação
# 6. Armazene essa nota no dicionário, sendo a chave o título do curso e o valor a nota
cursos_linkedin = [
    "Excel para Iniciantes",
    "Comunicação Interpessoal",
    "Gestão do Tempo",
    "Introdução ao Python",
    "Liderança e Influência"
]
curso1 = 'Excel para Iniciantes'
curso2 = 'Introdução ao Python'
curso3 = 'Liderança e seus liderados'
nota_curso = {}

if curso1 in cursos_linkedin:
  print(f'O curso {curso1} está no catálogo. Por favor, avalie o curso')
  nota_curso[curso1] = int(input('Informe a nota que você dá para o curso (0 a 5)'))

if curso2 in cursos_linkedin:
  print(f'O curso {curso2} está no catálogo. Por favor, avalie o curso')
  nota_curso[curso2] = int(input('Informe a nota que você dá para o curso (0 a 5)'))

if curso3 in cursos_linkedin:
  print(f'O curso {curso3} está no catálogo. Por favor, avalie o curso')
  nota_curso[curso3] = int(input('Informe a nota que você dá para o curso (0 a 5)'))

else:
  print('Infelizmente o curso não compõe o nosso catálogo')

print(nota_curso)