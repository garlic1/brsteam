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
    0: Encerrar sessão
'''
OPCOES = '0123'
FUNCOES = {
    '1': db.gasto_usuarios,
    '2': db.usuarios_jogos,
    '3': db.suporte_sistema
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
