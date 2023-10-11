```mermaid
sequenceDiagram
    participant Raspagem
    participant DiarioOficial
    participant BancoDeDados
    participant GitHubPage

    Raspagem ->> DiarioOficial: Inicia Coleta
    DiarioOficial -->> Raspagem: Retorna Dados Coletados
    Raspagem ->> BancoDeDados: Insere Dados Coletados
    BancoDeDados -->> Raspagem: Confirma Inserção
    Raspagem ->> GitHubPage: Atualiza Página Web
    GitHubPage -->> Raspagem: Confirma Atualização

