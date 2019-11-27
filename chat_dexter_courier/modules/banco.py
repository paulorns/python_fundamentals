from pymongo import MongoClient, DESCENDING
import time

class BancoMongo():

    def __init__(self):
        try:
            client = MongoClient('192.168.201.116') # Criando a conexão com o banco
            self.db = client['chat'] # Informando o database que irá usar
        except Exception as e:
            print(f'Erro: {e}')
            exit()

    def cadastrar(self, name, mensagem):
        date = {
            'nome': name,
            'mensagem': mensagem,
            'hora': time.strftime('%d-%m-%Y %H:%M:%S')
            }
        self.db.chat.insert(date)

    def select(self):
        ultimo = [x for x in self.db.chat.find().sort("_id", DESCENDING)] # Denominado "Compreenção em lista"
        while True:
            date = [x for x in self.db.chat.find().sort("_id", DESCENDING)]
            if date != ultimo:
                ultimo = date
                print(f'[{date[0]["hora"]}] {date[0]["nome"]} : {date[0]["mensagem"]} \n')
                time.sleep(2)

if __name__ == "__main__":
    obj = BancoMongo()
    obj.select

# etc/mongodb.conf
# Liberar no bind_ip: 0.0.0.0
# Port: 27017
# Configurar esse arquivo!!!