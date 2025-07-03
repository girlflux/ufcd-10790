# Risco de Incêndio por Concelho em Portugal Continental

## Contexto
Repositório com entrega para UFCD 10790 – Atividade Final – Github + Projeto | **ID: 7336277**

> *Nota*: este repositório continha originalmente um jogo incompleto em pygame. Agora contém uma aplicação web feita em Python com Flask e a API do IPMA.

<br>

## Apresentação do Projecto
Inicialmente desenvolvido como projecto de avaliação de módulo em Python Avançado, este projecto gera um website que, a partir de informação recolhida da API do Instituto Português do Mar e da Atmosfera (IPMA), mostra o risco de incêndio por concelho em Portugal Continental.

<br>

### Dependências
Para executar localmente o projecto é necessário ter **Python** a correr uma versão igual ou superior a 3.9 e instalar as seguintes dependências:
- [Flask](https://pypi.org/project/Flask/)
- [requests](https://pypi.org/project/requests/)

Método de instalação:
`pip install flask requests`

Verficação se as dependências foram instaladas:
`pip list`

<br>

### Referência Principal
O IPMA tem uma versão própria e bastante desenvolvido disponível — [visualizador web para o risco de incêndio](https://www.ipma.pt/en/riscoincendio/rcm.pt/) — completa com outras informações relevantes ao risco de incêndio e utilizando um mapa interactivo.

<br>

### Entendimento do Projecto
É possível obter mais informação sobre a API do IPMA aqui: [https://api.ipma.pt/](https://api.ipma.pt/).

Percorrendo a página podemos encontrar na secção dos serviços [*Previsão do Risco de Incêndio até 2 dias, informação agregada por dia*](https://api.ipma.pt/#C3) a explicação dos dados relativos ao risco de incêndio. As ligações à API a partir da qual se obtém o risco de incêndio estão nesta [pasta](https://api.ipma.pt/open-data/forecast/meteorology/rcm/) e são:
- ligação [para o presente dia](https://api.ipma.pt/open-data/forecast/meteorology/rcm/rcm-d0.json);
- ligação [para o dia seguinte](https://api.ipma.pt/open-data/forecast/meteorology/rcm/rcm-d1.json).

<br>

Lendo a explicação e observando os ficheiros json podemos ver que a listagem/referência aos concelhos é feita a partir do seu código DICO. O código DICO é um código numérico único a cada concelho. Segundo a API do IPMA:
> DICO: Identificador único de concelho (de acordo com a CAOP - DGT)

Para melhorar a acessibilidade da plataforma desenvolvida usei o [documento encontrado no sítio do Instituto da Conservação da Natureza e das Florestas](https://fogos.icnf.pt/pmdfci/Correspondencia_CodigosConcelhos.xlsx) que explicita a relação entre código e município. Esta relação é também possível explorar [neste website da Direção-Geral de Agricultura e Desenvolvimento Rural](http://mpb.dgadr.pt/ConcFreg.py) inclusive dando para ver quais os códigos relativos às freguesias de cada concelho.

<br>

Por curiosidade, ao investigar estes ficheiros, ficou claro que os códigos incrementam com uma lógica alfabética e embutida, ou seja:
```
Distrito de Aveiro: 01
    Concelho de Agueda: 0101
        Freguesia de Agadao: 010101
        Freguesia de Aguada de Baixo: 010102
        Freguesia de Aguada de Cima: 010103
        …
    Concelho de Albergaria-a-Velha: 0102
        Freguesia de Albergaria-a-Velha: 010201
        Freguesia de Alquerubim: 010202
        …
    …
Distrito de Beja: 02
    Concelho de Aljustrel: 0201
        Freguesia de ALjustrel: 020101
        …
    …
…
````

### Possibilidades Futuras
- [ ] Visualização do dia seguinte
- [ ] Inclusão de outros dados metereológicos
- [ ] Criar algum tipo de mecanismo de filtro que permita ver por risco
- [ ] Pesquisa por concelhos