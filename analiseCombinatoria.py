# Assim, para calcular uma combinação simples de n elementos tomados p a p (p ≤ n), utiliza-se a seguinte expressão:
from math import factorial

def getFactorial(num):
    return factorial(num)

def getCombinations(elem, poss): #Cn,p = n! / (p!*(n - p)!)
    return getFactorial(elem) / (getFactorial(poss) * getFactorial(elem - poss))




