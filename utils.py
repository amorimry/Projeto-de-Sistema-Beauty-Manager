from classes import Cliente, Servico, Agendamento

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
        "nome": nome.title(),
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
        valor = input("Digite o valor do serviço: ")
        if valor == "":
            print("Preencha o campo VALOR.")
        else:
            valor = float(valor)
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
        "nome": nome.title(),
        "valor": valor,
        "duração": duracao
    }

def exibir_clientes(lista_de_clientes):
    nomes_clientes = []
    for n in lista_de_clientes:
        if n.nome not in nomes_clientes:
            nomes_clientes.append(n.nome)
            print(f"- {n.nome}\n")

def exibir_servicos(lista_de_servicos):
    nomes_servicos = []
    for s in lista_de_servicos:
        if s.nome not in nomes_servicos:
            nomes_servicos.append(s.nome)
            print(f"- {s.nome}\n")

def exibir_agendamentos(lista):
    for i, agendamento in enumerate(lista):
        print(f"""{i+1}. {agendamento.cliente.nome} | {agendamento.servico.nome}

{agendamento.data} | {agendamento.horario}H
""")

def agendar_atendimento(lista1, lista2, lista3):

    while True:
        nomes_clientes  = []
        print("== CLIENTES ==")

        for i, n in enumerate(lista1):
            if n.nome not in nomes_clientes:
                nomes_clientes.append(n.nome)
                print(f"{i+1}. {n.nome}\n")

        cliente_agendamento = input("Digite o número do cliente que deseja agendar um serviço: ")
        if cliente_agendamento == "":
            print("Preencha o campo.")
            continue
        else:
            cliente_agendamento = int(cliente_agendamento)
            indice_cliente = cliente_agendamento-1

            if indice_cliente >= 0 and indice_cliente < len(nomes_clientes):
                break
            else:
                print("Número de posição inválido, digite novamente.")

    while True:
        nomes_servicos = []
        print("== SERVIÇOS ==")

        for i, s in enumerate(lista2):
            if s.nome not in nomes_servicos:
                nomes_servicos.append(s.nome)
                print(f"{i+1} {s.nome}\n")
        
        servico_agendamento = input(f"Digite o número do serviço que deseja agendar: ")
        if servico_agendamento == "":
            print("Preencha o campo.")
            continue
        else:
            servico_agendamento = int(servico_agendamento)
            indice_servico = servico_agendamento-1

            if indice_servico >= 0 and indice_servico <= len(nomes_servicos):
                data_agendamento = input("Digite a data para o serviço (dd/mm/aaaa): ")
                horario_agendamento = input("Digite o horário do agendamento (hh:mm): ")
                for dh in lista3:
                    if dh.data == data_agendamento and dh.horario == horario_agendamento:
                        print("Já existe agendamento para essa data e horário.")
                        return None
                print("Agendamento finalizado!")
                return {
                        "cliente": lista1[indice_cliente],
                        "serviço": lista2[indice_servico],
                        "data": data_agendamento,
                        "horário": horario_agendamento
                        }
            else:
                print("Serviço não encontrado, digite novamente.")                

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