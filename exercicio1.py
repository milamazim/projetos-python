LINHA = 50
usuarios = []

def criar_usuario():
    usuario = {
        "id": len(usuarios) + 1,
        "nome": input("Usuário: "),
        "email": input("E-mail: ")
    }
    usuarios.append(usuario)
    print("Usuário criado com sucesso!")
    print("-" * LINHA)


def listar_usuario():
    if not usuarios:
        print("Nenhum usuário cadastrado")
        print("-" * LINHA)
    else:
        for user in usuarios:
            print(f"ID: {user['id']}")
            print(f"Nome: {user['nome']}")
            print(f"Email: {user['email']}")
            print("-" * LINHA)


def atualizar_usuario():
    while True:
        try:
            user_id = int(input("Digite o ID do usuário: "))
            print("-" * LINHA)
            break
        except ValueError:
            print("Digite apenas números.")
            print("-" * LINHA)

    for user in usuarios:
        if user["id"] == user_id:
            user["nome"] = input("Novo nome: ")
            user["email"] = input("Novo email: ")
            print("Usuário atualizado!")
            print("-" * LINHA)
            return

    print("Usuário não encontrado")
    print("-" * LINHA)


def remover_usuario():
    while True:
        try:
            user_id = int(input("Digite o ID do usuário: "))
            print("-" * LINHA)
            break
        except ValueError:
            print("Digite apenas números.")
            print("-" * LINHA)

    for user in usuarios:
        if user["id"] == user_id:
            usuarios.remove(user)
            print("Usuário excluído!")
            print("-" * LINHA)
            return

    print("Usuário não encontrado")
    print("-" * LINHA)


def menu():
    while True:
        print('Digite o número da opção desejada:')
        print('-' * LINHA)
        print('(1) Criar usuário')
        print('(2) Listar usuário')
        print('(3) Atualizar usuário')
        print('(4) Remover usuário')
        print('(0) Sair')
        print('-' * LINHA)

        try:
            opcao = int(input('Opção: '))
            print("-" * LINHA)
        except ValueError:
            print("Digite apenas números.")
            print("-" * LINHA)
            continue

        match opcao:
            case 1:
                criar_usuario()
            case 2:
                listar_usuario()
            case 3:
                atualizar_usuario()
            case 4:
                remover_usuario()
            case 0:
                print('Programa finalizado')
                break
            case _:
                print('Opção inexistente')

menu()