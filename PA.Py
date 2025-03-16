pt = int(input('Qual o primeiro termo da sua PA? '))
razao = int(input('Qual a razão da sua PA? '))
resposta = pt + (10 - 1) * razao

for c in range (pt, resposta + razao, razao):
    print('{}'.format(c),end = ' -> ')
print('ACABOU')
