def contar_linhas():
    linhas = 0
    with open('nomes.txt', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            linhas += 1
    print(f"O arquivo possui {linhas} linhas.")

contar_linhas()