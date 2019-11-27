# def oi(nome='Pedro'):
#     return 'Oi ' + nome
#
#     def ola():
#         return 'aqui você está na função ola()'
#   
#     def boasvindas():
#         return 'aqui você está na função boasvindas()'
#
# # print(oi())
# # ola = oi()
# # print(ola)
# print(ola())

# Condeido de decoradores
def inc(x):
    return x + 1

def dec(x):
    return x - 1

def soma_2(x):
    return x + 2

def operacao(func, x):
    resultado = func(x)
    return resultado

funcao = input('Digite a função: ')
num = input('Digite o número: ')

print(operacao(funcao, int(num)))