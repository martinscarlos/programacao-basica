from datetime import date

ano = int(input('\nDigite um ano (0 para ano atual): '))

if ano == 0: ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
	print(f'O ano de {ano} é BISSEXTO')
else:
	print(f'O ano de {ano} NÃO é BISSEXTO')
print('\n')
