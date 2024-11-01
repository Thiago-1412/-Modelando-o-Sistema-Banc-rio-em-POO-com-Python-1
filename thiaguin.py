class Cliente:
    def __init__(self, nome, cpf, endereco=None):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.conta = None  # Associação com a conta
 
    def __str__(self):
        return f"Cliente: {self.nome}, CPF: {self.cpf}"
 
class Conta:
    def __init__(self, numero, saldo_inicial=0.0, limite_saque_diario=500.0):
        self.numero = numero
        self.saldo = saldo_inicial
        self.limite_saque_diario = limite_saque_diario
        self.extrato = []
 
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: + R${valor:.2f}")
            print("Depósito realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")
 
    def sacar(self, valor):
        if valor <= 0:
            print("Valor inválido para saque.")
        elif valor > self.saldo:
            print("Saldo insuficiente.")
        elif valor > self.limite_saque_diario:
            print(f"Limite de saque diário excedido. Limite atual: R${self.limite_saque_diario:.2f}")
        else:
            self.saldo -= valor
            self.extrato.append(f"Saque: - R${valor:.2f}")
            print("Saque realizado com sucesso.")
 
    def exibir_extrato(self):
        print("\nExtrato Bancário:")
        if not self.extrato:
            print("Nenhuma movimentação.")
        else:
            for transacao in self.extrato:
                print(transacao)
        print(f"\nSaldo atual: R${self.saldo:.2f}\n")
 
    def __str__(self):
        return f"Conta {self.numero}, Saldo: R${self.saldo:.2f}"
 
class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.clientes = []
        self.contas = []
 
    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)
        print(f"Cliente {cliente.nome} adicionado ao banco.")
 
    def abrir_conta(self, cliente, saldo_inicial=0.0):
        numero_conta = str(len(self.contas) + 1).zfill(6)  # Número da conta formatado com 6 dígitos
        conta = Conta(numero_conta, saldo_inicial)
        self.contas.append(conta)
        cliente.conta = conta
        print(f"Conta {numero_conta} aberta para o cliente {cliente.nome}.")
 
    def buscar_cliente_por_cpf(self, cpf):
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                return cliente
        return None
 
    def __str__(self):
        return f"Banco: {self.nome}, Clientes: {len(self.clientes)}, Contas: {len(self.contas)}"
 
# Exemplo de uso
banco = Banco("Banco Central")
 
# Criação de clientes
cliente1 = Cliente("Thiago Rocha", "12345678900", "Rua Principal, 123")
cliente2 = Cliente("Ana Silva", "98765432100", "Avenida Secundária, 456")
 
# Adição de clientes ao banco
banco.adicionar_cliente(cliente1)
banco.adicionar_cliente(cliente2)
 
# Abertura de contas para clientes
banco.abrir_conta(cliente1, saldo_inicial=1000.0)
banco.abrir_conta(cliente2, saldo_inicial=500.0)
 
# Operações na conta de um cliente
cliente1.conta.depositar(200)
cliente1.conta.sacar(150)
cliente1.conta.exibir_extrato()
 
print(banco)