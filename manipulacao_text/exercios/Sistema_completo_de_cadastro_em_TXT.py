def carregar_alunos(caminho):
    alunos = []
    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            for linha in f:
                p = linha.strip().split(";")
                if len(p) == 4:
                    alunos.append({
                        "id": int(p[0]),
                        "nome": p[1],
                        "idade": int(p[2]),
                        "curso": p[3]
                    })
    except FileNotFoundError:
        pass
    return alunos


def salvar_alunos(caminho, alunos):
    with open(caminho, 'w', encoding='utf-8') as f:
        for a in alunos:
            f.write(f"{a['id']};{a['nome']};{a['idade']};{a['curso']}\n")


def sistema_alunos():
    arquivo = 'alunos.txt'
    alunos = carregar_alunos(arquivo)

    opcao = ""
    while opcao != "6":
        print("\n===== SISTEMA DE ALUNOS =====")
        print("1 - Listar alunos")
        print("2 - Buscar aluno")
        print("3 - Cadastrar aluno")
        print("4 - Remover aluno")
        print("5 - Alterar aluno")
        print("6 - Sair")

        opcao = input("\nEscolha: ")

        if opcao == "1":
            print("\n--- Lista de Alunos ---")
            for a in alunos:
                print(f"{a['id']} - {a['nome']} - {a['idade']} anos")

        elif opcao == "2":
            id_busca = int(input("Digite o ID: "))
            encontrado = False
            for a in alunos:
                if a['id'] == id_busca:
                    print(f"\nAluno encontrado:\n{a['nome']}\n{a['idade']} anos\n{a['curso']}")
                    encontrado = True
                    break
            if not encontrado:
                print("\nAluno não encontrado!")

        elif opcao == "3":
            # Gera novo ID
            novo_id = max([a['id'] for a in alunos], default=0) + 1
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            curso = input("Curso: ")

            alunos.append({"id": novo_id, "nome": nome, "idade": idade, "curso": curso})
            salvar_alunos(arquivo, alunos)
            print("Aluno cadastrado com sucesso!")

        elif opcao == "4":
            id_rem = int(input("Digite o ID do aluno a remover: "))
            original_len = len(alunos)
            alunos = [a for a in alunos if a['id'] != id_rem]

            if len(alunos) < original_len:
                salvar_alunos(arquivo, alunos)
                print("Aluno removido com sucesso!")
            else:
                print("Aluno não encontrado.")

        elif opcao == "5":
            id_alt = int(input("Digite o ID do aluno a alterar: "))
            encontrado = False
            for a in alunos:
                if a['id'] == id_alt:
                    a['nome'] = input(f"Novo nome ({a['nome']}): ") or a['nome']
                    a['idade'] = int(input(f"Nova idade ({a['idade']}): ") or a['idade'])
                    a['curso'] = input(f"Novo curso ({a['curso']}): ") or a['curso']
                    salvar_alunos(arquivo, alunos)
                    print("Dados atualizados com sucesso!")
                    encontrado = True
                    break
            if not encontrado:
                print("Aluno não encontrado.")

        elif opcao == "6":
            print("Saindo do sistema...")
        else:
            print("Opção inválida!")


sistema_alunos()