from banco import *


while True:
	acao = input('''Oque pretende fazer?:
1 -> Criar conta.
2 -> Saldo.
3 -> Depósito.
4 -> Saque.
5 -> Mudar senha.
6 -> Emprestimo.\n''')
	if acao == '1':
		criaConta()
	elif acao == '2':
		IDask = int(input('Informe o ID da sua conta: '))
		print (usuarios[IDask])
	elif acao == '3':
		IDask = int(input('Informe o ID da sua conta: '))
		senha = getpass.getpass('Informe sua senha: ')
		deposito = float(input('Depósito: '))
		usuarios[IDask].deposito(senha, deposito)
