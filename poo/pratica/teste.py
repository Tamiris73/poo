class Sessao:
    def __init__(self, dia, mes, tipo_sessao):
        self.dia = dia
        self.mes = mes
        self.tipo_sessao = tipo_sessao


class TipoSessao:
    def __init__(self, nome, duracao, preco):
        self.nome = nome
        self.duracao = duracao
        self.preco = preco


class Paciente:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
        self.sessoes = []

    def addSessao(self, sessao):
        self.sessoes.append(sessao)

    def geraFichaPaciente(self, mes=None):
        print("Nome:", self.nome)
        print("Endereço:", self.endereco)

    def calculaValorDevido(self, mes):
        pass


class Convenio(Paciente):
    def __init__(self, nome, endereco, convenio, numero_cartao):
        super().__init__(nome, endereco)
        self.convenio = convenio
        self.numero_cartao = numero_cartao

    def geraFichaPaciente(self, mes=None):
        super().geraFichaPaciente()
        print("Convênio:", self.convenio)
        print("Número do cartão:", self.numero_cartao)
        if mes:
            for sessao in self.sessoes:
                if sessao.mes == mes:
                    print("Data: {}/{}, Tipo de sessão: {}".format(sessao.dia, sessao.mes, sessao.tipo_sessao.nome))
        else:
            for sessao in self.sessoes:
                print("Data: {}/{}, Tipo de sessão: {}".format(sessao.dia, sessao.mes, sessao.tipo_sessao.nome))

    def calculaValorDevido(self, mes):
        valor_total = 0
        for sessao in self.sessoes:
            if sessao.mes == mes:
                valor_total += sessao.tipo_sessao.preco * 0.6
        return valor_total


class Particular(Paciente):
    def __init__(self, nome, endereco, cpf):
        super().__init__(nome, endereco)
        self.cpf = cpf

    def geraFichaPaciente(self, mes=None):
        super().geraFichaPaciente()
        print("CPF:", self.cpf)
        if mes:
            for sessao in self.sessoes:
                if sessao.mes == mes:
                    print("Data: {}/{}, Tipo de sessão: {}".format(sessao.dia, sessao.mes, sessao.tipo_sessao.nome))
        else:
            for sessao in self.sessoes:
                print("Data: {}/{}, Tipo de sessão: {}".format(sessao.dia, sessao.mes, sessao.tipo_sessao.nome))

    def calculaValorDevido(self, mes):
        valor_total = 0
        for sessao in self.sessoes:
            if sessao.mes == mes:
                valor_total += sessao.tipo_sessao.preco
        return valor_total


if __name__ == "__main__":
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
    pac2.geraFichaPaciente()
    print()
    faturamento = 0
    for paciente in listaPac:
        faturamento += paciente.calculaValorDevido(9)
    print('Faturamento do mês 9: {}'.format(faturamento))