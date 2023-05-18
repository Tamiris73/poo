from abc import ABC, abstractmethod

class Dependente():
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    @property
    def nome(self):
        return self.__nome
        
    @property
    def idade(self):
        return self.__idade

class Trabalhador(ABC):
    def __init__(self, cpf, nome):
        self.__cpf = cpf
        self.__nome = nome

        self.__listaDependentes = []

    @property
    def cpf(self):
        return self.__cpf
        
    @property
    def nome(self):
        return self.__nome
        
    @property
    def listaDependentes(self):
        return self.__listaDependentes
        
    def insereDependente(self, nome, idade):
        self.__listaDependentes.append(Dependente(nome, idade))

    @abstractmethod
    def calculaPagto(mes):
        pass

    @abstractmethod
    def imprimeRecibo(mes, ano):
        pass

class Diaria():
    def __init__(self, dia, mes, ano, refeicao, atraso):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano
        self.__refeicao = refeicao
        self.__atraso = atraso

    @property
    def dia(self):
        return self.__dia
    
    @property
    def mes(self):
        return self.__mes
    
    @property
    def ano(self):
        return self.__ano
    
    @property
    def refeicao(self):
        return self.__refeicao
    
    @property
    def atraso(self):
        return self.__atraso
    
class Diarista(Trabalhador):
    def __init__(self, cpf, nome, valorDiaria):
        super().__init__(cpf, nome)
        self.__valorDiaria = valorDiaria
        self.__listaDiaria = []

    @property
    def valorDiaria(self):
        return self.__valorDiaria
    
    def adicionaDiaria(self, dia, mes, ano, refeicao, atraso):
        self.__listaDiaria.append(Diaria(dia, mes, ano, refeicao, atraso))
    
    def obtemValorAuxilio(self):
        auxilio=0
        for d in self.listaDependentes:
            if d.idade<6:
                auxilio+=100
        return auxilio     

    def calculaPagto(self, mes):
        pgto=0
        for d in self.__listaDiaria:
            if d.mes==mes:
                if d.atraso==0:
                    pgto+=self.__valorDiaria
                elif d.atraso<=30:
                    pgto+=0.9*self.__valorDiaria
                else:
                    pgto+=0
                if d.refeicao==True:
                    pgto-=10
        return self.obtemValorAuxilio()+pgto

    def imprimeRecibo(self, mes, ano):
        print("Nome: {}".format(self.nome))
        print("cpf: {}".format(self.cpf))
        print("Pagamento: {}".format(self.calculaPagto(mes)))
    
class Empreito():
    def __init__(self, mes, ano, descricao, valor, atrasoEntrega):
        self.__mes = mes
        self.__ano = ano
        self.__descricao = descricao
        self.__valor = valor
        self.__atrasoEntrega = atrasoEntrega

    @property
    def mes(self):
        return self.__mes
    
    @property
    def ano(self):
        return self.__ano
    
    @property
    def descricao(self):
        return self.__descricao
    
    @property
    def valor(self):
        return self.__valor
    
    @property
    def atrasoEntrega(self):
        return self.__atrasoEntrega
    
class Empreiteiro(Trabalhador):
    def __init__(self, cpf, nome):
        super().__init__(cpf, nome)

        self.__listaEmpreito = []

    def adicionaEmpreito(self, mes, ano, descricao, valor, atrasoEntrega):
        self.__listaEmpreito.append(Empreito(mes, ano, descricao, valor, atrasoEntrega))

    def calculaPagto(self, mes):
        pgto=0
        for d in self.__listaEmpreito:
            if d.mes==mes:
                if d.atrasoEntrega==0:
                    pgto+=d.valor
                else:
                    pgto+=0.8*d.valor
        return pgto

    def imprimeRecibo(self, mes, ano):
        print("Nome: {}".format(self.nome))
        print("cpf: {}".format(self.cpf))
        print("Pagamento: {}".format(self.calculaPagto(mes)))

if __name__ == "__main__":
    listaTrab = []
    d1 = Diarista("111222", "Joao Silva", 100)
    d1.insereDependente("Pedro Silva", 4)
    d1.insereDependente("Ana Silva", 2)
    d1.adicionaDiaria(10, 3, 2022, False, False)
    d1.adicionaDiaria(12, 4, 2022, False, True)
    d2 = Diarista("222333", "Jose Cruz", 120)
    d2.insereDependente("Paula Cruz", 3)
    d2.insereDependente("Mario Cruz", 10)
    d2.adicionaDiaria(5, 4, 2022, False, False)
    d2.adicionaDiaria(6, 4, 2022, True, False)
    d2.adicionaDiaria(7, 4, 2022, True, True)
    e1 = Empreiteiro("333444,", "Marcio Souza")
    e1.adicionaEmpreito(3, 2022, "Fundações", 6000, False)
    e1.adicionaEmpreito(4, 2022, "Construção muros", 4000, False)
    e1.adicionaEmpreito(4, 2022, "Instalação dos pisos", 7000, True)
    listaTrab.append(d1)
    listaTrab.append(d2)
    listaTrab.append(e1)
    for trab in listaTrab:
        trab.imprimeRecibo(4, 2022)