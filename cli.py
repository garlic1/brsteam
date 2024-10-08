# BRSteam - Etapa 2
# Gabriel Lima Chimifosk - 134078
# Willian Nunes Reichert - 134090

import sys
import os
import consultas as db

MENU = '''
    1: Usuários que gastaram mais de <x> reais
    2: Quantidade de usuários que adquiriram cada jogo
    3: Produtos que não suportam o sistema <x>
    4: Usuários que possuem todos os jogos da publicadora <publi>
    5: Jogos que não possuem conquistas
    6: Mensagens enviadas pelo usuário <user>
    7: Compras efetuadas pelo usuário <user>, comparação de preços pagos com os atuais
    8: Avaliações realizadas pelo usuário <user>
    9: Ranking de gêneros de produtos que o usuário <user> possui
    10: Jogos que possuem média de nota maior que <nota>
    0: Encerrar sessão
'''
OPCOES = '012345678910'
FUNCOES = {
    '1': db.gasto_usuarios,
    '2': db.usuarios_jogos,
    '3': db.suporte_sistema,
    '4': db.usuarios_publi,
    '5': db.sem_conquistas,
    '6': db.msgs_usuario,
    '7': db.compras_usuario,
    '8': db.avaliacoes_usuario,
    '9': db.generos_usuario,
    '10': db.media_jogos
}

def sep(titulo: str):
    print(f'\n{titulo}\n' + 80 * '-')

os.system('cls')
opcao = ''
while (opcao != '0'):
    sep('BRSteam')
    opcao = input(f'{MENU}\nOpção: ')
    while (opcao not in OPCOES):
        opcao = input(f'{MENU}\nOpção: ')
    if (opcao != '0'):
        FUNCOES[opcao]()
        input('\nPressione enter para retornar...')
        os.system('cls')

db.encerrar()
os.system('cls')
sys.exit(0)
