# pip3 inssstall pymongo
from pymongo import MongoClient

try:
    client = MongoClient()
    db = client['4linux']
except Exception as e:
    print("Erro:{}".format(e))
#
# db.pessoas.insert({'_id':5,'nome':'joaozinho'})


# db.pessoas.insert({ "_id" : 2, "nome" : "joao", "idade" : 42, "sobrenome" : "silva" })
# db.pessoas.insert({ "_id" : 4, "nome" : "pedro", "idade" : 50, "sobrenome" : "silva" })
# db.pessoas.insert({ "_id" : 54, "nome" : "Vitor", "idade" : 30, "sobrenome" : "silva" })
# db.pessoas.insert({ "_id" : 1, "nome" : "daniel", "idade" : 24, "sobrenome" : "silver" })
# db.pessoas.insert({ "_id" : 5, "nome" : "joaozinho" })


# db.pessoas.remove() # matar a base

# dados = db.pessoas.find_one({'_id':2}) #ler só o id = 2
dados = db.pessoas.find()
dados =[x for x in dados]
print(dados)

