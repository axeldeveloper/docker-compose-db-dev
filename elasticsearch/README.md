# Projetct
    
    - Elasticsearch
    
    
# Build   
``` powershell  
    $ docker-compose -f docker-compose.yml build
    $ docker-compose -f docker-compose.yml up -d
```




# Create a docker-compose.yml file:
    
    docker-compose up
    
    docker pull docker.elastic.co/elasticsearch/elasticsearch:6.3.2

    docker run -e ELASTIC_PASSWORD=766312 docker.elastic.co/elasticsearch/elasticsearch:6.3.2

    docker run -e ELASTIC_PASSWORD=766312 docker.elastic.co/elasticsearch/elasticsearch-platinum:6.2.4

    docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:6.8.13

# Test

    curl -X GET "localhost:9200/_cat/nodes?v&pretty"


# Links uteis

link 1 [here](https://www.elastic.co/guide/en/elasticsearch/reference/7.5/docker.html)

