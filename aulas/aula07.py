# POO (Herança e Polimorfismo)

# Exemplo 01:
# class Pai():
#     '''Classe Pai'''
#     def __init__(self):
#         self.sobrenome = 'Pereira'
#
#     def get_sobrenome(self):
#         print(self.sobrenome)
#
# class Filho(Pai):
#     '''Classe Filho'''
#     def __init__(self):
#         super().__init__() # Permite pegar atributos que estão dentro da classe pai, dentro do __init__
#
# joao = Pai()
# joaquim = Filho()

# class Animal():
#     def __init__(self, raca, idade):
#         self.raca = raca
#         self.idade = idade
#         self.olhos = True
#         self.orgaos = True
    
#     def Nascer(self):
#         print('Nasceu...')

#     def AlimentarSe(self):
#         print('Se alimentando...')

#     def Morrer(self):
#         print('Morreu...')

#     def get_raca(self):
#         print(self.raca)

#     def get_idade(self):
#         print(self.idade)

# class Mamifero(Animal):
#     def __init__(self, raca, idade): # Definindo os parâmetros que a class pai precisa
#         super().__init__(raca, idade) # Definindo os parâmetros que a class pai precisa
#         self.pele = True
#         self.mamilos = True

# class Humano(Mamifero):
#     def __init__(self, nome, idade, pensa=True):
#         super().__init__()
#         self.nome = nome
#         self.idade = idade
#         self.pensa = pensa
#         self.bracos = 2
#         self.pernas = 2
#         self.cabeca = 1
#         self.tronco = 1
#
    # def Pensar(self):
    #     print('Pensando...')
#
# joao = Humano('João', 26)
# joao.Nascer()
# joao.AlimentarSe()
# joao.Morrer()
# print(f'Braços: {joao.bracos}')
# # joao.Pensar()
# print(joao.nome)
# print(joao.idade)
# print(joao.pensa)

# cachorro = Mamifero('Pastor', 7)
# cachorro.get_raca()
# cachorro.get_idade()

# Polimorfismo
class Pai():
    def trabalhar(self):
        print('Trabalhando de Engenheiro...')

class Filho(Pai):
    def trabalhar(self):
        print('Trabalhando de Programador...')

