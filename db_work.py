import pymongo
import datetime

my_client = pymongo.MongoClient("mongodb://localhost:27017")
my_db = my_client["Logika_15"]
my_col = my_db["Test"]

diction1 = {
    "type": "cat",
    "name": "Barsik",
    "age": 3,
    "birth": datetime.datetime.now()
}

diction2 = {
    "name": "виталик",
    "surname": "Крабов",
    "marks": []
}

# $set - устанавливает новые данные (на место старых)
# $unset - удаляет поле из документа
# $push - пополняет список (не удаляя старый) 
# $pull - удаляет элемент списка
my_col.update_one(
    {"name": "виталик"},
    {"$set": {"marks": []}} 
)