import pymongo

my_client = pymongo.MongoClient("mongodb://localhost:27017")
my_db = my_client["Logika"]
my_collection = my_db["Test"]

name = input("Введите свое имя:")
surname = input("Введите свою фамилию:")
age = input("Введите свой возраст:")

try:
    age_str = int(age)
except ValueError:
    print("Введите цифры")

me = {
    "name": name,
    "surname": surname,
    "age": age
}

my_collection.insert_one(me)
