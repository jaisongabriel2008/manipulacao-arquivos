def menu_arquivo():
    opcao = ""
    while opcao != "4":
        print("\n1 - Ler arquivo")
        print("2 - Adicionar texto")
        print("3 - Sobrescrever arquivo")
        print("4 - Sair")

        opcao = input("\nEscolha: ")

        if opcao == "1":
            try:
                with open('notas.txt', 'r', encoding='utf-8') as f:
                    print(f.read())
            except FileNotFoundError:
                print("Arquivo notas.txt não existe ainda.")
        elif opcao == "2":
            texto = input("Digite o texto a adicionar: ")
            with open('notas.txt', 'a', encoding='utf-8') as f:
                f.write(texto + "\n")
        elif opcao == "3":
            texto = input("Digite o novo conteúdo: ")
            with open('notas.txt', 'w', encoding='utf-8') as f:
                f.write(texto + "\n")
        elif opcao == "4":
            print("Programa encerrado.")
        else:
            print("Opção inválida!")


menu_arquivo()