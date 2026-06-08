"""
Funções sistema Hospital de Teresina.
"""

from utils import (
    ler_inteiro,
    ler_texto,
    gerar_novo_id,
    escolher_especialidade,
    escolher_prioridade,
    descricao_prioridade,
    validar_cpf,
    confirmar,
    truncar,
    percorrer_pacientes,
)


def encontrar_por_id(pacientes, id_busca):
    for paciente in pacientes:
        if paciente["id"] == id_busca:
            return paciente
    return None


def mostrar_paciente(paciente):
    print("\nID............:", paciente["id"])
    print("Nome..........:", paciente["nome"])
    print("CPF...........:", paciente["cpf"])
    print("Idade.........:", paciente["idade"])
    print("Especialidade.:", paciente["especialidade"])
    print(
        f"Prioridade....: {paciente['prioridade']} "
        f"({descricao_prioridade(paciente['prioridade'])})"
    )


def criar_paciente(pacientes, cpfs_cadastrados):
    print("\n--- CADASTRAR PACIENTE ---")

    nome = ler_texto("Nome do paciente: ")

    while True:
        cpf = ler_texto("CPF (somente números, 11 dígitos): ")
        valido, mensagem = validar_cpf(cpf, cpfs_cadastrados)
        if valido:
            break
        print(f"  {mensagem}")

    idade = ler_inteiro("Idade: ")
    while idade <= 0 or idade > 120:
        print("  Idade inválida. Informe um valor entre 1 e 120.")
        idade = ler_inteiro("Idade: ")

    especialidade = escolher_especialidade()
    prioridade = escolher_prioridade()

    novo_paciente = {
        "id": gerar_novo_id(pacientes),
        "nome": nome,
        "cpf": cpf,
        "idade": idade,
        "especialidade": especialidade,
        "prioridade": prioridade,
    }

    pacientes.append(novo_paciente)
    cpfs_cadastrados.add(cpf)

    print(f"\nPaciente cadastrado com sucesso! ID = {novo_paciente['id']}")


def listar_pacientes(pacientes):
    print("\n--- LISTA DE PACIENTES ---")

    if len(pacientes) == 0:
        print("Nenhum paciente cadastrado.")
        return

    print(
        f"{'ID':<4}{'NOME':<20}{'IDADE':<7}"
        f"{'ESPECIALIDADE':<16}{'PRIOR.':<7}"
    )
    print("-" * 60)

    for paciente in percorrer_pacientes(pacientes):
        nome = truncar(paciente["nome"], 18)
        especialidade = truncar(paciente["especialidade"], 14)

        print(
            f"{paciente['id']:<4}"
            f"{nome:<20}"
            f"{paciente['idade']:<7}"
            f"{especialidade:<16}"
            f"{paciente['prioridade']:<7}"
        )


def buscar_paciente(pacientes):
    print("\n--- BUSCAR PACIENTE ---")
    print("1 - Buscar por ID")
    print("2 - Buscar por nome")

    opcao = ler_inteiro("Escolha: ")

    if opcao == 1:
        id_busca = ler_inteiro("Digite o ID: ")
        paciente = encontrar_por_id(pacientes, id_busca)

        if paciente is None:
            print("Paciente não encontrado.")
        else:
            mostrar_paciente(paciente)

    elif opcao == 2:
        termo = ler_texto("Digite parte do nome: ").lower()

        encontrados = [
            paciente
            for paciente in pacientes
            if termo in paciente["nome"].lower()
        ]

        if len(encontrados) == 0:
            print("Nenhum paciente encontrado com esse nome.")
        else:
            for paciente in encontrados:
                mostrar_paciente(paciente)

    else:
        print("Opção inválida.")


def atualizar_paciente(pacientes):
    print("\n--- ATUALIZAR PACIENTE ---")

    id_busca = ler_inteiro("Digite o ID do paciente: ")
    paciente = encontrar_por_id(pacientes, id_busca)

    if paciente is None:
        print("Paciente não encontrado.")
        return

    mostrar_paciente(paciente)

    print("\nDeixe em branco para manter o valor atual.")

    novo_nome = input("Novo nome: ").strip()
    if novo_nome != "":
        paciente["nome"] = novo_nome

    nova_idade = input("Nova idade: ").strip()
    if nova_idade != "":
        try:
            idade = int(nova_idade)

            if idade > 0:
                paciente["idade"] = idade
            else:
                print("  Idade ignorada (precisa ser maior que zero).")

        except ValueError:
            print("  Idade ignorada (valor não numérico).")

    if confirmar("Deseja trocar a especialidade?"):
        paciente["especialidade"] = escolher_especialidade()

    if confirmar("Deseja refazer a triagem (prioridade)?"):
        paciente["prioridade"] = escolher_prioridade()

    print("\nPaciente atualizado com sucesso!")


def excluir_paciente(pacientes, cpfs_cadastrados):
    print("\n--- EXCLUIR PACIENTE ---")

    id_busca = ler_inteiro("Digite o ID do paciente: ")
    paciente = encontrar_por_id(pacientes, id_busca)

    if paciente is None:
        print("Paciente não encontrado.")
        return

    mostrar_paciente(paciente)

    if confirmar("Tem certeza que deseja excluir este paciente?"):
        pacientes.remove(paciente)
        cpfs_cadastrados.discard(paciente["cpf"])
        print("Paciente excluído com sucesso.")
    else:
        print("Exclusão cancelada.")


def relatorio_pacientes_por_especialidade(pacientes):
    print("\n--- RELATÓRIO POR ESPECIALIDADE ---")

    if len(pacientes) == 0:
        print("Nenhum paciente cadastrado.")
        return

    contagem = {
        especialidade: sum(
            1 for p in pacientes if p["especialidade"] == especialidade
        )
        for especialidade in {p["especialidade"] for p in pacientes}
    }

    for especialidade, quantidade in contagem.items():
        print(f"  {especialidade}: {quantidade} paciente(s)")

    idosos = [p["nome"] for p in pacientes if p["idade"] >= 60]

    print(f"\nTotal de pacientes.....: {len(pacientes)}")
    print(f"Pacientes idosos (60+).: {len(idosos)}")

    if idosos:
        print("  -> " + ", ".join(idosos))


def fila_prioridade(pacientes):
    print("\n--- FILA DE PRIORIDADE (TRIAGEM) ---")

    if len(pacientes) == 0:
        print("Nenhum paciente na fila.")
        return

    fila = sorted(pacientes, key=lambda p: (p["prioridade"], p["id"]))

    posicao = 1

    for paciente in fila:
        descricao = descricao_prioridade(paciente["prioridade"])

        print(
            f"  {posicao}º [P{paciente['prioridade']}] "
            f"{paciente['nome']} - {descricao}"
        )

        posicao += 1
