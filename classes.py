class Cliente():
    def __init__(self, nome, telefone, cpf, email):
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf
        self.email = email

    def exibir_cliente(self):
        print(f"""
    == Cliente ==
Cliente: {self.nome}
Telefone: {self.telefone}
CPF: {self.cpf}
E-mail: {self.email}
""")

class Servico():
    def __init__(self, nome, valor, duracao):
        self.nome = nome
        self.valor = valor
        self.duracao = duracao

    def exibir_servico(self):
        print(f"""
    == Serviço ==
Tipo: {self.nome}
Valor: R${self.valor:.2f}
Duração em minutos: {self.duracao} min.
""")

class Agendamento():
    def __init__(self, cliente_objeto, servico_objeto, data, horario):
        self.cliente = cliente_objeto
        self.servico = servico_objeto
        self.data = data
        self.horario = horario

    def exibir_agendamento(self):
        print(str(self))

    def __str__(self):
        return f"""
    == Agendamento Completo ==
Cliente: {self.cliente.nome} | Telefone: {self.cliente.telefone}
Serviço: {self.servico.nome} | Valor: R$ {self.servico.valor:.2f}

Data: {self.data} | Horário: {self.horario}H
"""
