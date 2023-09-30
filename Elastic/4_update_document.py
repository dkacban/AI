from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")


doc = {
    "title": "invoice 1",
    "value": "3000"
}

es.update(index="dk-documents", id=222, doc=doc)
