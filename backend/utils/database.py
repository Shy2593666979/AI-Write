from mongoengine import connect

def get_mongo_db():
    connect("py_database", host="mongodb://localhost:27017/")