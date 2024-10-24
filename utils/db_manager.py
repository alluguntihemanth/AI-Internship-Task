from pymongo import MongoClient
from datetime import datetime  

client = MongoClient("mongodb://localhost:27017/")
db = client["pdf_database"]
collection = db["documents"]

def save_to_mongo(file_path, summary, keywords):
    data = {
        "file_path": file_path,
        "summary": summary,
        "keywords": keywords,
        "timestamp": datetime.now()  
    }
    collection.insert_one(data)
