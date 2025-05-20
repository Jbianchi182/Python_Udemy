nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome == '' or idade == '':
    print('Você deixou campos vazios')
if nome != '' and idade != '':
    print(f'Seu nome é: {nome}')
    print(f'Seu nome invertido é: {nome[::-1]}')
    print(f'Seu nome tem ou não espaços? {"Sim" if " " in nome else "Não"}')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é: {nome[0]}')
    print(f'A última letra do seu nome é: {nome[-1]}')



