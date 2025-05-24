# Crie uma lista apenas com elementos numéricos
numericos = [1,4,8,12,16,20]
print(numericos)

# Crie uma lista contendo todos os tipos e estrutura de dados que você aprendeu até agora
mista = [3,1.3,'sábado', [4,5,6]]
print (mista) 

# Imprima na tela apenas os 5 primeiros elementos da lista

print(numericos[0:5])
print(numericos[0:])
print(numericos[:5])
# Crie um slice na lista para que imprima na tela os elementos de índice par

print(numericos[0:-1:2])

# Remova da lista o último item
numericos.pop()
print(numericos)
numericos.pop()
print(numericos)
# Insira na lista um novo item
numericos.append(32)
print (numericos)

# Remova da lista um item específico
numericos.remove(8)
print(numericos)