menu = """==============

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

==============
=> """

saldo = 0
limite = 500
extrato = "Extrato \n"
numero_saques = 0
LIMITE_SAQUES = 3
codigo_op = 0

while True:

    opcao = input(menu)

    if opcao == "d": 
        deposito = float(input("\ninforme o valor do depósito: "))
        saldo = saldo + deposito
        codigo_op = codigo_op + 1 
        print(f"\nOperação Nº: {codigo_op} -> Depósito de R$ {deposito:.2f} realizado. Saldo total: {saldo:.2f}\n")
        add_extrato = str(f"\nOperação Nº: {codigo_op} -> Depósito de R$ {deposito:.2f} realizado. Saldo total: {saldo:.2f}\n")
        extrato = extrato + add_extrato + ("\n")

    elif opcao == "s":
        if numero_saques < 3:
            saque = float(input("\ninforme o valor do saque: "))
            if saque <= limite:
                if saque < saldo:
                    saldo = saldo - saque
                    numero_saques = numero_saques + 1
                    codigo_op = codigo_op + 1 
                    print(f"\nOperação Nº: {codigo_op} -> Saque de R$ {saque:.2f} realizado. Saldo total: R$ {saldo:.2f}\n")
                    add_extrato = str(f"\nOperação Nº: {codigo_op} -> Saque de R$ {saque:.2f} realizado. Saldo total: R$ {saldo:.2f}\n")
                    extrato = extrato + add_extrato + ("\n")
                else:
                    print("\nSaldo insuficiente.\n")
            else:
                print("\nDesculpe, o valor excede seu limite de R$ 500.00 por saque.\n")
        else:
            print("\nDesculpe, você atingiu seu limite diário de 03 saques.\n")

    elif opcao == "e":
        print(f"\n##########################\n{extrato}\n##########################\n")
    elif opcao == "q":
        print("\nAcesso encerrado.\n")
        break

    else:
        print("Opção inválida. Favor digite uma das opções do menu:")