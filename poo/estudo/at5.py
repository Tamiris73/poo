from abc import ABC, abstractmethod

class venda:
    def __init__(self, cod, mes, ano, valor):
       self.__cod=cod
       self.__mes=mes
       self.__ano=ano
       self.__valor=valor
     
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
        
class vendedor(ABC):
    def __init__(self, pcodigo, pnome):
        self.__pcodigo=pcodigo
        self.__pnome=pnome
        self.__vendas=[]
    
    @property
    def pcodigo(self):
        return self.__pcodigo
    
    @pcodigo.getter
    def pnome(self):
        return self.__pcodigo

    @property
    def pnome(self):
        return self.__pnome
    
    @pnome.getter
    def pnome(self):
        return self.__pnome

    @property
    def vendas(self):
        return self.__vendas
    
    @vendas.getter
    def vendas(self):
        return self.__vendas
    
    def adicionaVenda(self, cod, mes, ano, valor):
        self.__vendas.append(venda(cod, mes, ano, valor))
    
    @abstractmethod
    def getDados():
        pass
    
    @abstractmethod
    def calculaRenda (mes, ano):
        pass
        
class Contratado(vendedor):
    def __init__(self, pcodigo, pnome, salario, carteira):
        super().__init__(pcodigo, pnome)
        self.__carteira=carteira
        self.__salario=salario
        self.__comissao = 0.01
        
    @property
    def carteira(self):
        return self.__carteira
        
    @property
    def salario(self):
        return self.__salario
    
    @property
    def comissao(self):
        return self.__comissao
        
    def getDados(self):
        print("\nVendedor contratado")
        print("Número:", self.carteira)
        print("Nome :", self.pnome)
    
    def calculaRenda(self, mes, ano):
        comi= sum([venda.valor * self.comissao for venda in self.vendas if venda.mes == mes and venda.ano == ano])
        return self.__salario+comi
        
class Comissionado(vendedor):
    def __init__(self, pcodigo, pnome, cpf, comissao):
        super().__init__(pcodigo, pnome)
        self.__cpf=cpf
        self.__comissao=comissao
        
    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.getter
    def cpf(self):
        return self.__cpf
        
    @property
    def comissao(self):
        return self.__comissao
    
    @comissao.getter
    def comissao(self):
        return self.__comissao
        
    def getDados(self):
        print("\nVendedor comissionado")
        print("Número:", self.cpf)
        print("Nome :", self.pnome)
    
    def calculaRenda(self, mes, ano):
        salario=sum([venda.valor * (self.comissao / 100) for venda in self.vendas if venda.mes == mes and venda.ano == ano])
        return salario
    
if __name__ == "__main__":
    funcContratado = Contratado(1001, 'João da Silva', 2000, 1234)
    funcContratado.adicionaVenda(100, 3, 2022, 200000)
    funcContratado.adicionaVenda(101, 3, 2022, 300000)
    funcContratado.adicionaVenda(102, 4, 2022, 600000)
    funcComissionado = Comissionado(1002, 'José Santos', 4321, 5)
    funcComissionado.adicionaVenda(200, 3, 2022, 200000)
    funcComissionado.adicionaVenda(201, 3, 2022, 400000)
    funcComissionado.adicionaVenda(202, 4, 2022, 500000)
    listaFunc = [funcContratado, funcComissionado]
    for func in listaFunc:
        print (func.getDados())
        print ("Renda no mês 3 de 2022: ")
        print (func.calculaRenda(3, 2022))