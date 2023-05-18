#Tamiris Oliveira - 2022006443

from abc import ABC, abstractmethod

class funcionario(ABC):
    def __init__(self, codigo, nome):
        self.__codigo = codigo
        self.__nome = nome
        self.__pontoMensalFunc = []
    
    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.getter
    def codigo(self):
        return self.__codigo
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.getter
    def nome(self):
        return self.__nome
    
    @property
    def pontoMensalFunc(self):
        return self.__pontoMensalFunc
    
    @pontoMensalFunc.getter
    def pontoMensalFunc(self):
        return self.__pontoMensalFunc


    def adicionaPonto(self, mes, ano, faltas, atrasos):
        self.__pontoMensalFunc.append(PontoFunc(mes, ano, faltas, atrasos))

    def lancaFaltas(self, mes, ano, faltas):
        for ponto in self.__pontoMensalFunc:
            if(ano == ponto.ano and mes == ponto.mes):
                ponto.lancaFaltas(faltas)

    def lancaAtrasos(self, mes, ano, atrasos):
        for ponto in self.__pontoMensalFunc:
            if(ano == ponto.ano and mes == ponto.mes):
                ponto.lancaAtrasos(atrasos)

    def imprimeFolha(self, mes, ano):
        salario = float(self.calculaSalario(mes, ano))
        bonus = self.calculaBonus(mes, ano)
        print("Codigo: {}".format(self.__codigo))
        print("Nome: {}".format(self.__nome))
        print("Salario Liquido: {:.2f}".format(salario))
        print("Bonus: {:.2f}".format(bonus))

    @abstractmethod
    def calculaSalario(mes, ano):
        pass

    @abstractmethod
    def calculaBonus(mes, ano):
        pass
 
class PontoFunc():
    def __init__(self, mes, ano, nroFaltas, nroAtrasos):
        self.__mes = mes
        self.__ano = ano
        self.__nroFaltas = nroFaltas
        self.__nroAtrasos = nroAtrasos

    @property
    def mes(self):
        return self.__mes
    
    @mes.getter
    def getMes(self):
        return self.__mes
    
    @property
    def ano(self):
        return self.__ano
    
    @ano.getter
    def getAno(self):
        return self.__ano
    
    @property
    def nroFaltas(self):
        return self.__nroFaltas
    
    @nroFaltas.getter
    def getNroFaltas(self):
        return self.__nroFaltas
    
    @property
    def nroAtrasos(self):
        return self.__nroAtrasos
    
    @nroAtrasos.getter
    def getNroAtrasos(self):
        return self.__nroAtrasos

    def lancaFaltas(self, nrofaltas):
        self.__nroFaltas = self.__nroFaltas + nrofaltas

    def lancaAtrasos(self, nroAtrasos):
        self.__nroAtrasos = self.__nroAtrasos + nroAtrasos       

class Professor(funcionario):
    def __init__(self, codigo, nome, titulacao, salarioHora, nroAulas):
        super().__init__(codigo, nome)
        self.__titulacao = titulacao
        self.__salarioHora = salarioHora
        self.__nroAulas = nroAulas

    @property
    def titulacao(self):
        return self.__titulacao
    
    @titulacao.getter
    def titulacao(self):
        return self.__titulacao
    
    @property
    def salarioHora(self):
        return self.__salarioHora
    
    @salarioHora.getter
    def salarioHora(self):
        return self.__salarioHora
    
    @property
    def nroAulas(self):
        return self.__nroAulas
    
    @nroAulas.getter
    def nroAulas(self):
        return self.__nroAulas
    
    def calculaSalario(self, mes, ano):
        for ponto in self.pontoMensalFunc:
            if(ano == ponto.ano and mes == ponto.mes):
                salarioprof = self.__salarioHora * self.__nroAulas - self.__salarioHora * ponto.nroFaltas
        return salarioprof        
        
    
    def calculaBonus(self, mes, ano):
        bonus = 0.1
        for ponto in self.pontoMensalFunc:
            if(ano == ponto.ano and mes == ponto.mes):
                bonus = bonus - 0.01 * ponto.nroAtrasos
                salario = self.calculaSalario(mes, ano)
        return salario * bonus
        
class tecAdmin(funcionario):
    def __init__(self, codigo, nome, funcao, salarioMensal):
        super().__init__(codigo, nome)
        self.__funcao = funcao
        self.__salarioMensal = salarioMensal

    @property
    def funcao(self):
        return self.__funcao
    
    @funcao.getter
    def funcao(self):
        return self.__funcao
    
    @property
    def salarioMensal(self):
        return self.__salarioMensal
    
    @salarioMensal.getter
    def salarioMensal(self):
        return self.__salarioMensal
    
    
    def calculaSalario(self, mes, ano):
        for ponto in self.pontoMensalFunc:
            if(ano == ponto.ano and mes == ponto.mes):
                salariotec = self.__salarioMensal - ((self.__salarioMensal/30) * ponto.nroFaltas)
                return salariotec
            
    def calculaBonus(self, mes, ano):
        bonus = 0.08
        for ponto in self.pontoMensalFunc:
            if(ano == ponto.ano and mes == ponto.mes):
                bonus = bonus - 0.01 * ponto.nroAtrasos
                salario = self.calculaSalario(mes, ano)
        return salario * bonus


if __name__ == "__main__":
    funcionarios = []
    prof = Professor(1, "Joao", "Doutor", 45.35, 32)
    prof.adicionaPonto(4, 2021, 0, 0)
    prof.lancaFaltas(4, 2021, 2)
    prof.lancaAtrasos(4, 2021, 3)
    funcionarios.append(prof)
    tec = tecAdmin(2, "Pedro", "Analista Contábil", 3600)
    tec.adicionaPonto(4, 2021, 0, 0)
    tec.lancaFaltas(4, 2021, 3)
    tec.lancaAtrasos(4, 2021, 4)
    funcionarios.append(tec)
    for func in funcionarios:
        func.imprimeFolha(4, 2021)
        print()
