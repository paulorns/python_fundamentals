# -*- coding: utf-8 -*-

#!/usr/bin/python3

# Faça um programa que imprima o nome do seu time|
# time = input("Qual o nome do seu time: ")
# print(time)

# Faça um programa que peça um número e imprima esse número
# v1 = input("Digite um número: ")
# print(v1)
# ou
# print(input("Digite um número: "))

# Faça um programa que receba 'F' ou 'M' e mostre Feminino ou Masculino
# capitalize -> Ele deixa a string em caixa alta
# sexo = str(input('Informe qual o seu sexo: '))
# sexo = sexo.capitalize()
# if sexo == 'F':
#     print('Seu sexo é Feminino')
# elif sexo == 'M':
#     print('Seu sexo é Masculino')
# else:
#     print('Informação inválida')

# Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo
# numero = float(input('Digite um número: '))
# if numero > 0:
#     print('O número é positivo')
# elif numero < 0:
#     print('O número é negativo')
# else:
#     print('O número informado é 0')

# Exemplo de tratativa de erro com o exercicio anterior
# numero = int(input('Digite um número: '))
# --- Fazer

# Dada a lista abaixo, faça:
# print 3, 13, Vasco
# print 5, sp, 14
# mude o valor: 4 -> 30
# mude o valor: 10 -> 100
# mude o valor: 14 -> 150
# mude o valor: Vasco -> Bragantino
# lista: ['Corinthians', [1, 2, 3, 4, 5], 'Palmeiras', 'São Paulo', [10, 11, 12, 13, 14], 'Flamengo', 'Vasco']
# lista = ['Corinthians', [1, 2, 3, 4, 5], 'Palmeiras', 'São Paulo', [10, 11, 12, 13, 14], 'Flamengo', 'Vasco']
# print(lista[1][2], lista[4][3], lista[6])
# print('---')
# print(lista[1][4], lista[3], lista[4][4])
# print('---')
# lista[1][3] = 30
# print(lista[1])
# print('--')
# lista[4][0] = 100
# print(lista[4])
# print('--')
# lista[4][4] = 150
# print(lista[4])
# print('--')
# lista[6] = 'Bragantino'
# print(lista)

# Dicionários
# dados = {
#     'cidades': {
#         'saopaulo': {
#             'nome': 'São Paulo',
#             'municipios': 645,
#             'populacao': 12.18
#         },
#         'riodejaneiro': {
#             'nome': 'Rio de Janeiro',
#             'municipios': 92,
#             'populacao': 6.32
#         },
#         'minasgerais': {
#             'nome': 'Minas Gerais',
#             'municipios': 31,
#             'populacao': 20.87
#         }
#     }
# }
# # Print a quantidade de municípios de minas
# # Print a quantidade de municípios do rio
# # Print a população de minas em milhões
# # Print a população de são paulo em milhões
# # Print o nome de são paulo
# # -- Reposta --
# print(dados['cidades']['minasgerais']['municipios'])
# print(dados['cidades']['riodejaneiro']['municipios'])
# print(dados['cidades']['minasgerais']['populacao'] * 1000000)
# print(dados['cidades']['saopaulo']['populacao'] * 1000000)
# print(dados['cidades']['saopaulo']['nome'])

# Conversão de tipos
# dado a variável var, peça que o usuário digite um número e multipliquepor var
# var = 15
# num = print(int(input('Digite um número: ')) * var)
# print(num)