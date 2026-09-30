def gerenciar_tarefas():
    tarefas = []

    # Carrega as tarefas existentes
    try:
        with open('tarefas.txt', 'r', encoding='utf-8') as f:
            for linha in f:
                tarefas.append(linha.strip())
    except FileNotFoundError:
        pass

    opcao = ""
    while opcao != "4":
        print("\n1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Remover tarefa")
        print("4 - Sair")

        opcao = input("\nEscolha: ")

        if opcao == "1":
            nova = input("Digite a tarefa: ")
            tarefas.append(nova)
        elif opcao == "2":
            print("\nTarefas:")
            for i, t in enumerate(tarefas, 1):
                print(f"{i}. {t}")
        elif opcao == "3":
            remover = input("Digite o nome da tarefa a remover: ")
            if remover in tarefas:
                tarefas.remove(remover)
                print("Tarefa removida!")
            else:
                print("Tarefa não encontrada.")
        elif opcao == "4":
            print("Saindo...")
        else:
            print("Opção inválida!")

        # Atualiza o arquivo em qualquer alteração/saída
        with open('tarefas.txt', 'w', encoding='utf-8') as f:
            for t in tarefas:
                f.write(f"{t}\n")


gerenciar_tarefas()