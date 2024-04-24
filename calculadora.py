import os
import time

saldo = 0
limite_500 = 0.0
resposta = 'sim'
depositos_lista = []
saque_lista = []

print('Bem-vindo(a) ao Banco Star')

while resposta.lower().startswith('s'):
    print('''
      
      [0] Sair
      [1] Depósito
      [2] Saque
      [3] Extrato''')

#VerificandoRespostaDoUsuario
    try:
        escolha = int(input('Qual operação você deseja realizar?: '))
    except ValueError:
        print("Por favor, digite um número válido.")

    time.sleep(2)
    os.system('cls')

 #OperaçãoDeDepósito:
    if escolha == 1:
        deposito = float(input('Qual valor deseja depositar?: '))
        depositos_lista.append(deposito)
        time.sleep(2)
        os.system('cls')
        if deposito < 1:
            print('Valor informado não pode ser adicionado, tente novamente...')
        elif deposito > 0:
            saldo += deposito
            print("Esse é o seu saldo atual: {}".format(saldo))
            resposta = str(input("Deseja continuar com essa operação?: "))
    
    #OperaçãoDeSaque:
    elif escolha == 2:
        saque = float(input("Qual valor deseja sacar?: "))
        if saque < saldo and saque <= 500:
            if saque == 500:
                if limite_500 < 3:
                    limite_500 += 1 
                else:
                    print("Limite diário de 3 saques de R$500 excedido...")
                    continue

            saque_lista.append(saque)        
            saldo -= saque
            print("Esse é o seu saldo atual: {}".format(saldo))
            resposta = str(input("Deseja continuar com a operação?: "))

        elif saque > saldo:
            print("Você não tem saldo suficiente para realizar essa operação...")
                
        elif saque > 500:
            print("Você ultrapassou o limite de R$500...")

#VerificandoExtrato
    elif escolha == 3:
        print("Operações realizadas em sua conta nos ultimos dias: ")
        print("--------------------------------------------------")

        print("""Lista de depósitos realizados: 
                {} """.format(depositos_lista))
        
        print("-----------------------------------------------------")
        
        print('''Lista de saques realizados: 
                {}'''.format(saque_lista))
        
        resposta = str(input("Deseja continuar com a operação?: "))
    else:
        break


print("Operação finalizada...")

