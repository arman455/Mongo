import pymongo

my_client = pymongo.MongoClient("mongodb://localhost:27017")
my_db = my_client["Logika"] #database - база данных
my_collection = my_db["Test"] #collection - коллекция

drinks = {
    "name": "Fanta",
    "litrs": 2,
}

my_collection.insert_one(drinks) #вставить одну запись

find = my_collection.find_one({"age":15}) #найти одну запись, где ключ litrs = 2
print(find["name"])

#for objects in my_collection.find(): #поиск всех записей в коллекции
    #print(objects)
    
#my_collection.delete_one({"name":"Fanta"}) #удалить одну запись в коллекции

my_collection.delete_many({"name":'Fanta'}) #удалить все записи с соответствующим ключом-
