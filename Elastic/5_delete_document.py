from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

es.delete(index="dk-documents", id="123")
