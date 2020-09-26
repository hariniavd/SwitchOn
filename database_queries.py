""" Module which connects to mongodb and queries from the database.
"""
from pymongo import MongoClient
mongo_client = MongoClient('mongodb://localhost:27017')
my_database = mongo_client["mydatabase"]
sku_database = my_database["SKU_database"]


def get_all_skus():
    """ Returns all the SKU's names which are available in the database.
    """
    sku_ids = set()
    for i in sku_database.find({}, {"_id": 0, "SKU_id": 1}):
        sku_ids.add(i["SKU_id"])

    return list(sku_ids)


def get_sku_id(sku_id, status, start_time, end_time):
    """ For given sku_id, status and time span, it queries and returns back the data.

        Args:
            sku_id (str): Name of the SKU
            status (str): Status of the SKU, i-e Good or Bad
            start_time (str): Start time for comparing
            end_time (str): End time for comparing
    """
    all_data = []
    for i in sku_database.find({"SKU_id": sku_id, "Status": status}, {"_id": 0}):
        if start_time < i["Time_stamp"] < end_time:
            all_data.append(i)

    return all_data


def get_status_of_id(sku_id):
    """ Get the status of the given id

        Args:
            sku_id (int): SKU unique number
    """
    status_query = list(sku_database.find({"SKU_unit": int(sku_id)}, {'_id': 0, 'Status': 1}))
    status = status_query[0]["Status"]
    return status


def get_status_skus(sku_list, status):
    """ From a given list of SKU id's and status as mentioned, it checks whether the criteria is matching
        and returns the matching values.

        Args:
            sku_list (list): List of all the random sku unit numbers
            status (str): Status of the SKU, i-e Good or Bad
    """
    values = []
    for sku_id in sku_list:
        status_query = list(sku_database.find({"SKU_unit": int(sku_id), "Status": status}, {'_id': 0, 'Status': 1}))
        if status_query:
            values.append(sku_id)
    return values
