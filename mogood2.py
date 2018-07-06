from pymongo import MongoClient

try:
    client = MongoClient()
    db = client['frutas_3']
except Exception as e:
    print("Erro:{}".format(e))




db.frt.insert({ "_id" : 1, "fruta" : "laranja", "preco" : 42, "Qtd" : 13 })
db.frt.insert({ "_id" : 2, "fruta" : "maca",    "preco" : 50, "Qtd" : 45 })
db.frt.insert({ "_id" : 3, "fruta" : "banana",  "preco" : 30, "Qtd" : 78 })
db.frt.insert({ "_id" : 4, "fruta" : "pera",    "preco" : 24, "Qtd" : 25 })
db.frt.insert({ "_id" : 5, "fruta" : "uva",     "preco" : 10, "Qtd" : 75 })


dados = db.frt.find()
dados =[x for x in dados]
print(dados)