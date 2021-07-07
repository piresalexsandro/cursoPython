# p(A): probabilidade da ocorrência de um evento A
# n(A): número de casos que nos interessam (evento A)
# n(Ω): número total de casos possíveis o espaco amostral
# P(A) = n(A) / n(Ω)

numero_casos = int(input("Entre com o numero de casos: "))
espaco_amostral = int(input("Entre com o espaco amostral: "))
probabilidade = numero_casos / espaco_amostral * 100
print("A probabilidade da ocorrência do evento e de: {}%".format(probabilidade))
