from backend.modules.base import mongodb_operate
from backend.crud.base import mongoDB
from backend.crud.elastic import elasticSearchModel
from settings import setting

myMongoDB = mongoDB()

baseMongoDB = mongodb_operate(myMongoDB)

baseElasticSearch = elasticSearchModel(host=setting.ES_host, port=setting.ES_port)