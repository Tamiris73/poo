from abc import ABC, abstractmethod

class NaoEDoutor(Exception):
    pass

class IdadeMenorQueTrinta(Exception):
    pass

class NaoECCONemSIN(Exception):
    pass

class IdadeMenorQueDezoito(Exception):
    pass

class CPFRepetido(Exception):
    pass

class Pessoa(ABC):
    def __init__(self, nome, cpf, endereco, idade):
        self.__nome = nome
        self.__cpf = cpf
        self.__endereco = endereco
        self.__idade = idade

    @property
    def getNome(self):
        return self.__nome

    @property
    def getCpf(self):
        return self.__cpf

    @property
    def getEndereco(self):
        return self.__endereco

    @property
    def getIdade(self):
        return self.__idade

    @abstractmethod
    def printDescricao(self):
        pass


class Professor(Pessoa):
    def __init__(self, nome, cpf, endereco, idade, titulacao):
        super().__init__(nome, cpf, endereco, idade)
        self.__titulacao = titulacao

    @property
    def getTitulacao(self):
        return self.__titulacao

    def printDescricao(self):
        print("Nome: {}".format(self.getNome))
        print("cpf: {}".format(self.getCpf))
        print("Endereço: {}".format(self.getEndereco))
        print("Idade: {}".format(self.getIdade))
        print("Titulação: {}".format(self.getTitulacao))

        return 0


class Aluno(Pessoa):
    def __init__(self, nome, cpf, endereco, idade, curso):
        super().__init__(nome, cpf, endereco, idade)
        self.__curso = curso

    @property
    def getCurso(self):
        return self.__curso

    def printDescricao(self):
        print("Nome: {}".format(self.getNome))
        print("cpf: {}".format(self.getCpf))
        print("Endereço: {}".format(self.getEndereco))
        print("Idade: {}".format(self.getIdade))
        print("Curso: {}".format(self.getCurso))

        return 0

if __name__ == "__main__":
    P1 = Professor("Paulo", "12345671", 1, 41, "Doutor")
    P2 = Professor("maria", "12345672", 2, 29, "cachorro")
    P3 = Professor("antonio", "12345673", 3, 65, "estagiário")
    P4 = Professor("pedro", "12345674", 4, 55, "mestre")
    P5 = Professor("marisa", "12345675", 5, 43, "Doutor")
    P6 = Professor("ana", "12345671", 6, 12, "Doutor")
    A1 = Aluno("Paule", "22345671", 1, 21, "CCO")
    A2 = Aluno("marie", "22345672", 2, 22, "SIN")
    A3 = Aluno("antonie", "22345671", 3, 42, "CCO")
    A4 = Aluno("pedre", "22345674", 4, 32, "ECO")
    A5 = Aluno("marise", "12345675", 5, 19, "CCO")
    A6 = Aluno("ane", "22345671", 6, 16, "ECO")

    cadastro = [P1, P2, P3, P4, P5, P6, A1, A2, A3, A4, A5, A6]
    listaProfessor = [P1, P2, P3, P4, P5, P6]
    listaAluno = [A1, A2, A3, A4, A5, A6]

    for pessoa in listaProfessor:
        try:
            if pessoa.getIdade < 30:
                raise IdadeMenorQueTrinta

            if pessoa.getTitulacao != "Doutor":
                raise NaoEDoutor

            for primeiro, segundo in zip(listaProfessor, listaAluno):
                if (pessoa.getCpf == primeiro.getCpf or pessoa.getCpf == segundo.getCpf) and pessoa is not primeiro:
                    raise CPFRepetido


        except IdadeMenorQueTrinta:
            print("O professor '%s' não possui idade suficiente" % pessoa.getNome)
            print()
            if pessoa in cadastro:
                cadastro.remove(pessoa)

        except NaoEDoutor:
            print("O professor '%s' não possui cargo de doutor" % pessoa.getNome)
            print()
            if pessoa in cadastro:
                cadastro.remove(pessoa)

        except CPFRepetido:
            print("O professor '%s' está cometendo falsidade ideológica" % pessoa.getNome)
            print()
            if pessoa in cadastro:
                cadastro.remove(pessoa)

    for pessoa in listaAluno:
        try:
            if pessoa.getIdade < 18:
                raise IdadeMenorQueDezoito

            if pessoa.getCurso not in ["CCO", "SIN"]:
                raise NaoECCONemSIN

            for primeiro, segundo in zip(listaProfessor, listaAluno):
                if (pessoa.getCpf == primeiro.getCpf or pessoa.getCpf == segundo.getCpf) and pessoa is not segundo:
                    raise CPFRepetido

        except IdadeMenorQueDezoito:
            print("O aluno '%s' não possui idade suficiente" % pessoa.getNome)
            print()
            if pessoa in cadastro:
                cadastro.remove(pessoa)

        except NaoECCONemSIN:
            print("O aluno '%s' não é de CCO nem SIN" % pessoa.getNome)
            print()
            if pessoa in cadastro:
                cadastro.remove(pessoa)

        except CPFRepetido:
            print("O aluno '%s' está cometendo falsidade ideológica" % pessoa.getNome)
            print()
            if pessoa in cadastro:
                cadastro.remove(pessoa)

    for pessoas in cadastro:
        pessoas.printDescricao()
        print()
