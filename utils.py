from classes import Cliente, Servico, Agendamento

# def salvar_nomes(lista1, lista2, lista3):
#     nomes_clientes = []
#     cpfs = []
#     servicos = []
#     data_agendamento = []
#     horario_agendamento = []

#     for n in lista1:
#         if len(nomes_clientes) == 0:
#             nomes_clientes.append(n.nome)
#         if len(nomes_clientes) > 0:
#             if n not in nomes_clientes:
#                 nomes_clientes.append(n.nome)
#     for c in lista1:
#         if len(cpfs) == 0:
#             cpfs.append(c.cpf)
#         if len(cpfs) > 0:
#             if c not in cpfs:
#                 cpfs.append(c.cpf)
#     for s in lista2:
#         if len(servicos) == 0:
#             servicos.append(s.nome)
#         if len(servicos) > 0:
#             if s not in servicos:
#                 servicos.append(s.nome)
#     for d in lista3:
#         if len(data_agendamento) == 0:
#             data_agendamento.append(d.data)
#         if len(data_agendamento) > 0:
#             if d not in data_agendamento:
#                 data_agendamento.append(d.data)
#     for h in lista3:
#         if len(horario_agendamento) == 0:
#             horario_agendamento.append(h.horario)
#         if len(horario_agendamento) > 0:
#             if h not in horario_agendamento:
#                 horario_agendamento.append(h.horario)

def cadastrar_cliente(lista):
    cpfs = []

    for c in lista:
        if c.cpf not in cpfs:
            cpfs.append(c.cpf)

    # print (cpfs)

    while True:
        nome = input("Digite o nome do cliente: ")
        if nome == "":
            print("Preeencha o campo NOME.")
        else:
            break
    while True:
        telefone = input("Digite o número do telefone do cliente: ")
        if telefone == "":
            print("Preeencha o campo TELEEFONE.")
        elif len(telefone) != 11:
            print("Digite um telefone válido.")
        else:
            break
    while True:
        cpf = input("Digite o CPF do cliente: ")
        if cpf == "":
            print("Preencha o campo CPF.")
        elif len(cpf) != 11:
            print("Digite um CPF válido.")
        elif cpf in cpfs:
            print("CPF já cadastrado no sistema.")
        else:
            break
    while True:
        email = input("Digite o e-mail do cliente: ")
        if email == "":
            print("Preencha o campo E-MAIL.")
        else:
            break

    return {
        "nome": nome.title,
        "telefone": telefone,
        "cpf": cpf,
        "email": email
    }

def cadastrar_servico():
    while True:
        nome = input("Digite o nome do serviço: ")
        if nome == "":
            print("Preeencha o campo NOME DO SERVIÇO.")
        else:
            break
    while True:
        valor = float(input("Digite o valor do serviço: "))
        if valor <= 0:
            print("Valor inválido, digite novamente.")
        else:
            break
    while True:
        duracao = input("Digite a duração, em minutos, do serviço: ")
        if duracao == "":
            print("Preencha o campo DURAÇÃO.")
        else:
            break

    return {
        "nome": nome,
        "valor": valor,
        "duração": duracao
    }

def exibir_clientes(lista):
    for i, nome_cliente in enumerate(lista):
        print(f"{i+1}. {nome_cliente.nome}\n")

def exibir_servicos(lista):
    for i, nome_servico in enumerate(lista):
        print(f"{i+1}. {nome_servico.nome}\n")

def exibir_agendamentos(lista):
    for i, agendamento in enumerate(lista):
        print(f"""{i+1} - {agendamento.cliente} | {agendamento.servico}
{agendamento.data} | {agendamento.horario}H\n""")

def agendar_atendimento(lista1, lista2, lista3):
    nomes_clientes = []
    nomes_servicos = []

    print("== CLIENTES ==")

    for nome_cliente in lista1:
        print(f"- {nome_cliente.nome}\n")
        nomes_clientes.append(nome_cliente.nome)

    cliente_agendamento = input("Digite o nome do cliente que deseja agendar um serviço: \n")

    if cliente_agendamento.title() in nomes_clientes:

        print("== SERVIÇOS ==")

        for nome_servico in lista2:
            print(f"- {nome_servico.nome}\n")
            nomes_servicos.append(nome_servico.nome)
        
        servico_agendamento = input(f"Digite o nome do serviço que deseja agendar: \n")

        if servico_agendamento.title() in nomes_servicos:
            data_agendamento = input("Digite a dapa para o serviço (dd/mm/aaaa): \n")
            horario_agendamento = input("Digite o horário do agendamento (hh:mm): \n")
            for dh in lista3:
                if dh.data == data_agendamento and dh.horario == horario_agendamento:
                    print("Já existe agendamento para essa data e horário.")
                    return

            print("Agendamento finalizado!")

            return {
                "cliente": {cliente_agendamento.title},
                "serviço": {servico_agendamento.title},
                "data": {data_agendamento},
                "horário": {horario_agendamento}
            }

        else:
            print("Serviço não encontrado, digite novamente.")
            
    else:
        print("Cliente não cadastrado no sistema, cadastre o cliente primeiro.")

def remover_agendamento(lista):
    op = int(input("Digite a posição do agendamento que deseja remover: "))
    agendamento_selecionado = lista[op-1]
    print("Deseja mesmo remover o agendamento abaixo?")
    agendamento_selecionado.exibir_agendamento()
    escolha = int(input("1. Sim\n2. Não\nDigite o número da sua escolha: "))
    if escolha == 1:
        lista.pop(op-1)
        print("Agendamento cancelado com sucesso.")
    elif escolha == 2:
        print("Agendamento NÃO cancelado.")