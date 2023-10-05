#feito por Marcus
#Proz Educação
#Professor Gleison

acao = 0
saldo = 150
opcao = int(input("O que você deseja fazer? "))
print("[1]Sacar; [2]Depositar; [3]Ver quantidade do saldo.")

if opcao == 1:
    saque = float(input("Quanto você deseja sacar?" ))
    while saque > saldo:
        print("Saldo insuficiente")
        saque = float(input("Quanto você deseja sacar? "))
    saldo -= saque
    print("Saque efetuado! Seu saldo atual é de: ", saldo)
elif opcao  == 2:
    depos = float(input("Quanto você dejesa depositar? "))
    depos += saldo
    print("Deposito efetuado! Seu saldo atual é de: ", saldo)
elif opcao == 3:
    print("Seu saldo atual é de: ", saldo)