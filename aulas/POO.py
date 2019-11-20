# -*- coding: utf-8 -*-

# 1º Exemplo:
# class Servidor:
#     memoria = None
#     disco = None
#     cpu = None
#
# dns = Servidor()
# dns.memoria = 2048
# dns.disco = 50
# dns.cpu = 2
#
# print(f'O servidor tem as seguintes configurações: \
#     \nCPU: {dns.cpu}, \
#     \nMemória: {dns.memoria}, \
#     \nDisco: {dns.disco}')

# 2º Exemplo:
# class PrimeiraClasse:
#     def __init__(self):
#         print('Acessando o método construtor.')
#
#     def metodo(self):
#         print('Acessando o método')
#
# classe = PrimeiraClasse()
# classe.metodo()

# 3º Exemplo:
# class Passaro():
#     def __init__(self):
#         self.asa = 2
#         self.bico = 1
#         self.penas = True
#         self.pernas = 2
#         self.rabo = 1
#
#     def voar(self):
#         self.t = 0
#         if self.asa != 2:
#             print('Pássaro deficiente, não pode voar!')
#         else:
#             self.t = 1            
#             print('Voando...')
#
#     def pousar(self):
#         if self.t == 0:
#             pass
#         else:
#             print('Pousando...')
#
#     def dormir(self):
#         print('Dormindo...')
#
#     def acordar(self):
#         print('Acordando...')
#
# sabia = Passaro()
# sabia.patas = 1
# sabia.asa = 3
#
# sabia.acordar()
# sabia.voar()
# sabia.pousar()
# sabia.dormir()