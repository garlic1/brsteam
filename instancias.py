# BRSteam - Etapa 2
# Gabriel Lima Chimifosk - 134078
# Willian Nunes Reichert - 134090

import psycopg2 as ps

conn = ps.connect('dbname=brsteam user=postgres password=123')
cur = conn.cursor()


tables = ('Amizade', 'Avaliacao', 'Categorizacao', 'Compra', 'Conquista', 'Desenvolvedor', 'Desenvolvimento', 'DLC',
'Faixa', 'Genero', 'Jogo', 'Mensagem', 'Produto', 'Publicacao', 'Publicador', 'Sistema', 'Soundtrack', 'Suporte',
'Usuario')

for table in tables:
  cur.execute(f'DROP TABLE IF EXISTS {table} CASCADE')

cur.execute(
'''CREATE TABLE IF NOT EXISTS Usuario(
  codigo INTEGER UNIQUE NOT NULL,
  nome VARCHAR(50) UNIQUE NOT NULL,
  dataCriacao DATE UNIQUE NOT NULL,
  ban BOOLEAN,
PRIMARY KEY (codigo));''')

cur.execute(
'''CREATE TABLE IF NOT EXISTS Produto(
  codigo INTEGER UNIQUE NOT NULL,
  nome VARCHAR(50) UNIQUE NOT NULL,
  dataLancamento date,
  dataAtualizacao TIMESTAMP NOT NULL,
  desconto SMALLINT CHECK (desconto BETWEEN 1 AND 100),
  preco NUMERIC(6,2),
  PRIMARY KEY (codigo));''')

cur.execute(
'''CREATE TABLE IF NOT EXISTS Jogo(
  codigoProduto INTEGER UNIQUE NOT NULL,
  isDemo BOOLEAN NOT NULL,
  FOREIGN KEY (codigoProduto) REFERENCES Produto(codigo));''')

cur.execute(
'''CREATE TABLE IF NOT EXISTS DLC(
  codigoProduto INTEGER UNIQUE NOT NULL,
  codigoJogo INTEGER NOT NULL,
  FOREIGN KEY (codigoJogo)REFERENCES Jogo(codigoProduto),
  FOREIGN KEY (codigoProduto) REFERENCES Produto(codigo));''')

cur.execute(
'''CREATE TABLE IF NOT EXISTS Soundtrack(
  codigoProduto INTEGER UNIQUE NOT NULL,
  qtdeFaixas SMALLINT NOT NULL,
  duracao NUMERIC(5,2) NOT NULL,
  FOREIGN KEY (codigoProduto) REFERENCES Produto(codigo));''')

cur.execute(
'''CREATE TABLE IF NOT EXISTS Faixa(
  codigoSoundtrack INTEGER NOT NULL,
  posicaoFaixa SMALLINT UNIQUE NOT NULL,
  nome VARCHAR(50) NOT NULL,
  duracao NUMERIC(4,2) NOT NULL,
  compositor VARCHAR(50) NOT NULL,
  FOREIGN KEY (codigoSoundtrack) REFERENCES Soundtrack(codigoProduto),
  PRIMARY KEY (codigoSoundtrack, posicaoFaixa));''')

cur.execute(
'''CREATE TABLE IF NOT EXISTS Desenvolvedor(
  codigo INTEGER UNIQUE NOT NULL,
  nome VARCHAR(50) UNIQUE NOT NULL,
  PRIMARY KEY(codigo));''')

cur.execute(
'''CREATE TABLE IF NOT EXISTS Publicador(
  codigo INTEGER UNIQUE NOT NULL,
  nome VARCHAR(50) UNIQUE NOT NULL,
  PRIMARY KEY(codigo));''')

cur.execute(
'''CREATE TABLE IF NOT EXISTS Sistema(
  nome VARCHAR(7) UNIQUE NOT NULL,
 PRIMARY KEY (nome));''') 

cur.execute(
'''CREATE TABLE IF NOT EXISTS Genero(
  nome VARCHAR(20) UNIQUE NOT NULL,
  PRIMARY KEY (nome));''')

cur.execute(
'''CREATE TABLE IF NOT EXISTS Conquista(
  codigo INTEGER UNIQUE NOT NULL,
  nome VARCHAR(50) UNIQUE NOT NULL,
  descricao VARCHAR(500) UNIQUE NOT NULL,
  escondido BOOLEAN NOT NULL,
  contador INTEGER,
  codigoJogo INTEGER NOT NULL,
  PRIMARY KEY (codigo),
  FOREIGN KEY (codigoJogo) REFERENCES Jogo(codigoProduto));''')

cur.execute(
'''CREATE TABLE IF NOT EXISTS Desenvolvimento(
  codigoProduto INTEGER NOT NULL,
  codigoDesenvolvedor INTEGER NOT NULL,
  PRIMARY KEY (codigoProduto, codigoDesenvolvedor),
  FOREIGN KEY (codigoProduto) REFERENCES Produto(codigo),
  FOREIGN KEY (codigoDesenvolvedor) REFERENCES Desenvolvedor(codigo));''')

cur.execute(
'''CREATE TABLE IF NOT EXISTS Publicacao(
  codigoProduto INTEGER NOT NULL,
  codigoPublicador INTEGER NOT NULL,
  PRIMARY KEY (codigoProduto, codigoPublicador),
  FOREIGN KEY (codigoProduto) REFERENCES Produto(codigo),
  FOREIGN KEY (codigoPublicador) REFERENCES Publicador(codigo));''')

cur.execute(
'''CREATE TABLE IF NOT EXISTS Categorizacao(
  codigoProduto INTEGER NOT NULL,
  nomeGenero VARCHAR(20) NOT NULL,
  PRIMARY KEY (codigoProduto, nomeGenero),
  FOREIGN KEY (codigoProduto) REFERENCES Produto(codigo),
  FOREIGN KEY (nomeGenero) REFERENCES Genero(nome));''')

cur.execute(
'''CREATE TABLE IF NOT EXISTS Suporte(
  codigoProduto INTEGER NOT NULL,
  nomeSistema VARCHAR(7) NOT NULL,
  PRIMARY KEY (codigoProduto, nomeSistema),
  FOREIGN KEY (codigoProduto) REFERENCES Produto(codigo),
  FOREIGN KEY (nomeSistema) REFERENCES Sistema(nome));''')

cur.execute(
'''CREATE TABLE IF NOT EXISTS Compra(
  codigoProduto INTEGER NOT NULL,
  codigoUsuario INTEGER NOT NULL,
  formaPagamento VARCHAR(50) NOT NULL,
  dataCompra DATE NOT NULL,
  precoPago NUMERIC(6,2) NOT NULL,
  PRIMARY KEY (codigoProduto, codigoUsuario),
  FOREIGN KEY (codigoProduto) REFERENCES Produto(codigo),
  FOREIGN KEY (codigoUsuario) REFERENCES Usuario(codigo));''')

cur.execute(
'''CREATE TABLE IF NOT EXISTS Avaliacao(
  codigoProduto INTEGER NOT NULL,
  codigoUsuario INTEGER NOT NULL,
  dataAvaliacao DATE NOT NULL,
  nota SMALLINT NOT NULL CHECK (nota BETWEEN 0 AND 10),
  analise VARCHAR(500),
  PRIMARY KEY (codigoProduto, codigoUsuario),
  FOREIGN KEY (codigoProduto) REFERENCES Produto(codigo),
  FOREIGN KEY (codigoUsuario) REFERENCES Usuario(codigo));''')

cur.execute(
'''CREATE TABLE IF NOT EXISTS Amizade(
  codigoSolicitante INTEGER NOT NULL,
  codigoSolicitado INTEGER NOT NULL,
  dataSolicitacao DATE NOT NULL,
  PRIMARY KEY (codigoSolicitante, codigoSolicitado),
  FOREIGN KEY (codigoSolicitante) REFERENCES Usuario(codigo),
  FOREIGN KEY (codigoSolicitado) REFERENCES Usuario(codigo));''')

cur.execute(
'''CREATE TABLE IF NOT EXISTS Mensagem(
  codigoRemetente INTEGER NOT NULL,
  codigoDestinatario INTEGER NOT NULL,
  dataEnvio TIMESTAMP NOT NULL,
  conteudo VARCHAR(500) NOT NULL,
  PRIMARY KEY (codigoRemetente, codigoDestinatario, dataEnvio),
  FOREIGN KEY (codigoRemetente) REFERENCES Usuario(codigo),
  FOREIGN KEY (codigoDestinatario) REFERENCES Usuario(codigo));''')

conn.commit()

cur.execute('''INSERT INTO sistema VALUES('Windows');''')
cur.execute('''INSERT INTO sistema VALUES('macOS');''')
cur.execute('''INSERT INTO sistema VALUES('Linux');''')
cur.execute('''INSERT INTO usuario VALUES (1,'lucanofraga2','2011-01-08',true);''')
cur.execute('''INSERT INTO usuario VALUES (2,'william','2011-01-09',false);''')
cur.execute('''INSERT INTO usuario VALUES (3,'alho','2011-01-10',false);''')

cur.execute('''INSERT INTO Produto VALUES (730,'Counter-Strike: Global Offensive','2012-08-21','2021-08-17 15:28:46');''')
cur.execute('''INSERT INTO Produto VALUES (6784,'Touhou Dirutinea','2019-08-21','2021-11-20 20:22:46');''')
cur.execute('''INSERT INTO Jogo VALUES(6784, false);''')
cur.execute('''INSERT INTO Produto VALUES (391570,'UNDERTALE Soundtrack','2015-09-15','2021-10-01 04:05:00',NULL,19.99);''')
cur.execute('''INSERT INTO Jogo VALUES(730,false);''')
cur.execute('''INSERT INTO Produto VALUES(271590,'Grand Theft Auto V','2015-04-13','2021-10-01 18:10:00',NULL,69.99);''')
cur.execute('''INSERT INTO Jogo VALUES(271590,false);''')
cur.execute('''INSERT INTO Produto VALUES(218620,'PAYDAY 2','2013-08-13','2021-10-01 10:07:00',NULL,23.99);''')
cur.execute('''INSERT INTO Produto VALUES(1746580,'PAYDAY 2: Jiu Feng Smuggler Pack 3','2021-09-22','2021-10-3 18:07:47',NULL,8.69);''')
cur.execute('''INSERT INTO Jogo VALUES(218620,false);''')
cur.execute('''INSERT INTO DLC VALUES(1746580,218620);''')

cur.execute('''INSERT INTO Soundtrack VALUES(391570,101,132.12);''')
cur.execute('''INSERT INTO Faixa VALUES(391570,1,'Once Upon a Time',1.28,'Toby Fox');''')
cur.execute('''INSERT INTO Faixa VALUES(391570,2,'Start Menu',0.32,'Toby Fox');''')
cur.execute('''INSERT INTO Faixa VALUES(391570,3,'Your Best Friend',0.23,'Toby Fox');''')
cur.execute('''INSERT INTO Faixa VALUES(391570,4,'Fallen Down',0.57,'Toby Fox');''')
cur.execute('''INSERT INTO Faixa VALUES(391570,5,'Ruins',1.32,'Toby Fox');''')
cur.execute('''INSERT INTO Faixa VALUES(391570,6,'Uwa!! So Temperate',0.56,'Toby Fox');''')
cur.execute('''INSERT INTO Genero VALUES('Ação');''')
cur.execute('''INSERT INTO Genero VALUES('Aventura');''')
cur.execute('''INSERT INTO Genero VALUES('Corrida');''')
cur.execute('''INSERT INTO Genero VALUES('FPS');''')
cur.execute('''INSERT INTO Genero VALUES('Luta');''')
cur.execute('''INSERT INTO Genero VALUES('RPG');''')


cur.execute('''INSERT INTO Conquista VALUES(1,'Someone Set Up Us The Bomb','Win a round by planting a bomb',false,NULL,730);''')
cur.execute('''INSERT INTO Conquista VALUES(24,'Uma dinheirama','Gaste um total de $200 milhões entre todos os três personagens.',false,154654895,271590);''')

cur.execute('''INSERT INTO Desenvolvedor VALUES (123,'Valve');''')
cur.execute('''INSERT INTO Publicador VALUES (123,'Valve');''')

cur.execute('''INSERT INTO Amizade VALUES (2,3,'2021-10-03');''')

cur.execute('''INSERT INTO Mensagem VALUES (2,3,'2021-10-03 21:52:00','Eu william gosto de sgbd');''')
cur.execute('''INSERT INTO Mensagem VALUES (3,2,'2021-10-03 21:52:01','eu tb');''')

cur.execute('''INSERT INTO Avaliacao VALUES (730,2,'2021-10-03',10,'Eu william aaaaaaaaaamo counter strike global offensive muuuito bom!!! Recomendo!!');''')
cur.execute('''INSERT INTO Avaliacao VALUES (391570,2,'2021-10-03',0,'Eu william ODIEI a soundtrack do UNDERTALE. Me doeu os ouvidos. Melhor escutar um quadro sendo arranhado.');''')

cur.execute('''INSERT INTO Compra VALUES (730, 2, 'Boleto', '2013-10-02', 27.49);''')
cur.execute('''INSERT INTO Compra VALUES (391570, 2, 'Boleto', '2018-10-02', 500.49);''')
cur.execute('''INSERT INTO Compra VALUES (271590, 1, 'Boleto', '2013-10-02', 27.49);''')
cur.execute('''INSERT INTO Compra VALUES (391570, 1, 'Boleto', '2018-10-02', 45.49);''')
cur.execute('''INSERT INTO Compra VALUES (218620, 3, 'Boleto', '2013-10-02', 89.49);''')
cur.execute('''INSERT INTO Compra VALUES (271590, 3, 'Boleto', '2018-10-02', 500.49);''')

cur.execute('''INSERT INTO Suporte VALUES (730, 'Linux');''')
cur.execute('''INSERT INTO Suporte VALUES (730, 'Windows');''')
cur.execute('''INSERT INTO Suporte VALUES (730, 'macOS');''')
cur.execute('''INSERT INTO Suporte VALUES (391570, 'Linux');''')

conn.commit()

cmd = '''CREATE VIEW Biblioteca AS
    SELECT Usuario.nome, Produto.nome as NomeProduto FROM 
    Compra JOIN Usuario ON (Compra.codigousuario = Usuario.codigo)
      JOIN Produto ON (Produto.codigo = Compra.codigoProduto);'''
cur.execute(cmd)

conn.commit()
conn.close()
