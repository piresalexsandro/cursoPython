num = int(input("Digite um numero para ver a sua tabuada: "))

print("-"*15)

for i in range(11):
    if i > 0:
        print("{} x {:2} = {}".format(num, i, num * i))
print("-"*15)



