from prints import cabecalho, clean
from console import CashMachineConsole, AuthBankAccountConsole


def main():
    clean()

    cabecalho('*** School of Net - Caixa Eletrônico ***')

    if AuthBankAccountConsole.is_auth():
        clean()
        cabecalho('*** School of Net - Caixa Eletrônico ***')
        CashMachineConsole.call_operation() #lógica do caixa eletrônico
    else:
        print('Inválido')

if __name__ == '__main__':
    while True:
        main()

        input('Pressionae <ENTER> para continuar...')