# -*- coding: utf-8 -*-

#!/usr/bin/python3

# Manipulando arquivos

# arq1 = open('../arquivos/sherlock.txt', 'r') # Abrindo o arquivo
# print(arq1.read()) # Printando na tela o conteúdo do arquivo
# print(arq1.tell()) # Mostra a qtde de caracteres do arquivo e só funciona quando lê o arquivo
# print(arq1.seek(0,0)) # Ele mostra a posição
# print(arq1.read(50)) # Imprime os 50 primeiros caracteres do arquivo
# arq1.close() # Fechando o arquivo

# with open('arquivo01.txt', 'x') as f:
#     f.write('Abrindo arquivos em python')

# arq1 = '../arquivos/sherlock.txt'
# with open(arq1, 'r+') as f:
#     print(f.readlines())

# Funções
# def soma(x, y):
#     print(x + y)
# soma(10, 10)

# outro exemplo de função
# produtos = []
# def cadastraProduto(produto):
#     produtos.append(produto)
#     global prod
#     prod = "Chá"
#
# def listarProduto():
#     for p in produtos:
#         print(p)
#
# produto = ''
#
# while produto != 'sair':
#     produto = input('Digite o produto que deseja cadastrar: ')
#     cadastraProduto(produto)
#     print('Produtos cadastrados: ')
#     listarProduto
#
# print(prod)

# Outro exemplo de funções
# def primo(num):
#     for n in range(2, num):
#         if num % n == 0:
#             print('O número não é primo!')
#             print(n)
#             break
#         else:
#             print('É número primo!')
#             print(n)
#             break
#
# var1 = int(input('Digite um número: '))
# primo(var1)

# Args e Kwargs
# O "Args" transforma o valores que a função receber, como parâmetro, em tuplas
# def printa(*valores):
#     print(valores)
#     print(valores[0])
#     print(valores[1])
#     print(valores[-1])
# printa('teste', 'pagamento', 'dinheiro','banco','carro')
#
# O "Kwargs" transforma o valores que a função receber, como parâmetro, em um dicionário
# mas os valores informados para a função, tem que ser no estilo do dicionário
# def printa2(**valores):
#     print(valores)
# printa2(var1='valor', var2='valor2', var3='valor3')

# Exercício de função
# nome = 'Joao'
# print(nome)
# Criar uma função que muda o valor de nome e print na tela
# def mudaNome(novo_nome):
#     nome = novo_nome
#     return nome
# print(mudaNome('Ana'))

# Outro exemplo de funções:
# texto = 'Eu sou um cérebro, Watson. O resto é mero apêndice.'
# def split_texto(texto):
#     return texto.split(' ')
# def lower_texto(texto):
#     return texto.lower()
# arquivo_split = split_texto(texto)
# arquivo_lower = lower_texto(texto)
# print(arquivo_split)
# print(arquivo_lower)
# print(arquivo_novo)
# print(type(arquivo_novo))
