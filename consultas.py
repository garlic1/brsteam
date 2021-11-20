# BRSteam - Etapa 2
# Gabriel Lima Chimifosk - 134078
# Willian Nunes Reichert - 134090

import psycopg2 as ps

conn = ps.connect('dbname=brsteam user=postgres password=123')
cur = conn.cursor()


# gasto no steam (acima de 500 reais having) (group by)
cmd = '''
    SELECT Biblioteca.nome, SUM(Compra.precopago)
    FROM Biblioteca JOIN Usuario ON (Biblioteca.nome = Usuario.nome)
        JOIN Produto ON (Biblioteca.nomeproduto = Produto.nome)
        JOIN Compra ON (Compra.codigoproduto = Produto.codigo AND Compra.codigousuario = Usuario.codigo)
    GROUP BY Biblioteca.nome
    HAVING SUM(Compra.precopago) > 500'''
cur.execute(cmd)
print(f'\nGasto no steam (acima de 500):\n{cur.fetchall()}')

# quantas pessoas tem cada jogo (group by)
cmd = '''
    SELECT Produto.nome, COUNT(Compra.codigousuario)
    FROM Compra JOIN Produto ON (Compra.codigoproduto = Produto.codigo)
        JOIN Jogo ON (Compra.codigoproduto = Jogo.codigoproduto)
    GROUP BY Produto.nome
    '''
cur.execute(cmd)
print(f'\nQuantas pessoas tem cada jogo:\n{cur.fetchall()}')

conn.close()
