import os

restaurantes = [{'nome':'praça', 'categoria':'Japones', 'ativo':False},
                {'nome':'Pizza', 'categoria':'Pizza', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Italiana', 'ativo':False}]


# Funções de Exibição da aplicação #

# Exibir Nome do Programa
def exibir_nome_do_programa():
    print('Delivery Py')

# Método para ser chamado sempre que for mudado a tela passando como parametro
# um subtitulo para a nova tela
def exibir_subtitulo(subtitulo):
    os.system('cls')
    linha ='*' * len(subtitulo)
    print(linha)
    print(f'{subtitulo}')
    print(f'{linha}\n')

#Exibi as opções disponíveis ao usuário
def exibir_opcoes():
    print('\n1. Cadastrar Restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')


# Funcionalidades da aplicação #
def cadastrar_novo_restaurante():
    exibir_subtitulo('CADASTRO DE RESTAURANTE')
    nome_do_restaurante = input('Digite o nome do restaurante: ')
    categoria_do_restaurante = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')

    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria': categoria_do_restaurante, 
                            'ativo':False}

    restaurantes.append(dados_do_restaurante)
    print(f'\nO Restaurante "{nome_do_restaurante}" foi cadastrado com sucesso\n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    espacamento = 30 #Espaço dos caracteres na listagem

    exibir_subtitulo('LISTA DE RESTAURANTES CADASTRADOS')

    print (f'{'Nome do Restaurante'.ljust(espacamento+2)} | {'Categoria'.ljust(espacamento)} | Status\n')

    for indice in restaurantes:
        nome_restaurante = indice['nome']
        categoria_restaurante = indice['categoria']
        ativo_restaurante = 'ativado' if indice['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(espacamento)} | {categoria_restaurante.ljust(espacamento)} | {ativo_restaurante} ')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo('ALTERNAR STATUS DE UM RESTAURANTE')
    nome_restaurante = input('Digite o nome do Restaurante para alternar estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante ['ativo'] = not restaurante['ativo']
            mensagem = f'O Restaurante {nome_restaurante} foi ATIVADO com sucesso' if restaurante ['ativo'] else f'O Restaurante {nome_restaurante} foi DESATIVADO com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O Restaurante não foi encontrado')

    voltar_ao_menu_principal()

def finalizar_app():
    os.system('cls')
    print('App Finalizado\n')


# Método para tratar a escolha do usuário #
def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if   opcao_escolhida == 1:
                cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
                listar_restaurantes()
        elif opcao_escolhida == 3:
                alternar_estado_restaurante()
        elif opcao_escolhida == 4:
                finalizar_app()
        else:
                opcao_invalida()
                print(opcao_escolhida)   
    except:
        opcao_invalida()

# Método que pode ser chamado em um except #
def opcao_invalida():
    os.system('cls')
    print('Opção Inválida\n')
    voltar_ao_menu_principal()

# Método para ser chamado sempre que o usuário precisar voltar ao menu principal
def voltar_ao_menu_principal():
    input('\nAperte a tecla enter para voltar ao menu principal\n')
    main()  


# main()
def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()