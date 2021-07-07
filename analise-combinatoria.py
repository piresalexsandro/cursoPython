# Arranjos
# Nos arranjos, os agrupamentos dos elementos dependem da ordem e da natureza dos mesmos.
# Para obter o arranjo simples de n elementos tomados, p a p (p ≤ n), utiliza-se a seguinte expressão:
# A com n vírgula p subscrito fim do subscrito igual a numerador n fatorial sobre denominador parêntese
# esquerdo n menos p parêntese direito fatorial fim da fração

from math import factorial

e = int(input("Digite o numero de elementos: "))
p = int(input("Digite o numero de combinacoes entre si: "))

def getFactorial(num):
    return factorial(num)

def getCombinations(elem, poss):
    return getFactorial(elem) / getFactorial(elem - poss)

print("O total de combinacoes de {} elementos tomados {} a {} e de: {}".format(e, p, p, getCombinations(e, p)))




