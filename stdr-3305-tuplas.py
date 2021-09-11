
#criando tuplas
t1 = ()
t2 = (1,2,3,4)

#Cria uma tupla a partir de uma lista
lista = ['joao', 'maria','boris','joana']
t3 = (lista)
print(t3)

#Cria uma tupla a partir de uma string
t4 = tuple('Marrocos')
print('\n')
print(t4[1:4])
print(t4[:5])
print(t4[3:])
print(t4[0:-1])

#Operadores in e not in
print('\nOperadores in e not in')
print('o' in t4)
print('s' not in t4)

#Funcoes com tupla
t = (7, 33, 1)
print('\nFuncoes com tupla')
print(min(t))
print(max(t))
print(sum(t))
print(len(t))