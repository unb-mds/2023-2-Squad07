```mermaid
sequenceDiagram
    participant BancoDeDados
    participant Scrapy

    Scrapy ->> BancoDeDados: Inserção de Dados
    BancoDeDados -->> Scrapy: Confirma Inserção
    Scrapy ->> BancoDeDados: Leitura de Dados
    BancoDeDados -->> Scrapy: Retorna Dados Lidos
