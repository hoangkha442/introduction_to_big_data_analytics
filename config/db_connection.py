from pymongo import MongoClient

def get_database():
    client = MongoClient("mongodb+srv://chauhoangkha:123@cluster01.lzjgfli.mongodb.net")
    return client["ecommerce_analysis"]
