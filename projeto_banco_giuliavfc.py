menu = """
Opções

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

while True:
        opcao = int(input(menu)) 

        if opcao == 1:
            valor = float(input("Qual o valor do depósito? "))

            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
            else:
                print("O valor do depósito é inválido!")

        elif opcao == 2:
            valor = float(input("Qual o valor do saque? "))

            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saque = numero_saques >= LIMITE_SAQUE

            if excedeu_saldo:
                print("Você não tem saldo suficiente!")
            elif excedeu_limite:
                print("Você não tem limite suficiente!")
            elif excedeu_saque:
                print("Número máximo de saques atingido!")
            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
            else:
                print("Valor informado é inválido!")

        elif opcao == 3:
            print("#" * 16)
            print("EXTRATO".center(16))
            print("#" * 16)
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}\n")
            print("=" * 32)

        elif opcao == 0:
            print("Saindo do sistema. Até mais!")
            break

        else:
            print("A opção escolhida não está disponível!")
