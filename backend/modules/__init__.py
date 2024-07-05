from backend.modules.base import mongodb_operate
from backend.crud.base import mongoDB


myMongoDB = mongoDB()

baseMongoDB = mongodb_operate(myMongoDB)
