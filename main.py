"""
crud -Hospital de Teresina

Menu e execução do programa.
"""

from dados import pacientes, cpfs_cadastrados
from funcoes import (
    criar_paciente,
    listar_pacientes,
    buscar_paciente,
    atualizar_paciente,
    excluir_paciente,
    relatorio_pacientes_por_especialidade,
    fila_prioridade,
)


def mostrar_menu():
    print("\n========================================")
    print("         HOSPITAL DE TERESINA   ")
    print("         Sistema de Pacientes   ")
    print("==========================================")
    print("1 - Cadastrar paciente")
    print("2 - Listar pacientes")
    print("3 - Buscar paciente")
    print("4 - Atualizar paciente")
    print("5 - Excluir paciente")
    print("6 - Relatório por especialidade")
    print("7 - Fila de prioridade (triagem)")
    print("0 - Sair")


def main():
    """Loop do sistema para as funcionalidades"""
  
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip()

        # Uso de estruturas condicionais 
        if opcao == "1":
            criar_paciente(pacientes, cpfs_cadastrados)
        elif opcao == "2":
            listar_pacientes(pacientes)
        elif opcao == "3":
            buscar_paciente(pacientes)
        elif opcao == "4":
            atualizar_paciente(pacientes)
        elif opcao == "5":
            excluir_paciente(pacientes, cpfs_cadastrados)
        elif opcao == "6":
            relatorio_pacientes_por_especialidade(pacientes)
        elif opcao == "7":
            fila_prioridade(pacientes)
        elif opcao == "0":
            print("\nEncerrando o sistema. Até logo!")
            break
        else:
            print("\nOpção inválida! Digite um número de 0 a 7.")


# Garante que o programa só roda quando o arquivo é executado diretamente.
if __name__ == "__main__":
    main()
