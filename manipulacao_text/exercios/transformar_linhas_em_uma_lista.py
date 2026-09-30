def carregar_nomes():
    nomes = []
    with open('nomes.txt', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            nomes.append(linha.strip())
    print(nomes)

carregar_nomes()