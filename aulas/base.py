#!../venv/bin/python3

import pandas as pd
df = pd.read_csv('../arquivos/salarios.csv', encoding='UTF-8')
# encoding='UTF=8' -> Mostra qual encoding deve ser tratado o arquivo
# header=0 -> Informo qual linha ele vai usar como cabeçalho
# usecols['Name', 'Empoyee Annual Salary'] -> Especifico quais coluna eu quero que mostre
# nrows=30 -> Especifico quantas linhas eu quero que mostre

# print(dt.head()) # Mostra as 5 primeiras linhas + o cabeçalho
# print(dt.iloc[:2]) # Mostra as [inicio : fim], conforme o parâmetro [de : até]
# print(dt.loc[index, index]) # Traz as linhas dos index que você indicar entre os colchetes []
# print(df['Departament'], df['Name']) # Especifico a ordem e quais colunas mostrar

# var = df['Name'] # Definindo a coluna "Name"
# var.to_csv('name.csv', header=0, sep=";") # Criando um novo arquivo .csv, usando o separador ";"

# sr = pd.Series([2, 7, 5, 4, 3, 8])
# print(sr)

# parâmetros loc: número da linha, nome(s) da(s) coluna(s)
# var2 = df.loc[20, ['Name', 'Department']]
# var2.to_csv('valor_unico.csv', header=0, sep=";")
#
# parâmetros iloc: número da linha, index da coluna
# print(df.iloc[20, 2])

# var = df['Name'] + ' ' + df['Employee Annual Salary'] + ' ' + df['Department']
# var.to_csv('name_salario.csv', header=0)