# Função: Descrição:
# help()  Executa a ajuda do sistema
# abs()   Retorna o módulo de um valor numérico
# float() Retorna um valor numérico como decimal
# int()   Retorna um valor numérico como inteiro
# len()   Retorna o tamanho de um objeto
# list()  Retorna uma lista
# max()   Retorna o maior valor de uma coleção
# min()   Returns o menor valor de uma coleção
# print() Mostra o resultado de um comando
# round() Arredonda um valor numérico
# sorted() Ordena os itens de uma coleção
# str()   Retorna um objeto como string
# sum()   Soma os itens de uma coleção
# type()  Retorna o tipo dos dados de uma coleção

def good_morning(name):
    print('Bom dia {}'.format(name))

good_morning("Boris")  

def multiplicacao(n1: int, n2:int):
    print("resultado: {}".format(n1 * n2))

multiplicacao(3, 387)    

print('\n Funções lambda')
clientes = [
{'nome': 'Julia', 'idade': 25},
{'nome': 'Pedro', 'idade': 65},
{'nome': 'Maria', 'idade': 78}
]

def idoso(clientes):
    return clientes['idade'] > 60

clientes_idosos = filter(idoso, clientes)  
print(list(clientes_idosos))

# usando lambda
cliente_senior = filter(lambda clientes: clientes['idade']>60, clientes)
print(list(cliente_senior))