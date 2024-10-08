nome = []
senha = []
tentativa = 0
cont = 1
while True:
    print("1. Cadastro")
    print("2. Mostrar")
    print("3. Login")
    print("4. Sair")
    menu = int(input("Selecione uma das opções: "))
    while menu < 1 or menu > 4:
        menu = int(input("Opção inválida.\nSelecione uma opção de 1 a 4: "))

    match menu:
        case 1:
            nomeUsuario = input("Nome do usuário: ")
            senhaUsuario = int(input("Senha do usuário: "))
            nome.append(nomeUsuario)
            senha.append(senhaUsuario)
            print("- - - - -")
            print("Usuário cadastrado")
            print("- - - - -")


        case 2:
            if len(nome) == 0:
                print("x x x x x")
                print("Nenhum usuário encontrado")
                print("x x x x x")

            else:
                for i in range(len(nome)):
                    print("- - - - -")
                    print(f"Usuário: {nome[i]}\nSenha: {senha[i]}")
                    print("- - - - -")

        case 3:
            nomeUsuario = input("Nome do usuário: ")
            senhaUsuario = int(input("Senha do usuário: "))
            if nomeUsuario in nome:
                index = nome.index(nomeUsuario)
                if senha[index] == senhaUsuario:
                    print("- - - - -")
                    print("Login efetuado com sucesso!")
                    print("- - - - -")

                    tentativa = 0
                else:
                    tentativa += 1
                    print("x x x x x")
                    print(f"Senha incorreta. Tentativa {tentativa} de 3.")
                    print("x x x x x")

            else:
                print("x x x x x")
                print("Usuário não possui o cadastro")
                print("x x x x x")

            if tentativa == 3:
                print("x x x x x")
                print("Conta bloqueada após 3 tentativas erradas.")
                print("x x x x x")
                break
        case 4:
            print("Saindo...")
            break
