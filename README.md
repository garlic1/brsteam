# BRSTEAM

O Steam é, atualmente, a maior plataforma para jogos digitais de computador. Integrado a ela há um sistema de perfis no qual os usuários podem se adicionar e compartilhar conteúdos relacionados aos jogos. Na loja, os usuários podem adquirir produtos, que são subdivididos em Jogos e Soundtracks; e também escrever avaliações sobre os produtos.

O objetivo deste projeto é modelar os principais dados da loja e as relações do banco de dados com o usuário, porém apenas para usuários brasileiros. Para isso, utilizamos certos dados disponíveis abertamente na loja do Steam (https://store.steampowered.com/).

Utilizamos a linguagem Python 3.9, o SGBD PostgreSQL e a biblioteca psycopg2 para interagir com o servidor do PostgreSQL através de comandos em Python.

## Demonstração
https://youtu.be/UwriAmFzSCw

## Como executar
- clone o repositório para execução local
- execute localmente uma instância do PostgreSQL
- certifique-se que a versão do Python é 3.9
- execute `pip install psycopg2`
- execute `py instancias.py` para inicialização do banco de dados
- execute `py cli.py`
  
## Consultas
#### 1: Usuários que gastaram mais de [x] reais
  
Levanta estatísticas para o administrador saber quais usuários investiram mais na sua plataforma.

#### 2: Quantidade de usuários que adquiriram cada jogo
  
Levanta estatísticas para o administrador saber quais jogos são os mais populares.

#### 3: Produtos que não suportam o sistema [x]

Importante pro usuário saber se o jogo não suporta seu sistema.

#### 4: Usuários que possuem todos os jogos da publicadora [publi]

A consulta pode ser usada pelo sistema para recomendar novos jogos de uma certa publicadora para potenciais clientes.

#### 5: Jogos que não possuem conquistas
  
Alguns jogadores se importam muito com conquistas, e podem não querer comprar jogos que não possuem conquistas cadastradas no sistema.

#### 6: Mensagens enviadas pelo usuário [user]

Pode ser usado pelo administrador para consultar o histórico de mensagens do usuário, com intuito de verificar se há mensagens impróprias ou perigosas.

Usuários exemplo cadastrados:
  - william
  - alho

#### 7: Compras efetuadas pelo usuário [user], comparação de preços pagos com os atuais

Consulta feita pelo próprio usuário para analisar seu histórico de compras.

#### 8: Avaliações realizadas pelo usuário [user]

Usado pelo administrador para filtrar as avaliações a serem publicadas com base nas que o usuário já publicou, ou pelo próprio usuário para ver suas próprias avaliações.

#### 9: Ranking de gêneros de produtos que o usuário [user] possui

Usada para recomendar gêneros personalizadamente para cada usuário.

#### 10: Jogos que possuem média de nota maior que [nota]

Usuário pode pesquisar na loja apenas jogos que possuam boas avaliações.

## Detalhes

No banco de dados, modelamos:
- os principais dados da loja (no caso, os produtos, como jogos e trilhas sonoras)
- relações dos usuários com os produtos (como as compras, a inserção de avaliações com nota e texto para cada produto) 
- as interações entre usuários, consolidada através de um sistema de amizade e troca de mensagens.

Utilizamos a linguagem Python 3.9, o SGBD PostgreSQL e a biblioteca psycopg2 para interagir com o servidor do PostgreSQL através de comandos em Python.

Detalhes técnicos adicionais do banco de dados podem ser consultados no arquivo `spec.pdf`. 

## Diagrama Entidade-relacionamento
![image](https://github.com/user-attachments/assets/6ae3bfcb-d203-4881-af0b-a2f31f2b5c39)
