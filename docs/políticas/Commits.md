---
tag: "politicas"
---
Padronização dos commits no projeto.

## Histórico de Versões


| Data       | Versão | Descrição                      | Autor             |
| :--------: | :----: | :----------:                   | :---------------: |
| 04/10/2023 |  0.1   | Criação da política de commits | [Júlia Takaki](https://github.com/juliatakaki)|

## Semântica do Commit

Os commits devem seguir o seguinte padrão:

### Princípios:

#### Commits atômicos
Sempre dividir em pequenos e significativos commits, fazendo com que cada commit tenha apenas uma funcionalidade.

#### Commits em português
Por ser um projeto voltado totalmente para um público brasileiro e por toda equipe ter mais afinidade com o português, foi decidido que todos os commits serão em pt-BR.

### Formato:
```
<tipo>(#número da issue): assunto
```

#### Tipos:
- :bulb: quando adicionar nova funcionalidade
- :repeat: quando alguma alteração for feita
- :cool: quando melhorias de formato/estrutura do código
- :racehorse: quando melhorar o desempenho
- 🚱  quando resolver memory leaks
- :pencil: quando escrever documentação
- :bug: quando consertar um problema
- :fire: quando remover código ou arquivos
- :green_heart: quando consertar problemas de Integração Contínua
- :white_check_mark: quando adicionar testes
- :lock: quando lidar com segurança
- :arrow_up: quando realizar o upgrade de dependências
- :arrow_down: quando realizar downgrade de dependências

#### Assunto:

- Deve possuir no máximo 50 caracteres

*Exemplo de commit:*
```
git commit -m ":bulb:(#02): botão na página inicial"
```

## Referências

DARTORA, João. Tudo o que você precisa saber sobre commits semânticos. *Ilegra*. Disponível em: <https://ilegra.com/blog/tudo-o-que-voce-precisa-saber-sobre-commits-semanticos/>. Acesso em: 05 de outubro de 2023.

2023-05-04-commits. Disponível em: <https://github.com/fga-eps-mds/2023.1-GuiaUnB/blob/main/doc/2023-05-04-commits.md>. Acesso em: 05 de outubro de 2023.