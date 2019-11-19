#!../venv/bin/python3

import pandas as pd
dt = pd.read_csv('../arquivos/salarios.csv')
# print(dt.head()) # Mostra as 5 primeiras linhas + o cabeçalho
# print(dt.iloc[:2]) # Mostra as [inicio : fim], conforme o parâmetro [de : até]
# print(dt.loc[index, index]) # Traz as linhas dos index que você indicar entre os colchetes []

sr = pd.Series([2, 7, 5, 4, 3, 8])
print(sr)