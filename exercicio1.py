usuarios = []

def criar_usuario():    
    usuarios.append(input('Digite o usuário a ser criado: '))        

def listar_usuario():
    print('Usuarios cadastrados: ')    
    for x in usuarios:
        print(x)

def atualizar_usuario():
    usuario = input('Atualizar qual usuário? ')    
    
    for x in usuarios:
        if (x == usuario):
            update = input('Informação a ser atualizada: ')
            indice = usuarios.index(x)
            usuarios[indice] = update   

def remover_usuario():
    usuario = input('Informe o usuário a ser removido: ')        
    usuarios.remove(usuario)

def menu():
    print('Digite o número da opção desejada: \n' +
        '----------------------------------------------- \n' + 
        '(1) Criar usuário \n' +
        '(2) Listar usuário \n' +
        '(3) Atualizar usuário \n' +
        '(4) Remover usuário \n' +
        '(0) Sair\n\n')

    opcao = int(input('Opção: '))
   
    match opcao:
        case 1:
            criar_usuario()
            menu()
        case 2:            
            listar_usuario()
            menu()
        case 3:
            atualizar_usuario()
            menu()
        case 4:
            remover_usuario()
            menu()
        case 0:
            print('Programa finalizado')
        case _: # default
            print('Opção inexistente')
            menu()            

menu()