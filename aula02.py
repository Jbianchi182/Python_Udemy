nome = 'Joao'
sobrenome = 'Bianchi'
ano_nasc = 1993
idade = 2024 - ano_nasc
maior_idade = idade > 17
altura = 1.79
peso = 60
imc = peso / altura ** 2

linha_1 = f'{nome} tem {altura:.2f} de altura.'
linha_2 = f'pesa {peso}kg, e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

