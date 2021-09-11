#criando uma lista
l = [1, 2, 3, 4, 'Santander', 33]
listUniType = [1, 2, 3, 4]
listMixType = ['Santander', 33]
lista = ['Santander', 7, 33, 1]

# acessandoitem de um a lista pelo indice
print(l[4])

# pegando partes de uma lista
print(lista[0:3])
print(lista[:2]) 
print(lista[3:])
print(lista[0:-1])

#Operações com listas
print("\nOperações com listas")
print(33 in l)
print(3 not in listUniType)
print(len(l))
print(min(listUniType))
print(max(listUniType))
print(sum(listUniType))
all = lista + l + lista + listMixType + listUniType
print(all)
