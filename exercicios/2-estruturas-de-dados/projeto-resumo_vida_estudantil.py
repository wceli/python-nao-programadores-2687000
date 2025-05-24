# Nesse exercício coletaremos dados de uma estudante, armazenaremos em um dicionário e imprimiremos na tela esse dados em um formato amigável.

# 1. Solicite a estudante os seguintes dados: nome, ano que conheceu o LinkedIn, ano atual e os cursos realizados no LinkedIn Learning separados por virgula em ordem cronológica
# 2. Armazene esses dados em um dicionário
# 3. Imprima na tela uma string com as informações de nome, ano_conheceu_linkedin, total de anos transcurridos, total de cursos realizados e (apenas) o primeiro e último curso.

nome = input('Informe seu nome: ')
ano_conheceu = input('Informe o ano em que conheceu o Linkedin: ')
ano_atual = input('Informe o ano atual: ')
cursos_str = input('cursos realizados no LinkedIn Learning separados por virgula em ordem cronológica: ')
cursos = [curso.strip() for curso in cursos_str.split(",")]
dados_estudante =  {
  "nome":nome,
  "ano_conheceu_linkedin": ano_conheceu,
  "ano_atual": ano_atual,
  "cursos":cursos
}
anos_transcorridos = int(dados_estudante['ano_atual']) - int(dados_estudante['ano_conheceu_linkedin'])
total_cursos = len(cursos)
primeiro_curso = cursos[0]
ultimo_curso = cursos[-1]

print(f"{dados_estudante['nome']} conheceu o linkedin em {dados_estudante['ano_conheceu_linkedin']} e nestes {anos_transcorridos} anos realizou {total_cursos} cursos, sendo o primeiro {primeiro_curso} e o mais recente {ultimo_curso}")