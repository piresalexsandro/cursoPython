reais = float(input("Quanto dinheiro voce tem na carteira? R$"))

dollar = 5.23
euro = 6.17

print("Com {} voce pode comprar U${:.2f} dolares.".format(reais, (reais / dollar)))
print("Com {} voce pode comprar €{:.2f} euros.".format(reais, (reais / euro)))




