saldo = 10
resposta = 'sim'

print('''Bem-vindo(a) ao Banco Star
      
      [1] Depósito
      [2] Saque
      [3] Extrato''')

escolha = int(input('Qual operação você desja realizar?: '))

while resposta == 'sim': 
    if escolha == 1:
        deposito = float(input('Qual valor deseja depositar?: '))
        if deposito < 1:
            print('Valor informado não pode ser adicionado, tente novamente...')
        elif deposito > 0:
            saldo += deposito
            print("Esse é o seu saldo atual: {}".format(saldo))
            resposta = str(input("deseja continuar com essa operação?: "))
            
            



