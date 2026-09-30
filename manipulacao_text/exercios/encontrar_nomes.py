def buscar_nome():
    nomes = []
    with open('nomes.txt', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            nomes.append(linha.strip())

    pesquisa = input("Digite o nome que deseja pesquisar: ")

    if pesquisa in nomes:
        print("Nome encontrado!")
    else:
        print("Nome não encontrado!")


buscar_nome()