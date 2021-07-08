import analiseCombinatoria as ac

e = int(input("Digite o numero de elementos: "))
p = int(input("Digite o numero de combinacoes entre si: "))

resultado = ac.getCombinations(e, p)

print("O total de combinacoes de {} elementos tomados {} a {} e de: {}".format(e, p, p, resultado))

