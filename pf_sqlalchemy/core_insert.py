from core import user_table, engine

con = engine.connect()
ins = user_table.insert()

# insert pessoa
new = ins.values(idade=24, nome='teste', senha='testando')
con.execute(new)

# insert pessoas
con.execute(user_table.insert(),[
    {'nome': 'Marcio', 'idade': 20, 'senha': 'semsenha'},
    {'nome': 'Gustavo', 'idade': 18, 'senha': 'abacaxi123'},
    {'nome': 'Guilherme', 'idade': 22, 'senha': 'goiaba123'}
])