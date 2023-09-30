from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

citiesMapping = {
    "name" : {
        "type" : "text"
    },
    "population" : {
        "type" : "integer"
    },
    "president" : {
        "type" : "text"
    },
       "voivodship" : {
        "type" : "keyword"
    }
}

es.indices.create(index="cities", mappings =
{
'properties': citiesMapping                      
})

#TODO:
#Kibana: Management -> Stack Management -> Index management -> Find Mappings