import textwrap

def menu():
    menu = '''
    ('❀ ˖⁺. ༶ ⋆BEM VINDO(A). ༶ ⋆˙⊹ ❀')
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova Conta
    [lc] Listar Contas
    [nu] Novo Usuário
    [x] Sair
    => '''
    return input(textwrap.dedent(menu))

def depositar(saldo,valor,extrato,/):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n₊˚⊹♡ Depósito realizado com sucesso! ₊˚⊹♡")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. ฅ^•ﻌ•^ฅ")

    return saldo, extrato

def sacar (*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\nOperação falhou! Você não tem saldo suficiente. ₍⑅ᐢ..ᐢ₎")

    elif excedeu_limite:
        print("\nOperação falhou! O valor do saque excede o limite. ( ˘︹˘ )")

    elif excedeu_saques:
        print("\nOperação falhou! Número máximo de saques excedido. ᓚ₍ ^. .^₎")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n✧˖° Saque realizado com sucesso! ʕ•́ᴥ•̀ʔっ ✧˖°")

    else:
        print("\n✘ Operação falhou! O valor informado é inválido. ✘")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n.・✫・゜・。. EXTRATO .・✫・゜・。.")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰✰")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Já existe usuário com esse CPF! ( ｡ •̀ ᴖ •́ ｡)")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("⋅˚₊ ୨୧ ‧₊˚ ⋅ Usuário criado com sucesso! ⋅˚₊ ୨୧ ‧₊˚ ⋅")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso! ⸜(｡˃ ᵕ ˂ )⸝♡")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n╰┈➤ Usuário não encontrado, fluxo de criação de conta encerrado!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))



def main():
    LIMITE_SAQUE= 3
    AGENCIA = '0001'

    saldo = 0
    limite = 1000
    extrato = ''
    numero_saques= 0
    usuarios = []
    contas= []

    while True:
        opcao = menu()

        if opcao == "d" or opcao == "D":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s" or opcao == "S":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUE,
            )

        elif opcao == "e" or opcao == "E":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu" or opcao == "NU":
            criar_usuario(usuarios)

        elif opcao == "nc" or opcao == "NC":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc" or opcao == "LC":
            listar_contas(contas)

        elif opcao == "x" or opcao == "X":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()
