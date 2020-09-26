""" File to generate dummy data in mongo db.
"""
import pandas
import pymongo
import random

SKU_names = ["bottle_100ml", "bottle_50ml", "bottle_25ml"]
Status = ["Good"] * 90 + ["Bad"] * 10
unit = 0
all_data = []

pymongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
database = pymongo_client["mydatabase"]
sku_db = database["SKU_database"]


for time_stamp in pandas.date_range("11:00", "15:00", freq="3S"):
    data_dict = {}
    unit = unit + 1
    sku_name = random.choice(SKU_names)
    status = random.choice(Status)
    data_dict["SKU_id"] = sku_name
    data_dict["SKU_unit"] = unit
    data_dict["Time_stamp"] = str(time_stamp.time())
    data_dict["Status"] = status
    print(data_dict)
    all_data.append(data_dict)

print("Adding all data to database")
sku_db.insert_many(all_data)
print(sku_db)
print("DONE")
