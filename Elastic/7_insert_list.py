from elasticsearch import Elasticsearch
from cities import cities


es = Elasticsearch("http://localhost:9200")


for document_id, document in enumerate(cities):
    es.index(index="cities", document = document, id = document_id)

#TODO:
#Kibana: Analytics -> Discover -> Index management -> Find Mappings