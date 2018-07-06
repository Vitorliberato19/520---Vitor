from pymongo import MongoClient
from random import choice as sorteio

ids = list(range(999))

try:
    client = MongoClient()
    db = client['frutas_3']
except Exception as e:
    print("Erro:{}".format(e))


frutas_ = [
    {"fruta" : "laranja", "preco" : 42, "Qtd" : 13 },
    {"fruta" : "maca",    "preco" : 50, "Qtd" : 45 },
    {"fruta" : "banana",  "preco" : 30, "Qtd" : 78 },
    {"fruta" : "pera",    "preco" : 24, "Qtd" : 25 },
    {"fruta" : "uva",     "preco" : 10, "Qtd" : 75 },
]

# db.frt.insert({ "fruta" : "laranja", "preco" : 42, "Qtd" : 13 })

db.frt.remove()
for fruta in frutas_:
    a = sorteio(ids)
    ids.remove(a)
    fruta["_id"] = a
    db.frt.insert(fruta)




    # teste

dados = db.frt.find()
dados =[x for x in dados]
print(dados)