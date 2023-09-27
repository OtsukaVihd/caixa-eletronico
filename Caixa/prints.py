import os

def cabecalho(msg):
    tam = len(msg)
    print('*'*tam)
    print(msg)
    print('*'*tam)


def clean():
    os.system('cls' if os.name == 'nt' else 'clear')


def opt_invalida():
    print('Opção inválida!')

