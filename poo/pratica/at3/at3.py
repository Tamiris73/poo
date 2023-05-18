from abc import ABC, abstractmethod

class EmpDomestica(ABC):
    def __init__(self, nome, telefone):
        self.__nome = nome
        self.__telefone = telefone

    @property
    def nome(self):
        return self.__nome

    @property
    def telefone(self):
        return self.__telefone

    @abstractmethod
    def calculaSalario(self):
        pass

class Diarista(EmpDomestica):
    def __init__(self, nome, telefone, diasTrabalhados, valorPorDia):
        super().__init__(nome, telefone)
        self.__diasTrabalhados= diasTrabalhados
        self.__valorPorDia= valorPorDia

    @property
    def diasTrabalhados(self):
        return self.__diasTrabalhados

    @property
    def valorPorDia(self):
        return self.__valorPorDia
    

    def calculaSalario(self):
        return self.__diasTrabalhados * self.__valorPorDia

class Horista(EmpDomestica):
    def __init__(self, nome, telefone, horasTrabalhadas, valorHora):
        super().__init__(nome, telefone)
        self.__horasTrabalhadas = horasTrabalhadas
        self.__valorHora = valorHora


    @property
    def horasTrabalhadas(self):
        return self.__horasTrabalhadas

    @property
    def valorHora(self):
        return self.__valorHora
    

    def calculaSalario(self):
        return self.__horasTrabalhadas * self.valorHora
    
class Mensalista(EmpDomestica):
    def __init__(self, nome, telefone, valorMensal):
        super().__init__(nome, telefone)
        self.__valorMensal= valorMensal


    @property
    def valorMensal(self):
        return self.__valorMensal
    

    def calculaSalario(self):
        return self.__valorMensal
    

if __name__ == "__main__":
    emp1 = Horista('Maria', '32651890', 160, 12)
    emp2 = Diarista('Ana', '40028922', 20, 65)
    emp3 = Mensalista('Francisca', '70707070', 1200)
    emps = [emp1, emp2, emp3]
    for emp in emps:
        print ('Nome: {} - Salário: {}'.format(emp.nome, emp.calculaSalario()))
