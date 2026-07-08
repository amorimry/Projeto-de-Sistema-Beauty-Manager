from classes import Cliente, Servico, Agendamento

def cadastrar_cliente():
    nome = input("Digite o nome do cliente: ")
    telefone = input("Digite o número do telefone do cliente: ")
    cpf = input("Digite o CPF do cliente: ")
    email = input("Digite o e-mail do cliente: ")

    return {
        "nome": nome.title,
        "telefone": telefone,
        "cpf": cpf,
        "email": email
    }

def cadastrar_servico():
    nome = input("Digite o nome do serviço: ")
    while True:
        valor = float(input("Digite o valor do serviço: "))
        if valor > 0:
            break
        else:
            print("Valor inválido, digite novamente.")
    duracao = input("Digite a duração, em minutos, do serviço: ")

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