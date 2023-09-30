from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

query = {
    "query" : {
        "match" : {
            "name":"Warszawa"
        }
    }
}

result = es.search(index="cities", query=query)
print(result)


#TODO:
#Znajdź miasta, których populacja jest większa niż 100000