import os

restaurantes = [{'nome':'Di Lidia', 'categoria':'Pizzaria', 'ativo': False},
                {'nome': 'Burger Show' , 'categoria': 'Fast Food', 'ativo': True},
                {'nome': 'Umai Sushi' , 'categoria': 'Japonesa', 'ativo': False}]


def exibir_nome_do_programa():
    '''Essa função exibe o nome do programa.'''
    print('''
__________                _____        __________        _____         
___  ____/______ ___________  /_       ___  ____/______ ___  /_________
__  /_    _  __ `/__  ___/_  __/       __  __/   _  __ `/_  __/__  ___/
_  __/    / /_/ / _(__  ) / /_         _  /___   / /_/ / / /_  _(__  ) 
/_/       \__,_/  /____/  \__/         /_____/   \__,_/  \__/  /____/  
                                                                      
      ''')

def exibir_opcoes():
    '''Essa função exibe exibe as opções para o usuário.'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado de um restaurante')
    print('4. Sair')

def finalizar_app():
    '''Essa função finaliza a execução.'''
    exibir_subtitulo('Finalizando app...')

def exibir_subtitulo(texto):
    '''Essa função mostra o subtitulo da opção escolhida.'''
    os.system('cls')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def voltar_ao_menu_principal():
    '''Essa função volta ao menu de escolha. (principal)'''
    input('\nDigite qualquer tecla para voltar ao menu principal: ')
    main()

def opcao_invalida():
    '''Essa função exibe o alerta de que a opção escolhida é inválida'''
    print('''Opção inválida!
          ''')
    voltar_ao_menu_principal()

def casdastrar_novo_restaurante():
    '''Essa função cadastra um novo restaurante.'''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Nome restaurante: ')
    categoria = input(f'Categoria do {nome_do_restaurante}: ')    
    dados_do_restaurante = {'nome':nome_do_restaurante, 
    'categoria': categoria, 
    'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'''Restaurante {nome_do_restaurante} foi cadastrado com sucesso!
          ''')
    voltar_ao_menu_principal()
    
def listar_restaurantes():
    '''Essa função exibe a lista de restaurantes.'''
    exibir_subtitulo('Lista de restaurantes:')

    print(f'{'NOME DO RESTAURANTE'.ljust(22)} | {'CATEGORIA'.ljust(20)} | {'ESTADO'}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    '''Essa função alterna o status do restaurante (ativado, desativado).'''
    exibir_subtitulo('Alternando estado restaurante')
    nome_restaurante = input('Nome do restaurante para alternar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = (
                f'O restaurante {nome_restaurante} foi ativado com sucesso!' 
                if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
            )
            print(mensagem)
            break

    if not restaurante_encontrado:
        print('Restaurante não encontrado!')

    voltar_ao_menu_principal()


def escolher_opcao():
    '''Essa função pega o número digitado e direcionada para a função desejadas'''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f'Voce escolheu a opção {opcao_escolhida}')
        if opcao_escolhida == 1:
            casdastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()
    
def main():
    '''Essa função é a responsável para criar o menu principal.'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()