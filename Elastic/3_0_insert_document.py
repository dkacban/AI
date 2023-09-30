from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")


doc = {
    "title": "invoice 1",
    "value": "2000"
}

es.index(index="dk-documents", document = doc, id=222)
