#Tamiris Oliveira - 2022006443

from abc import ABC, abstractmethod
import datetime as dt
from datetime import date

class Transacao:
    def __init__(self, data, valor, descricao):
        self.data = data
        self.valor = valor
        self.descricao = descricao

class Conta(ABC):
    def __init__(self, nome, nConta, saldo):
        self.__nome = nome
        self.__nConta = nConta
        self.__saldo = saldo
        self.__lTransacao = []
    @property
    def nome(self):
        return self.__nome
    
    @property
    def nConta(self):
        return self.__nConta
        
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo

    @saldo.getter
    def saldo(self):
        return self.__saldo
    
    @abstractmethod
    def imprimirExtrato(self):
        pass

    def depositar(self, valor):
        self.saldo += valor
        transacao = Transacao(date.today(), valor, 'Depositado. Valor: ')
        self.__lTransacao.append(transacao)
        print("Transação Aprovada.")
    
    def retirada(self, valor):
        if(self.saldo > valor):
            self.saldo -= valor
            print("Transação Aprovada.")
            transacao = Transacao(date.today(), valor, 'Debitado. Valor: ')
            self.__lTransacao.append(transacao)
        else:
            print("Transação Negada.")

class ContaCorrente(Conta):
    def __init__(self, nome, nConta, saldo):
        super().__init__(nome,nConta, saldo)
        self.__lTransacao = []
    
    def imprimirExtrato(self):
        print("\nConta Corrente")
        print("Número:", self.nConta)
        print("Nome :", self.nome)
        print("Saldo:", self.saldo)
        print("Transações:")
        for t in self.__lTransacao:
            print(t.data.strftime("%d/%m/%Y"), t.descricao, t.valor)

class ContaLimite(Conta):
    def __init__(self, nome, nConta, saldo, limite):
        super().__init__(nome,nConta, saldo)
        self.__lTransacao = []
        self.__limite = limite

    def retirada(self, valor):
        if(self.saldo - valor > -1 * (self.__limite)):
            self.saldo -= valor
            print("Transação Aprovada.")
            transacao = Transacao(date.today(), valor, 'Debitado. Valor: ')
            self.__lTransacao.append(transacao)
        else:
            print("Transação Negada.")

    def imprimirExtrato(self):
        print("\nConta Limite")
        print("Número da Conta:", self.nConta)
        print("Nome do Correntista:", self.nome)
        print("Saldo:", self.saldo)
        print("Transações:")
        for abb in self.__lTransacao:
            print(abb.data.strftime("%d/%m/%Y"), abb.descricao, abb.valor)

class ContaPoupança(Conta):
    def __init__(self, nome, nConta, saldo, dataAni):
        super().__init__(nome,nConta, saldo)
        self.__lTransacao = []
        self.__diaAniversario = dataAni

    @property
    def diaAniversario(self):
        return self.__diaAniversario
    
    def getAniversario(self):
        return self.__diaAniversario.strftime("%m/%d")

    
    def imprimirExtrato(self):
        print("\nConta Poupança")
        print("Número da Conta:", self.nConta)
        print("Nome do Correntista:", self.nome)
        print(f"Dia do Aniversário: ", self.getAniversario())
        print("Saldo:", self.saldo)
        print("Transações:")
        for abb in self.__lTransacao:
            print(abb.data.strftime("%d/%m/%Y"), abb.descricao, abb.valor)
        print("\n")

if __name__ == "__main__":
    conta1 = ContaPoupança("ana", 1, 100, date(2050, 7, 10))
    conta2 = ContaCorrente("maria", 2, 1000)
    conta3 = ContaLimite("Joao", 3, 70000, 4000)

    contas = [conta1, conta2, conta3]

    for conta in contas:
        conta.depositar(500000)
        conta.imprimirExtrato()
        conta.retirada(4)
        conta.imprimirExtrato()