from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

doc = es.get(index="dk-documents", id=222)
print(doc['_source'])
