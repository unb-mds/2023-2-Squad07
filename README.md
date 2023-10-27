# 2023.2 - Squad 07 | LicitaX
<div align="center">
    <div style="display: inline-block; width: 30%; text-align: center;">
        <img src="https://i.pinimg.com/originals/bd/db/4d/bddb4d5d400a2724f5a94b3982d3d61e.png" style="width: 35%;"/>
        <p>Figura 1: Logo do LicitaX</p>
    </div>
    <div style="display: inline-block; width: 30%; text-align: center;">
        <img src="https://i.pinimg.com/originals/4b/36/fc/4b36fc30aaa87c5a5ae0f25d2e3a5d89.png" style="width: 20%;"/>
        <p>Figura 2: Logo do Querido Diário</p>
    </div>
    <div style="display: inline-block; width: 30%; text-align: center;">
        <img src="https://i.pinimg.com/originals/a5/34/49/a53449dbf40ab339b1ed613d53d57dfd.png" style="width: 20%;"/>
        <p>Figura 3: Logo do Exoonero</p>
    </div>
</div>

## Sobre o projeto
Este repositório contém o backend do Squad 07 da disciplina de Métodos de Desenvolvimento de Software. O objetivo é desenvolvermos um software com base no projeto open source Querido Diário tendo como projeto referência o Exoonero.

Conheça mais sobre a <a href="https://queridodiario.ok.org.br/sobre">história</a> do Querido Diário no <a href="https://queridodiario.ok.org.br/">site do Querido Diário</a>.

Saiba mais sobre o <a href="https://exoonero.org/sobre/">Exoonero</a>. 

Acesse nosso <a href="https://unb-mds.github.io/2023.2-LicitaX/">front-end</a>.

<a href="https://github.com/unb-mds/2023.2-LicitaX">Repositório do front-end</a>.

## Instruções de uso

### Pré-requisitos:

- Ubuntu 22.04.3
- Python 3.10 ou superior.
- Node.js 18.18.0 ou superior.
- Git 2.34.1 ou superior.
- Scrapy 2.11 ou superior.
- JDK 11.0.2 ou superior

Para começar a usar o software completo, você precisa clonar dois repositórios, primeiro clone o repositório do backend para a pasta desejada através do seguinte comando:

```bash
git clone https://github.com/unb-mds/2023-2-Squad07.git
```

Depois, navegue até a pasta src:

```bash
cd src
```

Após, navegue até diario_aprece:

```bash
cd diario_aprece
```

Abra o terminal e use o comando:

```bash
scrapy crawl spider_aprece
```

Após, insira o link do PDF do diário oficial (apenas do domínio www.diariomunicipal.com.br) e dê enter.

O Scrapy irá baixar o diário, o Apache Tika irá extrair o texto e processar a quantidade de vezes que a frase "aviso de licitação" ocorreu no diário oficial e irá gerar um JSON na pasta Public, na raiz do projeto.

Agora, clone o repositório do frontend para a pasta desejada através do seguinte comando:

```bash
git clone https://github.com/unb-mds/2023.2-LicitaX.git
```

Instale as dependências utilizadas através do comando:

```bash
yarn install
```

Inicie o servidor através do comando:

```bash
yarn dev
```

## Equipe

<table>
  <tr>
    <td align="center"><a href="https://github.com/joseandre25"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/98027989?v=4" width="100px;" alt=""/><br /><sub><b>José André</b></sub></a><br />
    <td align="center"><a href="https://github.com/juliatakaki"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/72303464?v=4" width="100px;" alt=""/><br /><sub><b>Júlia Takaki</b></sub></a><br />
    <td align="center"><a href="https://github.com/RafaBonach"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/104152350?v=4" width="100px;" alt=""/><br /><sub><b>Rafael Bonach</b></sub></a><br />
    <td align="center"><a href="https://github.com/gio221"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/111579005?v=4" width="100px;" alt=""/><br /><sub><b>Giovana Silva</b></sub></a><br /><a href="Link git" title="Rocketseat"></a></td>
    <td align="center"><a href="https://github.com/samarawwleticia"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/129631162?v=4" width="100px;" alt=""/><br /><sub><b>Samara Letícia</b></sub></a><br />
  </tr>
</table>
