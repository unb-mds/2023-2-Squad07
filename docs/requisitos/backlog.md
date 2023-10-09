---
excerpt: ""
---

Esse documento contêm os itens que deverão ser desenvolvidos pelo squad, levando em conta os requisitos levantados. 

## Histórico de revisão

  | Data       | Versão | Alteração                             | Autores                                               |
  | ---------- | ------ | ------------------------------------- | --------------------------------------------------- |
  | 09/10/2023 | 0.1    | Primeira definição de funcionalidades | [José André](https://github.com/joseandre25) e [Giovana Barbosa ](https://github.com/gio221)|
  

## 1. Introdução

### 1.1 Abreviações e seus significados

| Abreviação | Significado  |
| ---------- | ------------ |
| EP         | Epics        |
| FT         | Features     |
| US         | User Stories |

### 1.2 Termos importantes que serão utilizados nesse documento

| Termo        | Definição                                                                                  |
| ------------ | ------------------------------------------------------------------------------------------ |
| Epics        | Epics são descrições gerais do que se deseja no software                                   |
| Features     | Features são semelhantes a Epics, porém são mais detalhadas em relação ao que é função     |
| User Stories | User Stories são exemplos de usuários que irão utilizar a função de uma feature em questão |

### 1.3 Priorização com MoSCoW

O MoSCoW é uma técnica utilizada para definir a prioridade dos requisitos presentes no projeto. As classificações são dadas por Must, Should, Could e Won't, que juntas formam o acrônimo MoSCoW. Essas classificações são dadas, para que se possa hierarquizar a necessidade dos requisitos ao projeto. Entendendo as regras de priorização, fizemos essa classificação para dar início à abertura desse documento.

- Must: Deve ter este requisito para atender às necessidades de negócios.
- Should: Deve ter este requisito, se possível, mas o sucesso do projeto não depende dele.
- Could: Pode ter este requisito se não afetar mais nada no projeto.
- Won't: Gostaria de ter esse requisito mais tarde, mas a entrega não será desta vez.

## 2. Backlog

### EP01: Sobre o projeto
Será uma epic para ser uma informação inicial, onde o usuário terá o primeiro contato com a aplicação e terá uma breve explicação sobre como usa-la.

#### FT01: Boas-Vindas

| ID   | User Story                                                                                                                                                                                      | Prioridade | Pontos |
| ---- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ------ |
| US01 | Como usuário, eu quero ver uma tela de abertura quando eu abrir a aplicação, para que eu saiba que ele está carregando corretamente.                                                           | Must       | 1      |
| US02 | Como usuário, quero ver uma tela de sobre o projeto com uma breve introdução à aplicação e suas funcionalidades, para que eu possa ter uma ideia do que esperar e como usar a aplicação. | Must       | 1      |

#### FT02: Introdução

| ID   | User Story                                                                                                                                                          | Prioridade | Pontos |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ------ |
| US03 | Como usuário, eu quero ver uma breve explicação sobre a aplicação para entender como ele pode me ajudar a visualizar a quantidade de abertura de editais de licitação em determinado município do Ceará.                         | Must       | 1      |
| US04 | Como usuário, eu quero ter acesso ao código fonte da aplicação.             | Must       | 2      |

#### FT03: Navegação

| ID   | User Story                                                                                                                                               | Prioridade | Pontos |
| ---- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ------ |
| US05 | Como usuário, quero ser capaz de navegar facilmente pelas diferentes seções da aplicação para encontrar informações relevantes de forma rápida e fácil. | Must       | 2      |
| US06 | Como usuário, quero ser capaz de voltar para a página anterior a qualquer momento, caso eu precise rever uma informação anterior.                        | Must       | 1      |
| US07 | Como usuário, quero ser capaz de pesquisar por palavras-chave ou frases para encontrar informações específicas dentro da aplicação.                    | Could     | 8      |
| US08 | Como usuário, quero que a navegação na aplicação seja intuitiva e fácil de entender, independentemente do meu nível de experiência com tecnologia.      | Must       | 2      |


### EP02: Pesquisa
Será uma epic para detalhar as formas de pesquisar na aplicação.

#### FT04: Pesquisa por Município

| ID   | User Story                                                                                                                                                                                                    | Prioridade | Pontos |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ------ |
| US09 | Como usuário, gostaria de poder pesquisar um município específico para ver a quantidade de editais de licitação abertos.  | Must       | 2      |


#### FT05: Pesquisa por Data
| ID   | User Story                                                                                                                                             | Prioridade | Pontos |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- | ------ |
| US10 |  Como usuário, gostaria de poder pesquisar um período de data específico e ver a quantidade de editais de licitação abertos.                                                          | Must       | 2      |


#### FT06: Pesquisa por Palavra-Chave
| ID   | User Story                                                                                                                                             | Prioridade | Pontos |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- | ------ |
| US11 | Como usuário, quero poder pesquisar no Diário Oficial usando palavras-chave relevantes para encontrar editais de licitação relacionados às minhas necessidades.                                                      | Must       | 2  |

### EP03: Retorno
Será uma epic para detalhar o retorno desejado nas pesquisas.

#### FT07: Exibir Resultados de Pesquisa

| ID   | User Story                                                                                                                                                                                                    | Prioridade | Pontos |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ------ |
| US12 | Como usuário, quero ver os resultados da minha pesquisa de forma clara e específica, incluindo a citação relevante e a data em que a palavra-chave foi referenciada. | Must       | 2      |

#### FT08: Quantidade de editais de licitação

| ID   | User Story                                                                                                                                                                                                    | Prioridade | Pontos |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ------ |
| US13 | Como usuário, quero poder visualizar a quantidade de editais de licitação abertos por cada município do Estado do Ceará em um período de tempo específico. | Must       | 2      |


### EP04: Municípios que mais abrem editais e os que menos abrem
Será uma epic para mostrar as estatistícas dos municípios que mais abrem editais e os que menos abrem.

#### FT09: Destacar o que mais abre e o que menos abre
| ID   | User Story                                                                                                                                               | Prioridade | Pontos |
| ---- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ------ |
| US14 | Como usuário, quero poder ver qual município no Estado do Ceará que mais abre editais de licitação. | Must       | 2      |
| US15 | Como usuário, quero poder ver qual município no Estado do Ceará que menos abre editais de licitação.                        | Must       | 1      |

## Referências

- Railsware Product Academy. MoSCoW prioritization for your product backlog. Youtube, 19 de Setembro de 2019. Disponível em: https://www.youtube.com/watch?v=DzruAbBhY0Q. Acesso em: 09 de outubro de 2023.