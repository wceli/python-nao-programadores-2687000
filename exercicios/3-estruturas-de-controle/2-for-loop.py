# Crie uma lista
cursos_linkedin = [
    "Excel para Iniciantes",
    "Comunicação Interpessoal",
    "Gestão do Tempo",
    "Introdução ao Python",
    "Liderança e Influência"
]
# Crie um for loop para imprimir cada elemento dessa lista

for curso in cursos_linkedin:
	print(curso)

# Crie um objeto iterável utilizando a função range()
print (list(range(10,40,2)))

# Use esse objeto iterável para criar um for loop que imprima na tela a frase "Estou aprendendo uma linguagem de programação."
for item in range(10,40,2):
	print (f'{item} - estou aprendendo python')