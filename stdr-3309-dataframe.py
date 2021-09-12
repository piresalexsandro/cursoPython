# DataFrame
# Em Pandas, um DataFrame pode ser definido como uma estrutura de dados
# bidimensional com colunas de diferentes tipos. Em outras palavras, um
# DataFrame nada mais é do que uma representação de uma tabela, mas na
# linguagem Python.
# Você pode criar um DataFrame do zero usando dicionários e listas,
# ou, como acontece na maioria das vezes, criar um DataFrame carregando
# um arquivo de dados em .csv ou excel, por exemplo.

import pandas as pd

cliente = ['Boris','Gamora','Thanos']
idade = [44, 28, 123]
cidade = ['Bosnia','New York','Munich']

df_from_series=pd.DataFrame(cliente,idade, cidade)

df_from_series.show()
