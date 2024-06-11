import pymongo

my_client = pymongo.MongoClient("mongodb+srv://Logika_ivan_petrov:IbPS6hMS8sZGg50s@logikacluster.29t7q3c.mongodb.net/test")
my_db = my_client["Logika_DB"]
my_col = my_db["Tinder_col"]