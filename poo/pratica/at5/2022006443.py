#Tamiris Oliveira - 20226443
from abc import ABC, abstractmethod

class Vendedor(ABC):
    def __init__ (self, codigo, nome):
        self.__codigo = codigo 
        self.__nome = nome       
        self.__vendas = []
    
    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.getter
    def defNome(self):
        return self.__nome

    @property
    def nome(self):
        return self.__nome
    
    @nome.getter
    def defNome(self):
        return self.__nome

    @property
    def vendas(self):
        return self.__vendas
    
    @vendas.getter
    def vendas(self):
        return self.__vendas
    
    def adicionaVenda(self, cod, mes, ano, valor):
        venda = Venda(cod, mes, ano, valor)
        self.__vendas.append(venda)
    
    @abstractmethod
    def getDados ():
        pass
    
    @abstractmethod
    def calculaRenda (mes, ano):
        pass
    
class Venda:
    def __init__(self, cod, mes, ano, valor):
        self.__cod = cod
        self.__mes = mes       
        self.__ano= ano
        self.__valor = valor

    @property
    def cod(self):
        return self.__cod
    
    @cod.getter
    def cod(self):
        return self.__cod
    
    @property
    def mes(self):
        return self.__mes
    
    @mes.getter
    def mes(self):
        return self.__mes
    
    @property
    def ano(self):
        return self.__ano
    
    @ano.getter
    def ano(self):
        return self.__ano

    @property
    def valor(self):
        return self.__valor
    
    @valor.getter
    def valor(self):
        return self.__valor

class Contratado(Vendedor):
    def __init__ (self, codigo, nome, salarioFixo, nCarteira):
        super().__init__(codigo, nome)
        self.__nCarteira = nCarteira
        self.__salarioFixo = salarioFixo
        self.__comissao = 0.01
    
    @property
    def nCarteira(self):
        return self.__nCarteira
    
    @nCarteira.getter
    def nCarteira(self):
        return self.__nCarteira
    
    @property
    def salarioFixo(self):
        return self.__salarioFixo
    
    @salarioFixo.getter
    def salarioFixo(self):
        return self.__salarioFixo
    
    @property
    def comissao(self):
        return self.__comissao
    
    @comissao.getter
    def comissao(self):
        return self.__comissao
    
    def calculaRenda(self, mes, ano):
        valor_comissao = sum([venda.valor * self.comissao for venda in self.vendas if venda.mes == mes and venda.ano == ano])
        return self.salarioFixo + valor_comissao
    
    def getDados(self):
        return "Nome: " + self.nome + " - nCarteira " + str(self.__nCarteira)
    
class Comissionado(Vendedor):
    def __init__ (self, codigo, nome, CPF, comissao):
        super().__init__(codigo, nome)
        self.__CPF = CPF
        self.__comissao = comissao
    
    @property
    def CPF(self):
        return self.__CPF
    
    @CPF.getter
    def CPF(self):
        return self.__CPF
        
    @property
    def comissao(self):
        return self.__comissao
    
    @comissao.getter
    def comissao(self):
        return self.__comissao
    
    def calculaRenda(self, mes, ano):
        valor_comissao = sum([venda.valor * self.comissao / 1 for venda in self.vendas if venda.mes == mes and venda.ano == ano])
        return valor_comissao
    
    def getDados(self):
        return "Nome: " + self.nome + " - Nro Cpf: " + str(self.__CPF)

if __name__ == "__main__":
    funcContratado = Contratado(1001, 'Ana', 2000, 1234)
    funcContratado.adicionaVenda(1, 3, 2022, 20)
    funcContratado.adicionaVenda(101, 3, 2022, 30)
    funcContratado.adicionaVenda(102, 4, 2022, 60)
    funcComissionado = Comissionado(12, 'Maria', 4321, 5)
    funcComissionado.adicionaVenda(2, 3, 2022, 20)
    funcComissionado.adicionaVenda(201, 3, 2022, 40)
    funcComissionado.adicionaVenda(202, 4, 2022, 50)
    listaFunc = [funcContratado, funcComissionado]
    for func in listaFunc:
        print (func.getDados())
        print ("Renda no mês 1 de 2022: ")
        print (func.calculaRenda(3, 2022))