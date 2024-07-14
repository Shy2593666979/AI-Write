from elasticsearch import Elasticsearch

class elasticSearchModel:
    def __init__(self, **kwargs):
        host = kwargs.get('host')
        port = kwargs.get('port')
        self.es = Elasticsearch([{"host": host, "port": port}])
    
    def create_index(self, indexName, body):
        resultES = self.es.index(index=indexName, body=body)
        if resultES.get('result') != "created":
            return {
                "Mark": False,
                "result": "create index fail"
            }
        return {
            'Mark': True,
            "result": resultES
        }
        
    def create_index_with_id(self, indexName, id, body):
        resultES = self.es.index(index=indexName, id=id, body=body)
        if resultES.get('result') != "created":
            return {
                "Mark": False,
                "result": "create index fail"
            }
        return {
            'Mark': True,
            "result": resultES
        }
    def delete_index(self, indexName):
        resultES = self.es.indices.delete(index=indexName)
        if resultES.get('acknowledged') != True:
            return {
                "Mark": False,
                "result": "delete index fail"
            }
        return {
            'Mark': True,
            "result": resultES
        }
    
    def update_index_with_id(self, indexName, id, body):
        resultES = self.es.index(index=indexName, id=id, body=body)
        if resultES.get('result') != "updated":
            return {
                "Mark": False,
                "result": "updated index fail"
            }
        return {
            'Mark': True,
            "result": resultES
        }
    
    def search_index_all(self, indexName):
        resultES = self.es.search(index=indexName)
        if resultES['time_out']:
            return {
                'Mark': False,
                'result': "get time out"
            }
        result = []
        for idx in resultES['hits']['hits']:
            result.append(idx)
        return {
            'Mark': True,
            'result': result
        }
        
        