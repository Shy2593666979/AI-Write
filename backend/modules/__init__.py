from modules.base import mongodb_operate
from crud.base import mongoDB


myMongoDB = mongoDB()

baseMongoDB = mongodb_operate(myMongoDB)
