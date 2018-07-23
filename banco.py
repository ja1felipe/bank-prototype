import getpass, random
#Guarda informações do banco, como o total de dinheiro, se pode emprestar dinheiro e o valor da reserva.
class Banco:
	__total = 10000
	reserva = 0.1
	__reservaReal = __total * reserva
	
	def __init__(self):
		self.contas = Contas()
	
	def PodeEmprestar(valor):
		Banco.__total -= valor
		if Banco.__total >= Banco.__reservaReal:
			return True
		else:
			return False
	
	def MudaTotal(valor):
		Banco.__total += valor
	
#Cria nova conta, faz depósito, saque, confere se o banco pode fazer emprestimo de determinado valor e altera senha.	
class Conta(Banco):
	def __init__(self, ID, saldo, senha, nome):
		self.ID = ID
		self.__saldo = saldo
		self.__senha = senha
		self.__nome = nome
		
	def __str__(self):
		return 'Bem vindo(a) {}, seu saldo atual é de, R$ {:.2f}.\n'.format(self.__nome, self.__saldo)
	
	def deposito(self, senha, valor):
		if senha == self.__senha:
			Banco.MudaTotal(valor)
			self.__saldo += valor
			
	def saque(self, senha, valor):
		if senha == __senha:
			Banco.MudaTotal(-int(valor))
			self.__saldo -= valor
			
	def podeReceberEmprestimo(self, valor):
		if Banco.PodeEmprestar(valor):
			return print('Sim\n')
		else:
			return print('Não\n')
		
	def mudaSenha(self, senha, nova_senha):
		if senha == self.__senha and nova_senha != senha:
			self.__senha = nova_senha
			return print('Senha mudada com sucesso\n')
		elif senha != self.__senha:
			return print('Senha atual errada\n')
		elif nova_senha == senha:
			return print('A nova senha deve ser diferente da antiga\n')
		
		
#Coloca contas em ordem por ID
class Contas(list):
	def sort(self):
		copia = self.copy()
		tam = len(self)
		self.clear()
		
		while len(self) < tam:
			min_id = copia[0]
			for conta in copia:
				if conta.ID < min_id.ID:
					min_id = conta
			self.append(min_id)
			copia.remove(min_id)
		return self
		
usuarios = {21: 'Vai se uder'}
Ids = []
def criaConta():
	nome = input('Informe seu nome completo: ')
	dinheiro = float(input('Quantidade do primeiro depósito: '))
	senha = getpass.getpass('Senha: ')
	Id = random.randint(0, 500)
	while True:
		if Id in Ids:
			Id = random.randint(0,500)
		else:
			break
	Ids.append(Id)
	print('Conta criada, seu ID é {}, lembre-se sempre dele, será usado para transações futuras.\n'.format(Id))
	usuarios[Id] = Conta(Id, dinheiro, senha, nome)

	
