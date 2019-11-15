# -*- coding: utf-8 -*-

#!/usr/bin/python3

# While - Exemplo
# x = 0
# while x < 10:
#     x += 1
#     print(x)

# While - Segundo exemplo
# x = 1
# while x <= 10:
#     print(f'número: {x}')
#     x += 1
# print('\nO while acabou!')

# While - adicionando valores em uma lista
# x = 1
# lista = []
# while x < 1000:
#     lista.append(x)
#     x += 1
# print(lista)

# For - Exemplo
# fruta = ['Laranja', 'Melancia', 'Uva']
# for f in fruta:
#     print(f)

# For - Segundo exemplo
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for var in l:
#     print(var)

# For - Enumerando os itens da lista e mostrando os seus valores
# l = ['Abacaxi', 'Banana', 'Pera', 'Maça', 'Ameixa']
# for num,fruta in enumerate(l):
#     print(f'{num} - Fruta: {fruta}')

# For - Utilizando o range para determinar o for
# for i in range(0,10,+1):
#     print(i)

# Break - Exemplo com while
# cont = 0
# while cont < 10:
#     print(f'Vezes de execução {cont + 1}')
#     if cont == 2:
#         print('bloco de condição que interrompe o loop')
#         break
#     cont += 1

# Contine - Exemplo com while
# t = 0
# while t < 10:
#     print(t)
#     t += 1
#     if t == 5:
#         print('Continue')
#     continue

# Erros e exceções
# try:
#     if 'mariana' == nome:
#         print('nome correto')
#     else:
#         print('nome incorreto')
# except Exception as e:
#     print(e)
#
# try:
#     x = int(input('Digite o primeiro numero: '))
#     y = int(input('Digite o segundo numero: '))
#     print(x + y)
# except ValueError as v:
#     print('esse é um erro', v)
#
# while True:
#     try:
#         idade = int(input('Digite sua idade: '))
#         if idade < 16:
#             print('Você não pode comprar bebida alcoolica e nem tirar titulo de eleitor.')
#             break
#         else:
#             if idade >= 16 and idade < 18:
#                 print('Você pode ter um titulo de eleitor.')
#                 break
#             else:
#                 print('Você pode comprar bebida alcoolica e ter um titulo de eleitor.')
#                 break
#             break # discutivel o uso desse break...
#     except Exception as e:
#         print('Isso não é um número\n', e)
#         continue

# Raise Exception
while True:
    try:
        login = input('Digite o login: ')
        if login.lower() == 'bryan':
            raise NameError('Bryan está banido!')
        else:
            print(f'Bem vindo {login}, acesso permitido!')
            break
    except NameError as e:
        print(e)
        continue