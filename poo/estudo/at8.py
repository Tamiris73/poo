#Tamiris Oliveira - 2022006443

from abc import ABC, abstractmethod

class titulacaoInferior(Exception):
    pass

class idadeProf(Exception):
    pass

class cursoInvalido(Exception):
    pass

class idadeAluno(Exception):
    pass

class cpfDuplicado(Exception):
    pass

class pessoa(ABC):
    def __init__(self, nome, cpf, endereco, idade):
        self.__nome = nome
        self.__cpf= cpf
        self.__endereco= endereco
        self.__idade= idade
        

    @property
    def nome(self):
        return self.__nome

    @property
    def endereco(self):
        return self.__endereco

    @property
    def idade(self):
        return self.__idade
    
    @property
    def cpf(self):
        return self.__cpf
   
    def printDescricao(self):
        pass

class professor(pessoa):
    def __init__(self, nome, cpf, endereco, idade, titulacao):
        super().__init__(nome, cpf, endereco, idade)
        self.__titulacao = titulacao

    @property
    def titulacao(self):
        return self.__titulacao

    def printDescricao(self):
        print("Nome: {}".format(self.nome))
        print("cpf: {}".format(self.cpf))
        print("Endereço: {}".format(self.endereco))
        print("Idade: {}".format(self.idade))
        print("Titulação: {}".format(self.titulacao))
        return 0
    
class aluno(pessoa):
    def __init__(self, nome, cpf, endereco, idade, curso):
        super().__init__(nome, cpf, endereco, idade)
        self.__curso= curso

    @property
    def curso(self):
        return self.__curso
    
    def printDescricao(self):
        print("Nome: {}".format(self.nome))
        print("cpf: {}".format(self.cpf))
        print("Endereço: {}".format(self.endereco))
        print("Idade: {}".format(self.idade))
        print("Curso: {}".format(self.curso))
        return 0
    
if __name__ == "__main__":

    p1=professor("paulo", "11111111-11", "bps", 41, "mestre")
    p2=professor("ana", "111111111-12", "bps", 28, "doutor")
    p3=professor("joao", "111111111-12", "bps", 32, "doutor")
    p4=professor("maria", "111111111-13", "bps", 38, "doutor")
    
    listaExemploProf = [p1, p2, p3, p4]

    a1=aluno("paul", "111111111-14", "bps", 14, "CCO")
    a2=aluno("ann", "111111111-15", "bps", 18, "EMA")
    a3=aluno("john", "111111111-11", "bps", 21, "SIN")
    a4=aluno("mary", "111111111-16", "bps", 20, "CCO")
    listaExemploAluno = [a1, a2, a3, a4]
    
    cadastro = [p1, p2, p3, p4, a1, a2, a3, a4]
    
    for pessoas in listaExemploProf:
        try:
            if pessoas.idade < 30:
                raise idadeAluno

            if pessoas.titulacao != "doutor":
                raise titulacaoInferior

            for primeiro, segundo in zip(listaExemploProf, listaExemploAluno):
                if (pessoas.cpf == primeiro.cpf or pessoas.cpf == segundo.cpf) and pessoas is not primeiro:
                    raise cpfDuplicado


        except idadeAluno:
            print("O professor '%s' não possui idade suficiente" % pessoas.nome)
            print()
            if pessoas in cadastro:
                cadastro.remove(pessoas)

        except titulacaoInferior:
            print("O professor '%s' não possui é doutor" % pessoas.nome)
            print()
            if pessoas in cadastro:
                cadastro.remove(pessoas)

        except cpfDuplicado:
            print("O professor '%s' tem o cpf de outra pessoa" % pessoas.nome)
            print()
            if pessoas in cadastro:
                cadastro.remove(pessoas)

    for pessoas in listaExemploAluno:
        try:
            if pessoas.idade < 18:
                raise idadeAluno

            if pessoas.curso not in ["CCO", "SIN"]:
                raise cursoInvalido

            for primeiro, segundo in zip(listaExemploProf, listaExemploAluno):
                if (pessoas.cpf == primeiro.cpf or pessoas.cpf == segundo.cpf) and pessoas is not segundo:
                    raise cpfDuplicado

        except idadeAluno:
            print("O aluno '%s' não possui idade suficiente" % pessoas.nome)
            print()
            if pessoas in cadastro:
                cadastro.remove(pessoas)

        except cursoInvalido:
            print("O aluno '%s' não é de CCO nem de SIN" % pessoas.nome)
            print()
            if pessoa in cadastro:
                cadastro.remove(pessoa)

        except cpfDuplicado:
            print("O aluno '%s' tem o cpf de outra pessoa" % pessoa.nome)
            print()
            if pessoa in cadastro:
              cadastro.remove(pessoa)

    for lista in cadastro:
        lista.printDescricao()
        print()
