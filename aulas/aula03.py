# -*- coding: utf-8 -*-

# Dicionários
# variável que tiver com chaves -> {} -> é um dicionário
# lista = [] usa-se []
# tupla = () usa-se ()
# dicionario = {} usa-se {}
endereco = {'logradouro': 'rua vergueiro',
            'numero': '3057',
            'bairro': 'vila mariana',
            'cidade': 'são paulo',
            'UF': 'sp',
            'cep': '04101-300'
}

endereco_2 = {'logradouro': {'user1':'rua vergueiro',
                             'user2':'rua augusta'
},
            'numero': {'user1':'3057',
                       'user2':'1050'
            },
            'bairro': {'user1':'vila mariana',
                       'user2':'cerqueira cesar'
            },
            'cidade': {'user1':'são paulo',
                       'user2':'são paulo'
            },
            'UF': {'user1':'sp',
                   'user2':'sp'
            },
            'cep': {'user1':'04101-300',
                    'user2':'01212-030'}
}

# print(endereco.keys()) # retorna as chaves do dicionario
# print(endereco.values()) # retorna os valores do dicionario
# print(endereco.items()) # retorna os itens do dicionario

# for chave,valor in endereco.items():
#     print(chave,':',valor)

# print(endereco_2.keys())
# print(endereco_2.values())
# endereco_2.__setitem__('numero', {'user1','3057','user2','1030'}) # atualizando um valor dentro de um dicionário

# print(endereco_2['numero']['user1'])

# var_dict = dict(nome='paulo', sobrenome='nunes')
# print(var_dict)


# Concatenar e inserir dados
municipios_br = '5.570'
estados_br = '26'

brasil = 'O Brasil é uma república federativa formada pela união de {} estados federados, {} municípios e do Distrito Federal.'.format(estados_br,municipios_br)
brasil2 = f'O Brasil é uma república federativa formada pela união de {estados_br} estados federados, {municipios_br} municípios e do Distrito Federal.'
print(brasil)