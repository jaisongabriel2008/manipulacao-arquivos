def cadastrar_produtos():
    produtos = []
    with open('produtos.txt', 'r', encoding='utf-8') as f:
        for linha in f:
            partes = linha.strip().split(";")
            if len(partes) == 3:
                prod = {
                    "nome": partes[0],
                    "preco": float(partes[1]),
                    "quantidade": int(partes[2])
                }
                produtos.append(prod)

    print(produtos)


cadastrar_produtos()