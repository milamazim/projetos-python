usuarios = []

def criar_usuario():
    registro = []    
    registro.append(input('Usuário: '))
    registro.append(input('E-mail: '))
    usuarios.append(registro)
    print('-----------------------------------------------')

def listar_usuario():
    print('Usuarios cadastrados: ')    
    for x in usuarios:
        print(f'ID: {usuarios.index(x)}')
        print(f'Nome: {x[0]}')
        print(f'E-mail: {x[1]}')
        print('-----------------------------------------------')

def atualizar_usuario():
    usuario = input('Atualizar nome de qual usuário? ')    
    
    for x in usuarios:        
        if (x[0] == usuario):
            update = input('Atualizar nome: ')
            indice = usuarios.index(x)
            usuarios[indice][0] = update   
        
def remover_usuario():
    usuario = input('Informe o usuário a ser removido: ')

    for x in usuarios:        
        if (x[0] == usuario):            
            indice = usuarios.index(x)
            usuarios.remove(usuarios[indice])            
  
def menu():
    print('Digite o número da opção desejada: \n' +
        '----------------------------------------------- \n' + 
        '(1) Criar usuário \n' +
        '(2) Listar usuário \n' +
        '(3) Atualizar usuário \n' +
        '(4) Remover usuário \n' +
        '(0) Sair\n' + 
        '-----------------------------------------------')

    opcao = int(input('Opção: '))
    print('-----------------------------------------------')
   
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