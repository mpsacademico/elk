#  ELK

- Fornece uma solução completa para análise de registros (logs)
- Ajuda a verificar o comportamento do sistema:
  - issue debugging: verificar através dos logs os erros que estão ocorrendo para consertá-los
  - performance analysis: ajuda a otimizar o desempenho do sistema, observando por exemplo o tempo das respostas HTTP
  - security analysis: dá informações sobre brechas de segurança, por exemplo, com logs de ssh login
  - predictive analysis: os logs e eventos podem ajudar a identificar clientes em potencial, planos de recursos e otimização
  - internet of things and logging: verificar todo o contexto de conexão dos sistemas e otimizar e evitar falhas de uma maneira geral
- Desafios na análise de logs:
  - formato de logs não padronizado: linha, data/hora, informações
  - logs descentralizados: localizados em diferentes servidores e componentes
  - conhecimento específico requerido: necessário conhecimento e acesso aos logs

## ELK Stack

- Plataforma completa para análise de logs, sendo uma combinação de três aplicacações open source:
  - Elasticsearch: permite indexação dinâmica, encontra dados consultados muito rapidamente
  - Logstash: coleta, trata e encaminha os dados com várias facilidades de tratamento entre outros
  - Kibana: ferramenta Web (HTML e Javascrip) que usa dados indexados no Elasticsearch para exibir gráficos
    - discover (exploração interativa de dados com filtros), visualize (gráficos, métricas, mapas), dashboard (conjunto de visualizações), settings (ajustes, create scripted fields)
  
## Instalação

- Requisito: Java runtime (Java 7) `java -version`
- bin/elasticsearch `curl 'http://localhost:9200/?pretty'`
  - configurações: elasticsearch.yml e logging.yml (network address, paths, cluster name, node name)
- bin/logstash -e 'input { stdin { } } output { stdout { } }' OR bin/logstash -f arquivo.conf (configuration files are in the JSON format)
- bin/kibana acessar no navegador em http://localhost:5601
  - configurações config/kibana.yml

## Logstash plugins

- Input plugin
  - file: strems log events from a file
  - stdin: " standard input
  - syslog: messages over the network
  - elasticsearch: based on results of a search query
  - redis, ganglia, lumberjack, eventlog, s3
- Filters plugin
  - date: parse date fields
  - drop: drops everything that matches the filter condition
  - grok: parse unstructured data from logs to structured format
  - mutate: helps rename, remove, modify, replace fields in events
  - multiline, dns, geoip
- Output plugin
  - file: writes events to a file on disk
  - e-mail: sends an e-mail
  - elasticsearch: stores output to the Elasticsearch cluster
  - stdout: standard output
  - redis, mongodb, kafka

OBS: para informações mais avançadas sobre configurações verificar a documentação
