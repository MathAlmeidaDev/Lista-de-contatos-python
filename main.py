agenda = {}

#Pedir nome do contato
#Pedir telefone do contato
#Associar as variáveis nome e telefone
#Printar resultados
def adicionar():
    nome = input('Qual o nome do contato? ').strip().title()
    telefone = input('Qual o telefone? ').strip()
    agenda[nome] = telefone
    print('Contato adicionado com sucesso!')


#Mostrar lista de contatos
def exibir():
    if agenda:
        print('Lista de contatos:')
    else:
        print('Sem contatos adicionados!')
    for nome, telefone in agenda.items():
        print(f'Nome: {nome}')
        print(f'Telefone: {telefone}')
        print('-' * 30)


#Buscar nome do contato e verificar se o contato existe
#Atualizar o contato se desejar
def buscar():
    nome = input('Qual contato você deseja buscar? ').title().strip()
    if nome in agenda:
        print('-' * 30)
        print(f'Nome: {nome}')
        print(f'Telefone: {agenda[nome]}')
        print('-' * 30)
    else:
        print('Contato não encontrado!')
        print('-' * 30)
    finalizar()
    x = input('Deseja atualizar o contato? ')
    if x == '1':
        nome = input('Digite o nome atualizado: ').strip().title()
        agenda[nome] = input('Digite o telefone atualizado: ').strip()
        print('-' * 30)
        print('Nome e telefone atualizados:')
        print(f'Nome: {nome}')
        print(f'Telefone: {agenda[nome]}')
    if x == '2':
        print('Certo! Continuando o programa.')

# Verifica se o contato existe
# Se existir deleta o contato
def deletar():
    nome = input('Qual o contato que você deseja deletar? ').strip().title()
    if nome in agenda:
        del agenda[nome]
        print('-' * 30)
        print('Contato deletado com sucesso!')
        print('-' * 30)
    else:
        print('-' * 30)
        print('O contato não existe!')
        print('-' * 30)


def menu():
    print('1. Para adicionar o contato')
    print('2. Para exibir o contato')
    print('3. Para buscar ou atualizar o contato')
    print('4. Para deletar o contato.')
    print('5. Para sair da lista.')


def finalizar():
    print('1. Sim')
    print('2. Não')


def loop():
    while True:
        menu()
        x = input('Escolha uma opção: ')

        if x == '1':
            adicionar()
            finalizar()
            y = input('Deseja mais alguma coisa? ')
            if y == '1':
                continue
            if y == '2':
                print('Até a próxima!')
            break

        if x == '2':
            exibir()
            finalizar()
            y = input('Deseja mais alguma coisa? ')
            if y == '1':
                continue
            if y == '2':
                print('Até a próxima!')
            break

        if x == '3':
            buscar()
            finalizar()
            y = input('Deseja mais alguma coisa? ')
            if y == '1':
                continue
            if y == '2':
                print('Até a próxima!')
            break

        if x == '4':
            deletar()
            finalizar()
            y = input('Deseja mais alguma coisa? ')
            if y == '1':
                continue
            if y == '2':
                print('Até a próxima!')
            break

        if x == '5':
            print('Até a próxima!')
            break


loop()