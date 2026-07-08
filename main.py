from classes import Cliente, Servico, Agendamento
import utils

lista_clientes = [
    Cliente("Ana Silva", "85952478563", "23562485692", "ana.silva@email.com"),
    Cliente("Bruno Souza", "85963247561", "03641251478", "bruno.souza@email.com"),
    Cliente("Carla Oliveira", "85965234475", "09547852315", "carla.oliveira@email.com"),
    Cliente("Diego Santos", "85965554782", "56474123058", "diego.santos@email.com"),
    Cliente("Elena Costa", "85963225541", "65874123584", "elena.costa@email.com")
]
lista_servicos = [
    Servico("Corte Feminino", 80.0, "45"),
    Servico("Escova", 50.0, "30"),
    Servico("Manicure", 35.0, "40"),
    Servico("Pedicure", 40.0, "45"),
    Servico("Hidratação", 120.0, "60")
]
lista_agendamentos = [
    Agendamento("Ana Silva", "Corte Feminino", "10/07/2026", "09:00"),
    Agendamento("Bruno Souza", "Hidratação", "10/07/2026", "10:00"),
    Agendamento("Carla Oliveira", "Manicure", "11/07/2026", "14:00"),
    Agendamento("Diego Santos", "Pedicure", "11/07/2026", "15:00"),
    Agendamento("Elena Costa", "Escova", "12/07/2026", "11:30")
]

print(f"""
{"="*10} Bem vindo ao Sistema Beauty Manager {"="*10}
""")
while True:
    print(f"""
    {"="*10} Menu de opções {"="*10}

        1. Cadastrar Cliente
        2. Cadastrar Serviço
        3. Agendar Atendimento
        4. Lista de Agendamentos
        5. Cancelar Agendamento

        0. Sair do Sistema Beauty Manager
    """)
    op = input("Digite sua opção: ")
    if op == "1":
        print(f"""
{"="*5} Cadastrar Cliente {"="*5}
""")
        dados_cliente = utils.cadastrar_cliente(lista_clientes) #cadastra meu cliente, pelo utils, e me retorna o cliente com as informações em uma lista, jogando dentro da variável dados_cliente

        novo_cliente = Cliente(
            dados_cliente["nome"],
            dados_cliente["telefone"],
            dados_cliente["cpf"],
            dados_cliente["email"]
        ) #passo a instanciar o meu cliente colocando ele em uma classe, pego uma variável qualquer, chamo a classe dele e depois passo a puxar os dados da lista para cada informação que minha classe precisa

        lista_clientes.append(novo_cliente)

        print("Cliente cadastrado com sucesso!")
  
    elif op == "2":
        print(f"""
{"="*5} Cadastrar Serviço {"="*5}
""")
        dados_servico = utils.cadastrar_servico()

        novo_servico = Servico(
            dados_servico["nome"],
            dados_servico["valor"],
            dados_servico["duração"]
        )
        
        lista_servicos.append(novo_servico)

        print("Serviço cadastrado com sucesso!")

    elif op == "3":
        print(f"""
{"="*5} Agendar Atendimentos {"="*5}
""")
        dados_agendamento = utils.agendar_atendimento(lista_clientes, lista_servicos, lista_agendamentos)

        novo_agendamento = Agendamento(
            dados_agendamento["cliente"],
            dados_agendamento["serviço"],
            dados_agendamento["data"],
            dados_agendamento["horário"]
        )

        lista_agendamentos.append(novo_agendamento)

    elif op == "4":
        print(f"""
{"="*5} Lista de Agendamentos {"="*5}
""")
        utils.exibir_agendamentos(lista_agendamentos)

    elif op == "5":
        print(f"""
{"="*5} Cancelar Agendamento {"="*5}
""")
        utils.exibir_agendamentos(lista_agendamentos)
        utils.remover_agendamento(lista_agendamentos)

    elif op == "0":
        print("Encenrrando programa, até breve!")
        break
    else:
        print("Opcão inválida, digite novamente.")
input("Digite Enter...")