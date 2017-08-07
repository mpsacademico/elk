# Elasticsearch

É uma ferramenta open-source altamente escalável que permite anaálise e pesquisa full-text.  
Armazena, pesquisa e análisa grandes volumes de dados rapidamente e quase em tempo real.

Exemplos de casos de uso:
- armazenar o catálogo de produtos do site e prover pesquisa e sugestões autocomplete para os clientes
- analisar dados de logs ou transações para ver tendências, estatísticas, resumos ou anomalias
- plataforma de alertas de preços com interesses de clientes usando busca reversas (Percolator)
- analisar bilhões de registros com objetivos relacionados a business-intelligence

## Conceitos básicos

- Near Realtime (NRT): Elasticsearch é uma plataforma NRT. Possui uma ligeira latência (normalmente um segundo) que é o tempo que leva para um documento ser indexado até ele ser pesquisável
- Cluster: coleção de um ou mais nodes (servidores) que mantm todos os dados. É identificado por um nó, por padrão "elasticseacrh". Os nós se juntam ao cluster através do nome do cluster. Cuidado em usar mesmos nomes de cluster em ambientes diferentes.
- Node:  um único servidor que faz parte do cluster, é identificado por um nome (geralmente UUID). Pode ser configurado para se juntar a um cluster especfico, por padrão junta-se ao cluster "elasticsearch". Pode-se ter quantos clusters desejar.
- Index: coleção de documentos com características semelhantes. Identificado por um nome em minúsculas. No há limites de índices em um cluster.
- Type:  uma categoria (partição lógica) do índice, cuja semântica  totalmente do desenvolvedor. Em geral,  usado para documentos quem possuem campos em comum. Não ha limites de quantidade de tipos dentro de um índice.
- Document: unidade básica de informação que pode ser indexada. É expresso em JSON. Dentro de índice/tipo não há limites de documentos.
- Shards & Replicas: sharding - permitem escalar horizontalmente o volume de conteúdo; replication: fornece alta disponibilidade de um fragmento em caso do nó falhar
