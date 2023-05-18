from abc import ABC, abstractclassmethod

class emp(ABC):
    def __init__(self, nome, tel):
        self.__nome=nome
        self.__tel=tel
        
    @property
    def nome(self):
        return self.__nome
    
    @property
    def tel(self):
        return self.__tel
    
    @abstractclassmethod
    def sala(self):
        pass
    
    
class h(emp):
    def __init__(self, nome, tel, horas, valor):
        super().__init__(nome, tel)
        self.__horas=horas
        self.__valor=valor
        
    @property
    def horas(self):
        return self.__horas
    
    @property
    def valor(self):
        return self.__valor
    
    def sala(self):
        s=self.__horas*self.__valor
        return s
    
    
class d(emp):
    def __init__(self, nome, tel, dias, valor):
        super().__init__(nome, tel)
        self.__dias=dias
        self.__valor=valor
        
    @property
    def dias(self):
        return self.__dias
    
    @property
    def valor(self):
        return self.__valor
    
    def sala(self):
        s=self.__dias*self.__valor
        return s
    
    
class m(emp):
    def __init__(self, nome, tel, valor):
        super().__init__(nome, tel)
        self.__valor=valor
        
    @property
    def valor(self):
        return self.__valor
    
    def sala(self):
        s=self.__valor
        return s
    
    
if __name__ == "__main__":
    emph=h('ana', 999999999, 160, 12)
    empd=d('maria', 999999998, 20, 65)
    empm=m('mariana', 999999997, 1200)
    
    emp=[]
    emp=[emph, empd, empm]
    
    for empregadas in emp:
        s=empregadas.sala()
        print("nome: ", empregadas.nome)
        print("telefone: ", empregadas.tel)
        print("salario: ", s)
        
    s1=emph.sala()
    s2=empd.sala()
    s3=empm.sala()
    if(s1<s2 and s1<s2):
        print("contrate a horista")
    elif(s2<s1 and s2<s3):
        print("contrate a diarista")
    else:
        print("contrate a mensalista")
        