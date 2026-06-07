
# Estruturas de dados iniciais do sistema Hospital de Teresina.

ESPECIALIDADES = (
    "Clinico Geral",
    "Pediatria",
    "Cardiologia",
    "Ortopedia",
    "Ginecologia",
)

# Tupla com os níveis de prioridade da triagem
# A prioridade vai de 1 (mais urgente) a 5 (menos urgente).
NIVEIS_PRIORIDADE = (
    "Emergencia (atendimento imediato)",
    "Muito urgente",
    "Urgente",
    "Pouco urgente",
    "Nao urgente",
)

# 3 testes para uso no main.py
pacientes = [
    {
        "id": 1,
        "nome": "Maria Silva",
        "cpf": "11111111111",
        "idade": 67,
        "especialidade": "Cardiologia",
        "prioridade": 2,
    },
    {
        "id": 2,
        "nome": "Joao Souza",
        "cpf": "22222222222",
        "idade": 8,
        "especialidade": "Pediatria",
        "prioridade": 3,
    },
    {
        "id": 3,
        "nome": "Ana Costa",
        "cpf": "33333333333",
        "idade": 34,
        "especialidade": "Clinico Geral",
        "prioridade": 4,
    },
]
cpfs_cadastrados = {paciente["cpf"] for paciente in pacientes}
