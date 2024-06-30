from modules.base import mongodb_operate
from crud.base import mongoDB


myMongoDB = mongoDB()

styleMongoDB = mongodb_operate(myMongoDB)
