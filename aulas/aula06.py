# -*- coding: utf-8 -*-

#!/usr/bin/python3

# Funções
# def mostra(par1=None): # Tirando a obrigatoriedade de passar um parâmetro para a função
#     # Pois já está definindo um como padrão, caso não passe nada
#     print(f'Teste {par1}')
# mostra('Casa')

# Funções: args e kwargs
# lista = []
# def adiciona(valor):
#     global lista
#     return lista.append(valor)
#
# def remove(valor):
#     global lista
#     return lista.remove(valor)
#
# adiciona('Batata')
# remove('Batata')
#
# print(lista)

# Funções anônimas (lambda)
# Exemplo 1 - lambda
# def subtrair(x, y):
#     '''Subtrai valores'''
#     return x - y
#
# sub = lambda x, y: x - y

# Exemplo 2 - lambda
# carrinho = [{"nome": "Tenis", "valor":21.70},
#             {"nome": "Camiseta", "valor":10.33}]
#
# black_friday = lambda x: x / 2
#
# for c in carrinho:
#     print(f'\nNome do produto: {c["nome"]}')
#     print(f'Valor original: {c["valor"]}')
#     print(f'Valor com desconto: {black_friday(c["valor"])}\n')
#     print('=-'* 11)

# Exemplo 3 - lambda
# anonimas = [lambda x: x** 2,
#             lambda x: x** 3,
#             lambda x: x** 4]
#
# for c in anonimas:
#     print(c(10))


# Orientações a objeto