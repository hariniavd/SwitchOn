""" File to generate dummy data in mongo db.
"""
import pandas
import pymongo
import random
import constants

pymongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
# Generating 90% of good items and 10% of bad items as per the requirement.
Status = ["Good"] * 90 + ["Bad"] * 10
all_data = []


def generate_data():
    unit = 0
    database = pymongo_client["mydatabase"]
    sku_db = database["SKU_database"]

    for time_stamp in pandas.date_range("11:00", "15:00", freq="3S"):
        data_dict = {}
        unit = unit + 1
        if unit in [151, 981, 4483, 3734, 3719]:
            data_dict["Status"] = "Bad"
        else:
            status = random.choice(Status)
            data_dict["Status"] = status
        sku_name = random.choice(constants.SKU_NAMES)
        data_dict["SKU_id"] = sku_name
        data_dict["SKU_unit"] = unit
        data_dict["Time_stamp"] = str(time_stamp.time())
        print(data_dict)
        all_data.append(data_dict)

    print("Adding all data to the database")
    sku_db.insert_many(all_data)
    print("Data insertion completed..")


if __name__ == '__main__':
    if "mydatabase" not in pymongo_client.list_database_names():
        generate_data()
    else:
        print("Database already exists..!!")