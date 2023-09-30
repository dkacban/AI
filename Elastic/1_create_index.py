from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

es.indices.create(index="dk_documents")