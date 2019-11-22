# import aula07 as a7
#
# joao = a7.Pai()
# joao.trabalhar()
#
# joaquim = a7.Filho()
# joaquim.trabalhar()

# # .__name__ -> Informa o nome do arquivo que você está importando
# # .__doc__ -> Traz as doc-strings do arquivo que você está importando

# import os, pwd
# os.getlogin = lambda: pwd.getpwuid(os.getuid())[0]
# print(os.getlogin()) # Me traz o usuário  que está logado na máquina
# print(os.listdir('/home/developer')) # Me traz os diretórios desse caminho
# print(os.rename('./base.py', 'pandas.py')) # Renomeia o arquivo
# os.system('ls -la') # Executa o comando no terminal ou prompt de comando

# import os, sys
# print(sys.platform) # Informa a plataforma que está roando o script
# print(sys.builtin_module_names) # Informa os módulos que estão em execução no python
# for i in range(len(sys.argv)):
#     if i == 0:
#         print(f'Function name: {sys.argv[0]}')
#     else:
#         print(f'{i}. argument: {sys.argv[1]}')

# Exemplo de len()
# lista = [1, 2, 3, 4, 5, 6, 7, 8]
# print(len(lista)) # Traz a quantidade de itens tem na lista

# import datetime
# print(datetime.datetime.now()) # Informa a data e hora atual, de acordo com seu Sistema Operacional
# print(datetime.timedelta(7)) # Mostrar a data após 7 dias
# print(datetime.time(10, 0, 0)) # Definir uma hora
# print(datetime.date(2017, 1, 1)) # Difinir uma data no padrão americano
#
# from datetime import datetime
# from datetime import seconds
# #
# acesso = datetime(2019, 10, 12, 00,00,00)
# atual = datetime.now()
# #
# if (atual - acesso).total.seconds() > 3600:
#     print('Seu token expirou.')
# else:
#     print('Acesso liberado.')
# Procurar um código que faça funcionar o exemplo acima

# import csv
# with open('../arquivos/novo_salarios.csv', 'w', newline='') as csvfile:
#     arquivo = csv.writer(csvfile, delimiter=',')
#     arquivo.writerow(['Teste'] * 5)
#     arquivo.writerow(['4Linux', 'Python'])
# CRiando um novo arquivo .csv