from abc import ABC, abstractmethod

class pontoFunc:
    def __init__(self, mes, ano, faltas, atrasos):
        self.__mes=mes
        self.__ano=ano
        self.__faltas=faltas
        self.__atrasos=atrasos
        
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
    def faltas(self):
        return self.__faltas
    
    @faltas.getter
    def faltas(self):
        return self.__faltas
    
    @property
    def atrasos(self):
        return self.__atrasos
    
    @atrasos.getter
    def atrasos(self):
        return self.__atrasos
        
    def lancaFaltas(self, faltas):
        self.__faltas+=faltas
      
    def lancaAtrasos(self, atrasos):
        self.__atrasos+=atrasos
        
class funcionario(ABC):
    def __init__(self, codigo, nome):
        self.__codigo=codigo
        self.__nome=nome
        self.__pontoMensalFunc=[]
        
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
        self.__pontoMensalFunc.append(pontoFunc(mes, ano, faltas, atrasos))
        
    def lancaFaltas(self, mes, ano, faltas):
        for ponto in self.__pontoMensalFunc:
            if ponto.mes == mes and ponto.ano == ano:
                ponto.lancaFaltas(faltas)
                
    def lancaAtrasos(self, mes, ano, atrasos):
        for ponto in self.__pontoMensalFunc:
            if ponto.mes == mes and ponto.ano == ano:
                ponto.lancaAtrasos(atrasos)

    def imprimeFolha(self, mes, ano):
        print("Código:", self.codigo)
        print("Nome :", self.nome)
        for ponto in self.__pontoMensalFunc:
            if ponto.mes == mes and ponto.ano == ano:
                print("Salario Liquido:", self.calculaSalario(mes, ano))
                print("Bônus:", self.calculaBonus(mes, ano))
    
    @abstractmethod
    def calculaSalario(mes, ano):
        pass
    
    @abstractmethod
    def calculaBonus(mes, ano):
        pass
    
class Professor(funcionario):
    def __init__(self, codigo, nome, titulacao, sHoras, nAulas):
        super().__init__(codigo, nome)
        self.__titulacao=titulacao
        self.__sHoras=sHoras
        self.__nAulas=nAulas
        
    @property
    def titulacao(self):
        return self.__titulacao
    
    @titulacao.getter
    def titulacao(self):
        return self.__titulacao
    
    @property
    def sHoras(self):
        return self.__sHoras
    
    @sHoras.getter
    def sHoras(self):
        return self.__sHoras
    
    @property
    def nAulas(self):
        return self.__nAulas
    
    @nAulas.getter
    def nAulas(self):
        return self.__nAulas
    
    def calculaSalario(self, mes, ano):
        for ponto in self.pontoMensalFunc:
            if ponto.mes == mes and ponto.ano == ano:
                salario= self.__sHoras * self.__nAulas - self.__sHoras * ponto.faltas
        return salario
    
    def calculaBonus(self, mes, ano):
        s=self.calculaSalario(mes, ano)
        for ponto in self.pontoMensalFunc:
            if ponto.mes == mes and ponto.ano == ano:
                if ponto.faltas==0 and ponto.atrasos==0:
                    bonus=0.1
                else:
                    bonus=0.1-(ponto.atrasos/100)
        return s*bonus
    
class TecAdmin(funcionario):
    def __init__(self, codigo, nome, funcao, salarioM):
        super().__init__(codigo, nome)
        self.__funcao=funcao
        self.__salarioM=salarioM
        
    @property
    def funcao(self):
        return self.__funcao
    
    @funcao.getter
    def funcao(self):
        return self.__funcao
    
    @property
    def salarioM(self):
        return self.__salarioM
    
    @salarioM.getter
    def salarioM(self):
        return self.__salarioM
    
    def calculaSalario(self, mes, ano):
        for ponto in self.pontoMensalFunc:
            if ponto.mes == mes and ponto.ano == ano:
                salario= self.salarioM - (self.salarioM/30) * ponto.faltas
        return salario
    
    def calculaBonus(self, mes, ano):
        s=self.calculaSalario(mes, ano)
        for ponto in self.pontoMensalFunc:
            if ponto.mes == mes and ponto.ano == ano:
                if ponto.faltas==0 and ponto.atrasos==0:
                    bonus=0.08
                else:
                    bonus=0.08-(ponto.atrasos/100)
        return s*bonus
    
         
if __name__ == "__main__":
    funcionarios = []
    prof = Professor(1, "Joao", "Doutor", 45.35, 32)
    prof.adicionaPonto(4, 2021, 0, 0)
    prof.lancaFaltas(4, 2021, 2)
    prof.lancaAtrasos(4, 2021, 3)
    funcionarios.append(prof)
    tec = TecAdmin(2, "Pedro", "Analista Contábil", 3600)
    tec.adicionaPonto(4, 2021, 0, 0)
    tec.lancaFaltas(4, 2021, 3)
    tec.lancaAtrasos(4, 2021, 4)
    funcionarios.append(tec)
    for func in funcionarios:
        func.imprimeFolha(4, 2021)
        print()