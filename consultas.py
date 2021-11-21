# BRSteam - Etapa 2
# Gabriel Lima Chimifosk - 134078
# Willian Nunes Reichert - 134090

import psycopg2 as ps

conn = ps.connect('dbname=brsteam user=postgres password=123')
cur = conn.cursor()


# gasto no steam (acima de 500 reais)
cmd = '''
    SELECT Biblioteca.nome, SUM(Compra.precopago)
    FROM Biblioteca JOIN Usuario ON (Biblioteca.nome = Usuario.nome)
        JOIN Produto ON (Biblioteca.nomeproduto = Produto.nome)
        JOIN Compra ON (Compra.codigoproduto = Produto.codigo AND Compra.codigousuario = Usuario.codigo)
    GROUP BY Biblioteca.nome
    HAVING SUM(Compra.precopago) > 500'''
cur.execute(cmd)
print(f'\nGasto no steam (acima de 500):\n{cur.fetchall()}')

# quantas pessoas tem cada jogo
cmd = '''
    SELECT Produto.nome, COUNT(Compra.codigousuario)
    FROM Compra JOIN Produto ON (Compra.codigoproduto = Produto.codigo)
        JOIN Jogo ON (Compra.codigoproduto = Jogo.codigoproduto)
    GROUP BY Produto.nome
    '''
cur.execute(cmd)
print(f'\nQuantas pessoas tem cada jogo:\n{cur.fetchall()}')

# quais jogos não suportam meu sistema
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

# usuários que possuem todos os produtos da publicadora
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
print(f'\nUsuários que possuem todos os produtos da publicadora:\n{cur.fetchall()}\n')

conn.close()
