from abc import ABC, abstractmethod
class TipoSessao:
    def __init__(self, nome, duracao, preco):
        self.__nome=nome
        self.__duracao=duracao
        self.__preco=preco
        
    @property
    def nome(self):
        return self.__nome
    
    @nome.getter
    def nome(self):
        return self.__nome
    
    @property
    def duracao(self):
        return self.__duracao
    
    @duracao.getter
    def duracao(self):
        return self.__duracao
    
    @property
    def preco(self):
        return self.__preco
    
    @preco.getter
    def preco(self):
        return self.__preco
    
class Sessao:
    def __init__(self, dia, mes, tipo):
        self.__dia=dia
        self.__mes=mes
        self.__tipo=tipo
        
    @property
    def dia(self):
        return self.__dia
    
    @dia.getter
    def dia(self):
        return self.__dia
    
    @property
    def mes(self):
        return self.__mes
    
    @mes.getter
    def mes(self):
        return self.__mes
    
    @property
    def tipo(self):
        return self.__tipo
    
    @tipo.getter
    def tipo(self):
        return self.__tipo
    
class paciente(ABC):
    def __init__(self, nome, endereco):
        self.__nome=nome
        self.__endereco=endereco
        self.__sessoes=[]
        
    @property
    def nome(self):
        return self.__nome
    
    @nome.getter
    def nome(self):
        return self.__nome
    
    @property
    def endereco(self):
        return self.__endereco
    
    @endereco.getter
    def endereco(self):
        return self.__endereco
    
    @property
    def sessoes(self):
        return self.__sessoes
    
    @sessoes.getter
    def sessoes(self):
        return self.__sessoes
    
    def addSessao(self, sessao):
        self.sessoes.append(sessao)
        
    @abstractmethod
    def geraFichaPaciente(mes):
        pass
    
    @abstractmethod
    def calculaValorDevido(mes):
        pass
        
class Particular(paciente):
    def __init__(self, nome, endereco, cpf):
        super().__init__(nome, endereco)
        self.__cpf=cpf
       
    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.getter
    def cpf(self):
        return self.__cpf
        
    def geraFichaPaciente(self, mes):
                print("Nome :", self.nome)
                print("Endereco:", self.endereco)
                print("CPF:", self.cpf)
                print("Sessões realizadas:")
                for s in self.sessoes:
                    if s.mes == mes:
                        print("Data: {}/{} - Tipo de sessão: {}".format(s.dia, s.mes, s.tipo.nome))
    
    def calculaValorDevido(self, mes):
        v=0
        for s in self.sessoes:
            if s.mes == mes:
                v+=s.tipo.preco
        return v
    
class Convenio(paciente):
    def __init__(self, nome, endereco, nomeConv, nmrCartao):
        super().__init__(nome, endereco)
        self.__nomeConv=nomeConv
        self.__nmrCartao=nmrCartao
       
    @property
    def nomeConv(self):
        return self.__nomeConv
    
    @nomeConv.getter
    def nomeConv(self):
        return self.__nomeConv
    
    @property
    def nmrCartao(self):
        return self.__nmrCartao
    
    @nmrCartao.getter
    def nmrCartao(self):
        return self.__nmrCartao
        
    def geraFichaPaciente(self, mes):
                print("Nome :", self.nome)
                print("Endereco:", self.endereco)
                print("Nome do Convenio:", self.nomeConv)
                print("Numero do cartao:", self.nmrCartao)
                print("Sessões realizadas:")
                for s in self.sessoes:
                    if s.mes == mes:
                        print("Data: {}/{} - Tipo de sessão: {}".format(s.dia, s.mes, s.tipo.nome))
    
    def calculaValorDevido(self, mes):
        v=0
        for s in self.sessoes:
            if s.mes == mes:
                v+=s.tipo.preco*0.6
        return v
        
if __name__=="__main__":
    listaPac = []
    orto = TipoSessao('Ortopédica', 30, 50)
    resp = TipoSessao('Respiratória', 40, 60)
    pil = TipoSessao('Pilates', 50, 70)
    pac1 = Convenio('Pedro', 'Av BPS, 1303', 'Unimed', 123456)
    pac1.addSessao(Sessao(10, 9, resp))
    pac1.addSessao(Sessao(12, 9, resp))
    pac1.addSessao(Sessao(18, 9, pil))
    pac1.addSessao(Sessao(5, 10, resp))
    listaPac.append(pac1)
    pac2 = Particular('Maria', 'Av Cesario Alvin, 55', 654321)
    pac2.addSessao(Sessao(11, 9, orto))
    pac2.addSessao(Sessao(15, 9, orto))
    pac2.addSessao(Sessao(23, 9, pil))
    pac2.addSessao(Sessao(12, 10, orto))
    listaPac.append(pac2)
    pac1.geraFichaPaciente(10)
    print()
    pac2.geraFichaPaciente(9)
    print()
    faturamento = 0
    for pacientes in listaPac:
        faturamento += pacientes.calculaValorDevido(9)
    print('Faturamento do mês 9: {}'.format(faturamento))