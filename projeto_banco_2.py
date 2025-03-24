
def menu():
    menu = """
    Opções

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Novo usuário
    [5] Nova conta
    [6] Listar contas
    [0] Sair

    => """
    return int(input(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("O deposito foi realizado com sucesso!")

    else:
        print("O valor do depósito é inválido!")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saque = numero_saques >= limite_saques

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
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("#" * 16)
    print("EXTRATO".center(16))
    print("#" * 16)
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}\n")
    print("=" * 32)

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe usuário com esse CPF!")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe sua data de nascimento(dd-mm-aaaa)")
    endereco = input("Informe o endereço (logradouro, numero - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("\nO usuário não foi encontrado")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\n
        Agência:\n{conta["agencia"]}
        C/C:\n{conta["numero_conta"]}
        Titular:\n{conta["usuario"]["nome"]}
        """
    print("=" *100)
    print(linha)



def main ():
    LIMITE_SAQUE = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == 1:
            valor = float(input("Qual o valor do depósito>"))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == 2:
            valor = float(input("Qual o valor de saque?"))

            saldo, extrato = sacar(saldo = saldo, valor = valor, extrato = extrato, limite = limite, numero_saques = numero_saques, limite_saques = LIMITE_SAQUE)

        elif opcao == 3:
            exibir_extrato(saldo, extrato = extrato)

        elif opcao == 4:
            criar_usuario(usuarios)

        elif opcao == 5:
            numero_conta = len(contas) +1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == 6:
            listar_contas(contas)

        elif opcao == 0:
            break

        else:
            print("Operação inválida!")

main()  
