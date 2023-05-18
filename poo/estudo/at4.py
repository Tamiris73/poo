from abc import ABC, abstractclassmethod
import datetime as dt
from datetime import date

class transacao:
    def __init__(self, data, valor, desc):
        self.data=data
        self.valor=valor
        self.desc=desc

class conta(ABC):
    def __init__(self, nmr, nome, saldo):
        self.__nmr=nmr
        self.__nome=nome
        self.__saldo=saldo
        self.__transacoes = []
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def nmr(self):
        return self.__nmr
        
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo

    @saldo.getter
    def saldo(self):
        return self.__saldo
    
    def deposito(self, valor):
        self.__saldo+=valor
        t=transacao(date.today(), valor, "deposito")
        self.__transacoes.append(t)
        
    def retirada(self, valor):
        if(self.saldo>=valor):
            self.__saldo-=valor
            t=transacao(date.today(), valor, "retirada")
            self.__transacoes.append(t)
       
    def extrato(self):
        print("\nConta Corrente")
        print("Número:", self.nmr)
        print("Nome :", self.nome)
        print("Saldo:", self.saldo)
        print("Transações:")
        for trans in self.__transacoes:
            print(trans.data.strftime("%d/%m/%Y"), trans.desc, trans.valor)
        
class poupanca(conta):
    def __init__(self, nmr, nome, saldo, ani):
        super().__init__(nmr, nome, saldo)
        self.__ani=ani
        self.__transacoes=[]
    
    @property
    def ani(self):
        return self.__ani
    
    def getAniversario(self):
        return self.__ani.strftime("%m/%d")
    
    def imprimirExtrato(self):
        print("\nConta Poupança")
        print("Número da Conta:", self.nmr)
        print("Nome do Correntista:", self.nome)
        print("Dia do Aniversário: ", self.getAniversario())
        print("Saldo:", self.saldo)
        print("Transações:")
        for abb in self.__transacoes:
            print(abb.data.strftime("%d/%m/%Y"), abb.descricao, abb.valor)
        print("\n")
   
class limite(conta):
    def __init__(self, nmr, nome, saldo, lim):
        super().__init__(nmr, nome, saldo)
        self.__lim=lim
        self.__transacoes=[]
    
    @property
    def lim(self):
        return self.__lim
    
    def retirada(self, valor):
        if(self.saldo + self.__lim > valor):
            self.saldo-=valor
            t=transacao(date.today(), valor, "retirada")
            self.__transacoes.append(t)
    
    def extrato(self):
        print("\nConta Limite")
        print("Número da Conta:", self.nmr)
        print("Nome do Correntista:", self.nome)
        print("Saldo:", self.saldo)
        print("Transações:")
        for abb in self.__transacoes:
            print(abb.data.strftime("%d/%m/%Y"), abb.desc, abb.valor)
            
            
if __name__ == "__main__":
    c1=poupanca(1, 'ana', 700, date(2003, 7, 10))
    c2=limite(2, 'maria', 0, 90000000000000)
    c3=conta(3, 'mariana', 31200)
    
    c1.deposito(100000000000000)
    c1.deposito(0.1)
    c1.retirada(200)
    
    c2.deposito(3.15)
    c2.retirada(3000000)
    c2.retirada(500)
    
    c3.retirada(100)
    c3.deposito(3900)
    c3.retirada(8.96)
    
    c=[]
    c=[c1, c2, c3]
    for cont in c:
        cont.extrato()
        
        