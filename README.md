# ELK

Apontamentos e exemplos relacionados a plataforma Elastic Stack.

## Elasticsearch

- listar todos os índices disponíveis

`GET http://localhost:9200/_cat/indices?v`

- listar todos os nodes no cluster

`GET http://localhost:9200/_cat/nodes?v`

- criar um índice

`PUT http://localhost:9200/radar?pretty`

- inserir um documento em um índice

`PUT http://localhost:9200/radar/r2s_umb_id1/1?pretty`
```Javascript
{
	"f1": "v1"
}
```

## Exemplos

#### Logstash

- **basico.conf** - entrada stdin para a saída stdout
- **elasticsearch.conf** - entrada stdin para o Elasticsearch
- **mongodb.conf** - entrada stdin gravada no MongoDB
- **GOOG**
	- goog.conf - configuração Logstask
	- goog.csv - dados históricos (01/07/2014 a 31/12/2014) - Fonte: https://finance.yahoo.com/quote/GOOG/history?period1=1404183600&period2=1419991200&interval=1d&filter=history&frequency=1d
- **SubDates**
	- subdates.conf - configuração Logstash
	- subdates.csv - dados gerados pelo programa `subdates.py`

## Referências

CHHAJED, Saurabh. **Learning ELK Stack.** Birmingham: Packt Publishing Ltd, 2015. 206 p.
