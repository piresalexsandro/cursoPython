d = 'Santander'
x = 'SANTANDER'
b = 'Banco'
abc = 'abcdefghijklmnopqrstuvwxyz0123456789'
titulo = 'a bela e a fera'
# Retorna o primeiro caracter da string
print(d[0])

# concatenar
print("{} {}".format(b, d))

#  repete strings
print("{} ".format(d*3))

# substring
print("{}".format(abc[1:6]))
print("{}".format(abc[:9]))
print("{}".format(abc[20:]))
print("{}".format(abc[0:-2]))

# tamanho da string
print("{}".format(len(abc)))
# O tamanho do caracter é dado pelo seu código ASCII
print("{}".format(max(abc)))
print("{}".format(min(abc)))

# Você pode usar os operadores in e not in para checar a existência de uma string em uma outra string.
print("{}".format('der' in d))
print("{}".format('der' in abc))

print("\nFunções de Strings")
print("{}".format('Santander' == d))
print("{}".format('Santander' != d))
print("{}".format('Santander' > d))
print("{}".format('Santander' < d))
print("{}".format('Santander' >= d))
print("{}".format('Santander' <= d))

print("\nConvertendo Strings")
print("{}".format(d.capitalize()))
print("{}".format(d.swapcase()))
print("{}".format(x.lower()))
print("{}".format(abc.upper()))
print("{}".format(titulo.title()))


