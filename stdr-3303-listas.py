lista_unica = [1,2,3,4,5,6,7,8,9,0]
lista_mista = ['Maria', 70, 74, 'Julio']
lista = ['Santander', 7, 33, 1]
lista1 = [7, 5, 33, 1]
lista2 = [2, 3, 4]

print("{}".format(lista_unica[3]))
print("{}".format(lista_mista[3]))
print("{}".format(lista[0:3]))
print("{}".format(lista[:2]))
print("{}".format(lista[3:]))
print("{}".format(lista[0:-1]))
print("{}".format(33 in lista1))
print("{}".format(33 not in lista1))
print("{}".format(len(lista_unica)))
print("{}".format(min(lista1)))
print("{}".format(max(lista2)))
print("{}".format(sum(lista1)))
print("{}".format(lista + lista_unica))

print("\nAdicionar um elemento a uma lista")
clientes = ['Ana', 'Pedro']
clientes = clientes + ['Boris']
print("{}".format(clientes))

print("\nRemover um elemento a uma lista")
del clientes[1]
print("{}".format(clientes))

print("\nAlterar um elemento de uma lista")
clientes[0] = "Aretha"
print("{}".format(clientes))