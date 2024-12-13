## Needs to run an elastic-search container in local 

### Command
```
docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.10.1
```

### Install scrapy using command

```
pip install scrapy, Elasticsearch
```

### command to run Python file to scrape data
```
scrapy runspider .\spider.py
```
