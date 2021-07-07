# Assim, para calcular uma combinação simples de n elementos tomados p a p (p ≤ n), utiliza-se a seguinte expressão:
from math import factorial

e = int(input("Digite o numero de elementos: "))
p = int(input("Digite o numero de combinacoes entre si: "))

def getFactorial(num):
    return factorial(num)

def getCombinations(elem, poss): #Cn,p = n! / (p!*(n - p)!)
    return getFactorial(elem) / (getFactorial(poss) * getFactorial(elem - poss))

print("O total de combinacoes de {} elementos tomados {} a {} e de: {}".format(e, p, p, getCombinations(e, p)))




