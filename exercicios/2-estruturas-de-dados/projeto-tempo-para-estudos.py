# Criaremos um script que imprimirá na tela o total de horas que uma pessoa estudou durante um determinado período:
# 1. Crie uma variável chamada "nome" e, usando o método input(), atribua a ela um nome;
nome = input('Digite o seu nome: ')
# 2. Crie uma variável chamada "total_dias" e, usando o método input(), solicite o total de dias dedicados ao estudo por semana;
total_dias = int(input('Informe quantos dias por semana estudou: '))
# 3. Crie uma variável chamada "total_horas" e, usanod o método input(), solicite a média de horas estudada por dia;
total_horas = int(input('Informe número de horas de estudo no dia: '))
# 4. Crie uma variável chamada "curso" e, usando o método input(), solicite o título do curso desejado;
curso = input('Qual curso está fazendo? ')
# 5. Imprima na tela uma frase informando o nome da estudante, o total_dias dedicados aos estudos, o total horas semanais e o curso.

total_estudo =  total_horas * total_dias
print(f"{nome} estudou {curso} em média {total_horas} horas por dia durante {total_dias} dias, totalizando uma média de  {total_estudo} horas de estudo semanais. ")
