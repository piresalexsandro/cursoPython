# Em Python, como vimos anteriormente, as listas são sequências de
# elementos identificados por um índice representado por um número inteiro.
# Às vezes, no entanto, queremos utilizar alguma informação como índice de
# algum dado em vez de um índice numérico. Para isso, usamos os
# dicionários.
# Um dicionário nada mais é do que um tipo de dado usado para armazenar
# informações em pares chave-valor, na qual a chave tem um papel
# semelhante ao do índice numérico e o valor é o dado atribuído àquela
# chave. As chaves, da mesma forma que um índice numérico, devem ser
# únicas.

# Para criar um dicionário, os inputs devem estar entre chaves ({}) e
# separados por vírgula. Cada item do dicionário consiste em uma chave,
# seguido de dois pontos (:) e, por fim, um valor, como pode ser visto
# abaixo:

clientes = {'Boris' : 38, 'Malvo':45, 'Barak':62, 'Michelle':53, 'Cicero':25, "Moniele": 14}
print('{}'.format(clientes))
keys = [key for key in clientes]

# acessando dicionario por chave
print('Birth {} is {}'.format(keys[0],clientes['Boris']))

#alterando um dicionario
#uptdate - adicionando
clientes['Jay'] = 51
print(clientes)

#deletando um item no dicionario
del clientes['Cicero']
clientes.pop('Jay')
print(clientes)

#funçoes
print(len(clientes))

#in e not in
print('Jay' in clientes)
print('Jay' not in clientes)

# deleta um item aleatorio do dicionario
print( 'Deletei aleatoriamente: {}'.format(clientes.popitem()))
print(clientes)

#delta todos os itens do dicionario
# clientes.clear()

#retorna as chaves e valores do dicionario como tuplas
print("chaves do dicionário: {}".format(clientes.keys()))
print("valores do dicionário: {}".format(clientes.values()))




