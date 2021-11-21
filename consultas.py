# BRSteam - Etapa 2
# Gabriel Lima Chimifosk - 134078
# Willian Nunes Reichert - 134090

import psycopg2 as ps

# Conexão --------------------------------------------------------------------------------------------------------------

conn = ps.connect('dbname=brsteam user=postgres password=123')
cur = conn.cursor()

# Consultas ------------------------------------------------------------------------------------------------------------

# Usuários que gastaram acima de <limite> reais.
def gasto_usuarios(limite: float):
    cmd = '''
        SELECT Biblioteca.nome, SUM(Compra.precopago)
        FROM Biblioteca JOIN Usuario ON (Biblioteca.nome = Usuario.nome)
            JOIN Produto ON (Biblioteca.nomeproduto = Produto.nome)
            JOIN Compra ON (Compra.codigoproduto = Produto.codigo AND Compra.codigousuario = Usuario.codigo)
        GROUP BY Biblioteca.nome
        HAVING SUM(Compra.precopago) > %s'''
    cur.execute(cmd, (str(limite),))
    print(f'\nUsuários que gastaram mais de R$ {limite}:\n{cur.fetchall()}')

# Quantidade de usuários que adquiriram cada jogo.
def usuarios_jogos():
    cmd = '''
        SELECT Produto.nome, COUNT(Compra.codigousuario)
        FROM Compra JOIN Produto ON (Compra.codigoproduto = Produto.codigo)
            JOIN Jogo ON (Compra.codigoproduto = Jogo.codigoproduto)
        GROUP BY Produto.nome
        '''
    cur.execute(cmd)
    print(f'\nQuantas pessoas tem cada jogo:\n{cur.fetchall()}')

# Quais jogos não suportam o sistema <sistema>.
def suporte_sistema():
    cmd = '''
        SELECT Produto.nome as nomeproduto
        FROM Produto JOIN Suporte ON (Produto.codigo = Suporte.codigoProduto)
            JOIN Sistema ON (Sistema.nome = Suporte.nomeSistema)
        WHERE Produto.nome NOT IN
        (
            SELECT Produto.nome as nomeproduto
            FROM Produto JOIN Suporte ON (Produto.codigo = Suporte.codigoProduto)
                JOIN Sistema ON (Sistema.nome = Suporte.nomeSistema)
            WHERE nomesistema = %s
        )'''
    cur.execute(cmd, ('Windows',))
    print(f'\nQuais jogos não suportam meu sistema:\n{cur.fetchall()}')

# Usuários que possuem todos os jogos da publicadora <publi>.
def usuarios_publi():
    cmd = '''
        SELECT nome
        FROM usuario as ext
        WHERE NOT EXISTS
        (
            SELECT codigoproduto
            FROM Publicacao JOIN Publicador ON (Publicacao.codigopublicador = Publicador.codigo)
            WHERE Publicador.nome = %s AND codigoproduto NOT IN
            (
                SELECT codigoproduto
                FROM Compra
                WHERE codigousuario = ext.codigo
            )
        )'''
    cur.execute(cmd, ('Valve',))
    print(f'\nUsuários que possuem todos os produtos da publicadora:\n{cur.fetchall()}')

# Jogos que não possuem conquistas.
def sem_conquistas():
    cmd = '''
        SELECT Produto.nome as nomeproduto
        FROM Produto JOIN Jogo ON (Produto.codigo = Jogo.codigoProduto)
        WHERE Produto.nome NOT IN
        (
            SELECT Produto.nome as nomeproduto
            FROM Produto JOIN Jogo ON (Produto.codigo = Jogo.codigoProduto) 
            JOIN Conquista ON (Jogo.codigoProduto = Conquista.codigoJogo)
        )'''
    cur.execute(cmd)
    print(f'\nJogos que não possuem conquistas:\n{cur.fetchall()}')

# Mensagens enviadas pelo usuário <usuario>.
def msgs_usuario():
    cmd = '''
        SELECT Usuario.nome as nomeusuario, conteudo, dataenvio
        FROM Usuario JOIN Mensagem ON (Usuario.codigo = Mensagem.codigoRemetente)
            JOIN Amizade ON (Usuario.codigo = Amizade.codigoSolicitante)
        WHERE Usuario.nome = %s'''
    cur.execute(cmd, ('william',))
    print(f'\nMensagens enviadas pelo usuário \'william\':\n{cur.fetchall()}')

# Histórico de compras do usuário <usuario> com comparação dos preços pagos com os atuais.
def compras_usuario():
    cmd = '''
        SELECT Produto.nome as nomeproduto, precopago, Produto.preco as precoatual
        FROM Usuario JOIN Compra ON (Usuario.codigo = Compra.codigousuario)
            JOIN Produto ON (Compra.codigoproduto = Produto.codigo)
        WHERE Usuario.nome = %s'''
    cur.execute(cmd, ('william',))
    print(f'\nCompras do usuário \'william\':\n{cur.fetchall()}')

# Avaliações realizadas pelo usuário <usuario>.
def avaliacoes_usuario():
    cmd = '''
        SELECT Produto.nome as nomeproduto, analise, nota
        FROM Usuario JOIN Avaliacao ON (Usuario.codigo = Avaliacao.codigousuario)
            JOIN Produto ON (Avaliacao.codigoproduto = Produto.codigo)
        WHERE Usuario.nome = %s'''
    cur.execute(cmd, ('william',))
    print(f'\nAvaliações do usuário \'william\':\n{cur.fetchall()}')

# Ranking de gêneros de produtos que o usuário <usuario> possui.
def generos_usuario():
    cmd = '''
        SELECT nomegenero, count(nomegenero) as numprodutos
        FROM Biblioteca JOIN Produto ON (Biblioteca.nomeproduto = Produto.nome)
            JOIN Categorizacao ON (Produto.codigo = Categorizacao.codigoProduto)
            JOIN Genero ON (Categorizacao.nomegenero = Genero.nome)
        GROUP BY nomegenero, Biblioteca.nome
        HAVING Biblioteca.nome = %s
        ORDER BY numprodutos DESC'''
    cur.execute(cmd, ('william',))
    print(f'\nRanking de gêneros do usuário \'william\':\n{cur.fetchall()}')

# Jogos que possuem média de nota maior que <nota>.
def media_jogos():
    cmd = '''
        SELECT nome as nomejogo, AVG(nota) as medianotas
        FROM Produto JOIN Jogo ON (Produto.codigo = Jogo.codigoProduto) 
            JOIN Avaliacao ON (Avaliacao.codigoproduto = Produto.codigo)
        GROUP BY nomejogo
        HAVING avg(nota) > %s'''
    cur.execute(cmd, ('6',))
    print(f'\nJogos com média maior que 6:\n{cur.fetchall()}\n')

def encerrar():
    conn.close()
