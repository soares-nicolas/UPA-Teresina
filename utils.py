# funções auxiliares e geradoras

from dados import ESPECIALIDADES, NIVEIS_PRIORIDADE


def ler_inteiro(mensagem):
   # Lê um número inteiro do usuário, repetindo até o valor ser válido

    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            # Se o usuário digitar algo que não é número, reporta e repete
            print("  Entrada inválida, Digite apenas números inteiros.")


def ler_texto(mensagem):
    # Lê um texto obrigatório, que não pode ficar vazio
    while True:
        texto = input(mensagem).strip()
        if texto != "":
            return texto
        print("  Este campo é obrigatório. Tente novamente.")


def gerar_novo_id(pacientes):
    # Gera o próximo ID com base no maior ID já existente na lista
    if len(pacientes) == 0:
        return 1
    # Operador aritmético (+ 1) para criar o próximo ID
    maior_id = max(paciente["id"] for paciente in pacientes)
    return maior_id + 1


def escolher_especialidade():
    # Mostra a tupla de especialidades
    print("\nEspecialidades disponíveis:")
    # for percorrendo a tupla
    for indice, especialidade in enumerate(ESPECIALIDADES, start=1):
        print(f"  {indice} - {especialidade}")

    while True:
        opcao = ler_inteiro("Escolha o número da especialidade: ")
        # Operador relacional para validar se está dentro da lista.
        if 1 <= opcao <= len(ESPECIALIDADES):
            return ESPECIALIDADES[opcao - 1]
        print("  Opção fora da lista. Tente novamente.")


def escolher_prioridade():
    """Classifica a prioridade na triagem e devolve um número de 1 a 5.

    Prioridade 1 = mais urgente; prioridade 5 = menos urgente.
    O valor é validado ainda na tiragem).
    """
    print("\nTriagem - níveis de prioridade:")
    # for percorrendo a tupla
    for indice, descricao in enumerate(NIVEIS_PRIORIDADE, start=1):
        print(f"  {indice} - {descricao}")

    while True:
        prioridade = ler_inteiro("Classifique a prioridade (1 a 5): ")
        # Operador relacional para validar o intervalo permitido.
        if 1 <= prioridade <= 5:
            return prioridade
        print("  Prioridade inválida. Informe um número de 1 a 5.")


def descricao_prioridade(prioridade):
    return NIVEIS_PRIORIDADE[prioridade - 1]


def validar_cpf(cpf, cpfs_cadastrados):
    # Valida o CPF: 11 dígitos numéricos e sem duplicata
    if len(cpf) != 11 or not cpf.isdigit():
        return False, "O CPF deve conter exatamente 11 dígitos numéricos."
    if cpf in cpfs_cadastrados:
        return False, "Este CPF já está cadastrado."
    return True, "OK"


def confirmar(mensagem):
    # Pede uma confirmação (s/n) ao usuário e devolve True ou False.
    resposta = input(mensagem + " (s/n): ").strip().lower()
    return resposta[:1] == "s"


def truncar(texto, limite):
    # Encurta um texto longo usando slicing, para caber na tabela
    if len(texto) <= limite:
        return texto
    return texto[:limite - 3] + "..."


def percorrer_pacientes(pacientes):
    # Função geradora que percorre os pacientes um a um.

    for paciente in pacientes:
        yield paciente
