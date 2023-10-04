---
tag: "politicas"
---
Padronização das branches no projeto. 

## Histórico de Versões


| Data       | Versão | Descrição                                 | Autor             |
| :--------: | :----: | :----------:                              | :---------------: |
| 04/10/2023 |  0.1   | Criação da política de branch             | [Júlia Takaki](https://github.com/juliatakaki)



## Padronização das Branches
A adoção de uma abordagem de padronização das branches em sistemas de controle de versão, como o GitHub, é uma prática incrivelmente valiosa para o desenvolvimento colaborativo e eficiente de software. Essa estratégia traz consigo inúmeras vantagens que desempenham um papel fundamental na organização, colaboração e qualidade do código-fonte. A seguir, vamos explorar os benefícios dessa prática e como ela pode aprimorar significativamente o processo de desenvolvimento do nosso projeto.

### Prefixos:
- ```feature```
- ```hotfix```
- ```docs```

### Formato:
```
<prefixo>#número da issue/assunto
```

Não esquecer de dividir as palavras(sempre minúsculas) do assunto com "-".
Exemplo: 
```
feature#87/novo-menu
```

### Branches:

- **Branch main:** Branch que contém o código em nível de produção, será o código mais consolidado existente na aplicação. Nenhum integrante dos times é autorizado a fazer commits diretamente na *main.*
- **Branch dev:** Como o nome já diz, é a branch de trabalho no momento do desenvolvimento. São criadas começando com o prefixo **dev/**.
- **Branches feature:** Como o nome já diz, são branches na qual são desenvolvidos novos recursos ao projeto. São criadas começando com o prefixo **feature/**.
Exemplo: ```feature#22/novo-layout```
- **Branches hotfix:** Branches no qual são realizadas correções de bugs São criadas começando com o prefixo **hotfix/**.
Exemplo: ```hotfix#02/correcao-botao```
- **Branches docs:** Branches na qual são desenvolvidos os documentos do projeto. São ciradas começando com o prefixo **docs/**
Exemplo: ```docs#49/template-documento```

### Princípios:
- Como padronização optamos por nomear as branches em inglês, para toda a duração do projeto.

## Referências

DULCETTI, Bruno. Padrões e nomenclaturas no Git. *BrunoDulcetti*. Disponível em: <https://www.brunodulcetti.com/padroes-e-nomenclaturas-no-git/>. Acesso em: 4 de outrubo de 2023.

2023-05-04-branches. Disponível em: <https://github.com/fga-eps-mds/2023.1-GuiaUnB/blob/main/doc/2023-05-04-branches.md#formato. Acesso em: 4 de outubro de 2023.

HADLER, Mikael. Utilizando o fluxo Git Flow. *Medium*. Disponível em: <https://medium.com/trainingcenter/utilizando-o-fluxo-git-flow-e63d5e0d5e04>. Acesso em: 4 de outubro de 2023.
