```mermaid
sequenceDiagram
    participant Raspagem
    participant BancoDeDados
    participant PaginaWeb

    Raspagem ->> BancoDeDados: Coleta de Dados
    BancoDeDados ->> BancoDeDados: Inserção de Dados
    BancoDeDados ->> PaginaWeb: Leitura de Dados
    PaginaWeb -->> PaginaWeb: Visualização de Dados
