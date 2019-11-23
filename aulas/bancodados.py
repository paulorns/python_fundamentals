##################
#### POSTGRES ####
##################
# import psycopg2
#
# try:
#     con = psycopg2.connect("host=localhost dbname=projeto user=admin password=4linux")
#
#     cur = con.cursor()
#     # cur.execute("INSERT INTO scripts(nome, conteudo) VALUES ('devops', 'projeto de python')")
#     # cur.execute("UPDATE scripts set nome='devops_novo' where nome='devops'")
#     # cur.execute("DELETE FROM scripts WHERE nome='devops_novo'")
#     cur.execute("SELECT * FROM scripts")
#     # print(cur.fetchall()) # Imprime tudo
#     # print(cur.fetchone()) # Imprime apenas 1
#     con.commit()
#
#     print('Registro criado com sucesso!')
# except Exception as e:
#     print(f'Erro: {e}')
#     print('Fazendo rollback')
#     con.rollback()
# finally:
#     print('Finalizando conexao com o bando de dados')
#     cur.close()
#     con.close()

###########
## MYSQL ##
###########
# import MySQLdb
# Conexão com o bando de dados MySQL:
# try:
#     con = MySQLdb.connect(host="localhost", user="developer", passwd="4linux", db="projetos")
#     cur = con.cursor()
# #
#     # cur.execute("INSERT INTO clientes(nome,endereco) VALUES ('novo_nome', 'novo_endereco')")
#     cur.execute("SELECT * FROM clientes")
#     # print(cur.fetchall())
#     # print(cur.fetchone())
#     con.commit()
# #
#     print('Registro criado com sucesso!')
# except Exception as e:
#     print(f'Erro: {e}')
#     print('Fazendo rollback')
#     con.rollback()
# finally:
#     print('Finalizando...')
#     cur.close()
#     con.close()

#############
## MONGODB ##
#############
# from pymongo import MongoClient
# #
# client = MongoClient('localhost')
# db = client['dexterops']
# #
# # db.fila.insert({"_id":1,
# #                 "servico": "Intranet2",
# #                 "status": 0})
# #
# # db.fila.remove()
# #
# def inserir_dados():
#     try:
#         db.fila.insert({"_id":200,
#                         "empresa":"4linux",
#                         "cursos": [{"nome": "Python Fundamentals",
#                                     "carga horaria": 40},
#                                     {"nome": "Linux Fundamentals",
#                                     "carga horaria": 40}
#                                     ]
#                         })
#     except Exception as e:
#         print(f'Erro: {e}')
# #
# def buscar_dados():
#     # Teste solo...
#     # try:
#     #     print(db.fila.find())
#     # except Exception as e:
#     #     print(f'Erro: {e}')
# #
#     #Código passado em aula
#     for r in db.fila.find():
#         print(f'\nEmpresa: {r["empresa"]}')
#         for c in r["cursos"]:
#             print(f'Nome: {c["nome"]}, Carga Horária: {c["carga horaria"]}')
#         print('================')

# # inserir_dados()
# buscar_dados()