# BRSteam - Etapa 2
# Gabriel Lima Chimifosk - 134078
# Willian Nunes Reichert - 134090

import sys
import consultas as db

OPCOES = '01'
MENU = '1: Usuários que gastaram acima de <x> reais'
FUNCOES = {
    '1': db.gasto_usuarios
}

def sep(titulo: str):
    print(f'\n{titulo}\n' + 80 * '-')

opcao = ''
while (opcao != '0'):
    sep('BRSteam')
    opcao = input(f'{MENU}\nOpção: ')
    while (opcao not in OPCOES):
        opcao = input(f'{MENU}\nOpção: ')
    if (opcao != '0'):
        FUNCOES[opcao](500)

db.encerrar()
sys.exit(0)
