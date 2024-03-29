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

# Faça um programa para a leitura de duas notas parciais de um aluno.
# Média: 7
# O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem de "Aprovado", se a média alcançada for maior ou igual a 7;
# A mensagem de "Reprovado", se a média for menor do que 7;
# A mensagem de "Aprovado com Distinção", se a média for igual a 10.
# -- Resposta --
# nome_aluno = input('Digite o nome do aluno: ')
# nota1 = float(input('Informe a primeira nota: '))
# nota2 = float(input('Informe a segunda nota: '))
# resultado = (nota1 + nota2) / 2
# print(f'A nota do aluno {nome_aluno} é {resultado}')
# if resultado == 10.0:
#     print('Aprovado com Distinção')
# elif resultado >= 7.0:
#     print('Aprovado')
# else:
#     print('Reprovado')

# Try e except
# 1 - Faça uma lista com 10 nomes de usuários
# 2 - peça para o usuário digitar o nome de usuario
# 3 - caso não existaesse usuario na lista
# 4 - dê um NameError e volte para a parte 2
# lista_acesso = ['paulo', 'renato', 'camila', 'jorge', 'julio']
# while True:
#     try:
#         login = input('Digite o seu login: ')
#         for valida in lista_acesso:
#             if login.lower() != valida:
#                 raise NameError('Login não encontrado!')
#             else:
#                 print(f'Seja bem vindo {login}, acesso permitido!')
#                 break
#         break
#     except NameError as l:
#         print(l)
#         continue
#
# Alterativa para o exercicio acima
# lista_acesso = ['paulo', 'renato', 'camila', 'jorge', 'julio']
# while True:
#     try:
#         login = input('Digite o seu login: ')
#         if login.lower() not in lista_acesso:
#             raise NameError('Login não encontrado!')
#         else:
#                 print(f'Seja bem vindo {login}, acesso permitido!')
#                 break
#         break
#     except NameError as l:
#         print(l)
#         continue

#Funções
# criar uma função que pega o conteúdo da variável texto e deixa em caixa alta
# texto = 'Eu sou um cérebro, Watson. O resto é mero apêndice.'
# def upper_texto(texto):
#     return texto.upper()
# arquivo_upper = upper_texto(texto)
# print(arquivo_upper)

# Crie uma função que peça 2 números e retorne o maior
# se o valor for igual print "Valores iguais"
# guarde em variável e print
# def valida(var1, var2):
#     if var1 == var2:
#         return 'Valores iguais'
#     elif var1 > var2:
#         return var1
#     else:
#         return var2
#     # outra forma de fazer validação:
#     # else:
#     # return max(var1, var2)
#
# num1 = float(input('Digite o primeiro número: '))
# num2 = float(input('Digite o segundo número: '))
#
# resultado = valida(num1, num2)
# print(resultado)

# crie uma função que receba um número indefinido de valores númericos
# com *args e retorne os valores ordenados de forma descrecente.
# def ordenados(*valores):
#     return sorted(valores, reverse=True)

# POO: Herança
# Crie uma classe que represente um automóvel
# Com atributos:
# - Ano de fabricação;
# - Marca;
# - Preço;
# Métodos:
# - get_ano;
# - get_marca;
# - get_preco;
#
# class Automovel():
#     '''Classe que representa um automóvel'''
#     def __init__(self, ano, marca, preco): # Atributos necessários, devem ser passados aqui!
#         self.ano = ano
#         self.marca = marca
#         self.preco = preco
# #    
#     def get_ano(self):
#         print(f'Ano de fabricação: {self.ano}')
# #
#     def get_marca(self):
#         print(f'Marca: {self.marca}')
# #
#     def get_preco(self):
#         print(f'Preço: {self.preco}')
# #
# # carro1 = Automovel(2019, 'Ford', 25000.00)
# # carro1.get_ano()
# # carro1.get_marca()
# # carro1.get_preco()

# # Segunda parte do desafio.
# # Crie uma classe Moto que terá o atributo:
# # - Tipo e herdará os atributos/métodos da classe automóvel;
# # Obs.: 
# # - Lembresse que a moto só pode ligar se estiver desligada e desligar se ela estiver ligada
# # - Acelerar e Frear só se estiver ligada
# # Os métodos:
# # - Ligar()
# # - Desligar()
# # - Acelerar()
# # - Frear()
# #
# ligada = False
# #
# class Moto(Automovel):
#     def __init__(self, ano, marca, preco, tipo = 'Moto', ligada=True):
#         super().__init__(ano, marca, preco)
#         self.tipo = tipo
#         self.ligada = ligada
# #
#     def ligar(self):
#         global ligada
#         if ligada == False:
#             print('Ligando...')
#             ligada = True
#         else:
#             print('Moto está Ligada!')
# #
#     def desligar(self):
#         global ligada
#         if ligada == True:
#             print('Desligando...')
#             ligada = False
#         else:
#             print('Moto está desligada!')
# #
#     def acelerar(self):
#         global ligada
#         if ligada == True:
#             print('Acelerando...')
#         else:
#             print('Moto está desligada')
# #
#     def frear(self):
#         global ligada
#         if ligada == True:
#             print('Freando...')
#         else:
#             print('Moto está desligada')
# #
# moto1 = Moto(2012, 'BMW', 12000)
# moto1.desligar()
# moto1.ligar()
# moto1.acelerar()
# moto1.frear()
# moto1.get_ano()
# moto1.get_marca()
# moto1.get_preco()
#
# Criar o mesmo exercício acima, utilizando o try para tratar os erros das condições
# e o raise para criar os erros de quando as condições não forem atendidas.